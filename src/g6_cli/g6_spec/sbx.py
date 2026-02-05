from g6_cli.g6_spec import UsbHidDataFragment, DataFragmentMode, AudioFeature, get_slider_percent_hex, \
    SmartVolumeSpecialHex

ACTIVATE_HEX = get_slider_percent_hex(100)
DEACTIVATE_HEX = get_slider_percent_hex(0)


def sbx_toggle(audio_feature: AudioFeature, activate: bool) -> list[UsbHidDataFragment]:
    """
    Toggle a specific audio feature on or off.

    :param audio_feature: The audio feature to toggle on or off, e.g. Surround, Bass, Crystalizer, etc.
    :param activate: Whether to activate (True) or deactivate (False) the feature.
    :return: The list of UsbHidDataFragment objects to send to the G6, to toggle the specified audio feature on or off.
    """
    return [
        UsbHidDataFragment.from_enum(mode=DataFragmentMode.DATA, audio_feature=audio_feature.value,
                                     value=ACTIVATE_HEX if activate else DEACTIVATE_HEX),
        UsbHidDataFragment.from_enum(mode=DataFragmentMode.COMMIT, audio_feature=audio_feature.value,
                                     value=0x00),
    ]


def sbx_slider(audio_feature: AudioFeature, value: int) -> list[UsbHidDataFragment]:
    """
    Set the slider value of a specific audio feature.
    :param audio_feature: The audio feature to set the slider value for, e.g. Surround, Bass, Crystalizer, etc.
    :param value: The slider value to set (0 - 100).
    :return: The list of UsbHidDataFragment objects to send to the G6, to set the slider value of the specified audio feature.
    """
    if value < 0 or value > 100:
        raise ValueError(f"Slider value must be between 0 and 100, got {value}")
    return [
        UsbHidDataFragment.from_enum(mode=DataFragmentMode.DATA, audio_feature=audio_feature.value,
                                     value=get_slider_percent_hex(value)),
        UsbHidDataFragment.from_enum(mode=DataFragmentMode.COMMIT, audio_feature=audio_feature.value,
                                     value=0x00),
    ]


def sbx_smart_volume_special(smart_volume_special_hex: SmartVolumeSpecialHex) -> list[UsbHidDataFragment]:
    """
    Set the Smart Volume Special mode.
    :param smart_volume_special_hex: The Smart Volume Special mode to set, e.g.: Night or Loud
    :return: The list of UsbHidDataFragment objects to send to the G6, to set the Smart Volume Special mode.
    """
    return [
        UsbHidDataFragment.from_enum(mode=DataFragmentMode.DATA, audio_feature=AudioFeature.SMART_VOLUME_SPECIAL.value,
                                     value=smart_volume_special_hex.value),
        UsbHidDataFragment.from_enum(mode=DataFragmentMode.COMMIT,
                                     audio_feature=AudioFeature.SMART_VOLUME_SPECIAL.value,
                                     value=0x00)
    ]
