import re

import hid

from g6_payload import PAYLOAD_HEX_LINE_PATTERN
from g6_spec import AudioFeature, SmartVolumeSpecialHex
from g6_util import to_bool

# G6 specific USB information
G6_VENDOR_ID = 0x041e
G6_PRODUCT_ID = 0x3256
# The G6 has four interface (2 Audio and 2 HID), the endpoint of the fourth interface is used by SoundBlaster Connect.
# So will we, since data sent to the third interface is ignored by the device.
G6_INTERFACE = 4

# The udev rule to create in /etc/udev/rules.d/50-soundblaster-x-g6.rules
UDEV_RULE = r'SUBSYSTEM=="usb", ATTRS{idVendor}=="041e", ATTRS{idProduct}=="3256", TAG+="uaccess"'


def detect_device():
    """
    Tries to detect the SoundBlaster X G6 device and returns the device path to it.

    From all connected USB HID devices, we filter all devices which do not match the desired vendor_id and product_id.
    Since we know, that we have to communicate with USB-Interface 4, we also filter all other interfaces of the device.
    This approach is required, because the G6's endpoint of the third HID interface ignores any data transmitted to
    it. We have to use the endpoint of the fourth interface!

    If the device itself or the fourth interface could not be found, an IOError is risen to let the program terminate.

    Example for a device_path: "b'5-2.1:1.4'"
    - Bus 5
    - Port 2 (USB-Hub at Bus)
    - Port 1 (G6 at Hub)
    - bConfigurationValue 1
    - Interface 4

    A tree output of all connected USB devices can be generated with the command `lsusb -t`.
    :return: The unique device_path to the G6.
    """
    device_found = False
    for device_dict in hid.enumerate():
        if device_dict['vendor_id'] == G6_VENDOR_ID and device_dict['product_id']:
            device_found = True
            if G6_PRODUCT_ID and device_dict['interface_number'] == G6_INTERFACE:
                device_path = device_dict['path']
                print(f'Device detected at path: {device_path}')
                return device_path
    if device_found:
        raise IOError(
            f"The SoundBlaster X G6 device could be found having vendor_id='{G6_VENDOR_ID:#x}' and product_id"
            f"='{G6_PRODUCT_ID:#x}'. But the required fourth HDI interface does not seem to be available. "
            f"Something is wrong here, and thus, the program execution is terminated!")
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


def send_to_device(device_path, payload_hex_lines, dry_run):
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


# TODO G6 gui will call this method
def device_set_audio_effects(device_path, audio, args):
    """
    Sends all as CLI args given audio effects to the device.
    :param device_path: The detected usb device path for the G6.
    :param audio: An instance of the class Audio from g6_spec.py
    :param args: the CLI arguments, recently parsed by argparse in parse_cli_args()
    """
    # surround
    if args.set_surround is not None:
        hex_lines = audio.build_hex_lines_toggle(AudioFeature.SURROUND_TOGGLE, to_bool(args.set_surround))
        send_to_device(device_path, hex_lines, args.dry_run)
    if args.set_surround_value is not None:
        hex_lines = audio.build_hex_lines_slider(AudioFeature.SURROUND_SLIDER, args.set_surround_value)
        send_to_device(device_path, hex_lines, args.dry_run)

    # crystalizer
    if args.set_crystalizer is not None:
        hex_lines = audio.build_hex_lines_toggle(AudioFeature.CRYSTALIZER_TOGGLE, to_bool(args.set_crystalizer))
        send_to_device(device_path, hex_lines, args.dry_run)
    if args.set_crystalizer_value is not None:
        hex_lines = audio.build_hex_lines_slider(AudioFeature.CRYSTALIZER_SLIDER, args.set_crystalizer_value)
        send_to_device(device_path, hex_lines, args.dry_run)

    # bass
    if args.set_bass is not None:
        hex_lines = audio.build_hex_lines_toggle(AudioFeature.BASS_TOGGLE, to_bool(args.set_bass))
        send_to_device(device_path, hex_lines, args.dry_run)
    if args.set_bass_value is not None:
        hex_lines = audio.build_hex_lines_slider(AudioFeature.BASS_SLIDER, args.set_bass_value)
        send_to_device(device_path, hex_lines, args.dry_run)

    # smart-volume
    if args.set_smart_volume is not None:
        hex_lines = audio.build_hex_lines_toggle(AudioFeature.SMART_VOLUME_TOGGLE, to_bool(args.set_smart_volume))
        send_to_device(device_path, hex_lines, args.dry_run)
    if args.set_smart_volume_value is not None:
        hex_lines = audio.build_hex_lines_slider(AudioFeature.SMART_VOLUME_SLIDER, args.set_smart_volume_value)
        send_to_device(device_path, hex_lines, args.dry_run)
    if args.set_smart_volume_special_value is not None:
        smart_volume_special_value: SmartVolumeSpecialHex
        if args.set_smart_volume_special_value == 'Night':
            smart_volume_special_value = SmartVolumeSpecialHex.SMART_VOLUME_NIGHT
        elif args.set_smart_volume_special_value == 'Loud':
            smart_volume_special_value = SmartVolumeSpecialHex.SMART_VOLUME_LOUD
        else:
            raise ValueError(f'Expected one of the following values for --smart-volume-special-value: '
                             f'[\'Night\', \'Loud\'], but was \'{args.set_smart_volume_special_value}\'!')
        hex_lines = audio.build_hex_lines_slider_special(AudioFeature.SMART_VOLUME_SPECIAL, smart_volume_special_value)
        send_to_device(device_path, hex_lines, args.dry_run)

    # dialog-plus
    if args.set_dialog_plus is not None:
        hex_lines = audio.build_hex_lines_toggle(AudioFeature.DIALOG_PLUS_TOGGLE, to_bool(args.set_dialog_plus))
        send_to_device(device_path, hex_lines, args.dry_run)
    if args.set_dialog_plus_value is not None:
        hex_lines = audio.build_hex_lines_slider(AudioFeature.DIALOG_PLUS_SLIDER, args.set_dialog_plus_value)
        send_to_device(device_path, hex_lines, args.dry_run)
