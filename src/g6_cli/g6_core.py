import re

import hid

from g6_cli.g6_spec import UsbAudioData, UsbHidDataFragment

# G6 specific USB information
G6_VENDOR_ID = 0x041e
G6_PRODUCT_ID = 0x3256
# The G6 has five interfaces: 1 Audio Control, 2 Audio Streams and 2 HIDs.
# The endpoint of the first interface is used for audio control.
# The endpoint of the fourth interface is used by SoundBlaster Connect for HID communication - so
# will we, since data sent to the third interface is ignored by the device.
G6_AUDIO_CONTROL_INTERFACE = 0
G6_HID_INTERFACE = 4

# The udev rule to create in /etc/udev/rules.d/50-soundblaster-x-g6.rules
UDEV_RULE = r'SUBSYSTEM=="usb", ATTRS{idVendor}=="041e", ATTRS{idProduct}=="3256", TAG+="uaccess"'

# The payloads available to send to the G6
PAYLOAD_HEX_LINE_PATTERN = r'^[a-f0-9]{128}$'


class G6Device:
    def __init__(self, device_path_audio_interface: str, device_path_hid_interface: str):
        self.__device_path_audio_interface = device_path_audio_interface
        self.__device_path_hid_interface = device_path_hid_interface

    def get_device_path_audio_interface(self) -> str:
        return self.__device_path_audio_interface

    def get_device_path_hid_interface(self) -> str:
        return self.__device_path_hid_interface


def detect_device() -> G6Device:
    """
    Tries to detect the SoundBlaster X G6 device and returns the device path to it.

    From all connected USB HID devices, we filter all devices that do not match the desired vendor_id and product_id.
    Since we know, that we have to communicate with USB-Interface 0 (AudioControl) and 4 (HID), we also filter all
    other interfaces of the device. This approach is required, because the G6's endpoint of USB-Interface 3 (HID)
    ignores any data transmitted to it. We have to use the endpoint of the fourth interface!

    If the device itself or the required interfaces could not be found, an IOError is risen to let the program terminate.

    Example for a device_path: "b'5-2.1:1.4'"
    - Bus 5
    - Port 2 (USB-Hub at Bus)
    - Port 1 (G6 at Hub)
    - bConfigurationValue 1
    - Interface 4

    A tree output of all connected USB devices can be generated with the command `lsusb -t`.
    :return: The unique device_path to the G6.
    """
    # Try to detect the G6 device's interface paths.
    device_found = False
    device_path_audio_interface: str = ''
    device_path_hid_interface: str = ''
    for device_dict in hid.enumerate():
        if device_dict['vendor_id'] == G6_VENDOR_ID and device_dict['product_id'] == G6_PRODUCT_ID:
            device_found = True
            if device_dict['interface_number'] == G6_AUDIO_CONTROL_INTERFACE:
                device_path_audio_interface = device_dict['path']
                print(f'Device with AudioControl interface detected at path: {device_path_audio_interface}')
            if device_dict['interface_number'] == G6_HID_INTERFACE:
                device_path_hid_interface = device_dict['path']
                print(f'Device with HID interface detected at path: {device_path_hid_interface}')

    # Return a G6Device object if both interfaces were found. Otherwise, raise an IOError.
    if not device_path_hid_interface == '' and not device_path_audio_interface == '':
        return G6Device(device_path_audio_interface=device_path_audio_interface,
                        device_path_hid_interface=device_path_hid_interface)

    # If the device itself or the fourth interface could not be found, an IOError is risen to let the program terminate.
    if device_found:
        if device_path_hid_interface == '':
            raise IOError(f"The SoundBlaster X G6 device could be found having vendor_id='{G6_VENDOR_ID:#x}' and "
                          f"product_id='{G6_PRODUCT_ID:#x}'. But the required HID interface does not seem to be "
                          f"available. Something is wrong here, and thus, the program execution is terminated!")
        if device_path_audio_interface == '':
            raise IOError(f"The SoundBlaster X G6 device could be found having vendor_id='{G6_VENDOR_ID:#x}' and "
                          f"product_id='{G6_PRODUCT_ID:#x}'. But the required AudioControl interface does not "
                          f"seem to be available. Something is wrong here, and thus, the program execution is terminated!")
        raise IOError(
            f"The SoundBlaster X G6 device could be found having vendor_id='{G6_VENDOR_ID:#x}' and product_id"
            f"='{G6_PRODUCT_ID:#x}'. But the program got into an illegal state, and thus, it is terminated!")
    else:
        raise IOError(
            f"No SoundBlaster X G6 device could be found having vendor_id='{G6_VENDOR_ID:#x}' and "
            f"product_id='{G6_PRODUCT_ID:#x}'. Is the device connected to your system? Are you allowed to access the "
            f"device (missing udev-rules in linux)?")


