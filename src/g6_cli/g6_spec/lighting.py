from __future__ import annotations

from g6_cli.g6_spec import to_hex_str, UsbHidDataFragment

_LIGHTING_DISABLE_MODE = 0x3A02
_LIGHTING_DISABLE_INTERMEDIATE = 0x0600

_LIGHTING_ENABLE_PRE_1_MODE = 0x3A02
_LIGHTING_ENABLE_PRE_1_INTERMEDIATE = 0x0601

_LIGHTING_ENABLE_PRE_2_MODE = 0x3A06
_LIGHTING_ENABLE_PRE_2_INTERMEDIATE = 0x0400

_LIGHTING_ENABLE_RGB_MODE = 0x3A09
_LIGHTING_ENABLE_RGB_INTERMEDIATE = 0x0A00
_LIGHTING_ENABLE_RGB_AUDIO_FEATURE = 0x03


def lighting_disable() -> list[UsbHidDataFragment]:
    """
    Disable the RGB lighting on the G6 device.
    :return: The list of UsbHidDataFragment objects to send to the G6, to disable the RGB lighting.
    """
    return [
        UsbHidDataFragment(
            mode=_LIGHTING_DISABLE_MODE,
            intermediate=_LIGHTING_DISABLE_INTERMEDIATE,
            audio_feature=0x00,
            value=0x00000000,
            additional_payload=0x00,
        )
    ]


def lighting_enable_set_rgb(red: int, green: int, blue: int) -> list[UsbHidDataFragment]:
    """
    Set the RGB lighting on the G6 device to the specified color.
    :param red: The red component of the color (0..255).
    :param green: The green component of the color (0..255).
    :param blue: The blue component of the color (0..255).
    :return: The list of UsbHidDataFragment objects to send to the G6, to set the RGB lighting to the specified color.
    """
    if red < 0 or red > 255:
        raise ValueError(f"red must be between 0 and 255, got {red}")
    if green < 0 or green > 255:
        raise ValueError(f"green must be between 0 and 255, got {green}")
    if blue < 0 or blue > 255:
        raise ValueError(f"blue must be between 0 and 255, got {blue}")

    usb_hid_fragment_list: list[UsbHidDataFragment] = []
    for i in range(3):
        usb_hid_fragment_list.append(
            UsbHidDataFragment(
                mode=_LIGHTING_ENABLE_PRE_1_MODE,
                intermediate=_LIGHTING_ENABLE_PRE_1_INTERMEDIATE,
                audio_feature=0x00,
                value=0x00000000,
                additional_payload=0x00,
            )
        )
        usb_hid_fragment_list.append(
            UsbHidDataFragment(
                mode=_LIGHTING_ENABLE_PRE_2_MODE,
                intermediate=_LIGHTING_ENABLE_PRE_2_INTERMEDIATE,
                audio_feature=_LIGHTING_ENABLE_RGB_AUDIO_FEATURE,
                value=to_hex_str(0x01000100),
                additional_payload=0x00
            )
        )
        usb_hid_fragment_list.append(
            UsbHidDataFragment(
                mode=_LIGHTING_ENABLE_RGB_MODE,
                intermediate=_LIGHTING_ENABLE_RGB_INTERMEDIATE,
                audio_feature=_LIGHTING_ENABLE_RGB_AUDIO_FEATURE,
                value=to_hex_str(0x0101ff) + to_hex_str(blue),
                additional_payload=to_hex_str(green) + to_hex_str(red),
            )
        )

    return usb_hid_fragment_list