def list_all_devices():
    """
    Simply prints information of all detected usb devices to the console
    """
    for device_dict in hid.enumerate():
        keys = list(device_dict.keys())
        keys.sort()
        for key in keys:
            print("%s : %s" % (key, device_dict[key]))
        print()


def send_to_device(device_path: str, payload_hex_lines: list[str], dry_run: bool) -> None:
    """
    Send the payload_hex_lines to an endpoint from the usb device, identified by the device_path.
    :param device_path: The detected usb device path for the G6.
    :param payload_hex_lines: A list of hexlines (raw usb payload) to send to the G6.
                              Each line must be 128 characters long (64 bytes).
    :param dry_run: whether to simulate communication with the device for program testing purposes.
                    If set to true, no data is sent to the G6!
    """
    try:
        print(f"Opening the device '{device_path}' ...")
        h = hid.device()
        h.open_path(device_path)
        print(f"Opening the device '{device_path}': ok.")

        print(f"Manufacturer: '{h.get_manufacturer_string()}'")
        print(f"Product: '{h.get_product_string()}'")
        print(f"Serial No: '{h.get_serial_number_string()}'")

        # enable non-blocking mode
        h.set_nonblocking(1)

        # Validate all hex_lines
        regex_pattern = re.compile(PAYLOAD_HEX_LINE_PATTERN)
        for hex_line in payload_hex_lines:
            if not regex_pattern.fullmatch(hex_line):
                raise ValueError(
                    f"The following hex_line is part of the payload, but it did not match the expected regex pattern! "
                    f"Pattern: '{PAYLOAD_HEX_LINE_PATTERN}'; "
                    f"Hex-Line: '{hex_line}'")

        for hex_line in payload_hex_lines:
            # Prepend an additional zero byte as report_id to the hex_line. Otherwise, the first byte from the actual
            # 64 byte payload is cut off, since it is interpreted as report_id and thus, not sent to the device.
            hex_line = '00' + hex_line

            # Convert the hex string to a list of integers
            integer_list = [int(hex_line[i:i + 2], 16) for i in range(0, len(hex_line), 2)]

            # send the data to the device
            print("Sending data to G6 ...")
            print(hex_line)
            if dry_run:
                print("This is a dry run. No data has been sent!")
            else:
                h.write(integer_list)
            print("Sending data to G6: ok.")

            # read back the response
            if not dry_run:
                print("Read the response:")
                while True:
                    d = h.read(64)
                    if d:
                        print(d)
                    else:
                        break

        print("Closing the device")
        h.close()

    except IOError as ex:
        print(f'Unable to open a connection to the device by path: {device_path}')
        print(ex)
        print('\nAre the udev rules set and used by the kernel?')
        print('Create a udev-rule file at `/etc/udev/rules.d/50-soundblaster-x-g6.rules` with the following content:')
        print(UDEV_RULE)
        print('\nIf the file already exists, it might not be used by the kernel. Try to reload the configuration with:')
        print("`sudo udevadm trigger`")


def send_audio_data_to_device(device: G6Device, audio_data_list: list[UsbAudioData], dry_run: bool) -> None:
    """
    Convert the audio_data_list to a list of hex strings and send them to the device.
    :param device: The detected usb device path for the G6.
    :param audio_data_list: The list of UsbAudioData objects to send to the G6.
    :param dry_run: Whether to simulate communication with the device for program testing purposes.
    """
    send_to_device(device.get_device_path_audio_interface(), [audio_data.__str__() for audio_data in audio_data_list],
                   dry_run)


def send_hid_data_to_device(device: G6Device, hid_data_list: list[UsbHidDataFragment], dry_run: bool) -> None:
    """
    Convert the hid_data_list to a list of hex strings and send them to the device.
    :param device: The detected usb device path for the G6.
    :param hid_data_list: The list of UsbHidDataFragment objects to send to the G6.
    :param dry_run: Whether to simulate communication with the device for program testing purposes.
    """
    send_to_device(device.get_device_path_hid_interface(), [hid_data.__str__() for hid_data in hid_data_list], dry_run)
