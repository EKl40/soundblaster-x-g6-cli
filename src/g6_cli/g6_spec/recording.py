from enum import Enum

from g6_cli.g6_spec import UsbAudioData, UsbHidDataFragment, get_mic_recording_volume_percent_hex, \
    get_mic_monitoring_volume_percent_hex, get_mic_boost_decibel_hex, get_slider_percent_hex, DataFragmentMode, \
    get_mic_voice_clarity_level_hex, DataFragmentStatic

RECORDING_B_REQUEST = 0x01
CHANNEL_1 = 0x0102
CHANNEL_2 = 0x0202

# Audio (USB Audio class) wIndex targets from the table
RECORDING_FU_W_INDEX = 0x0004  # mute + mic recording volume live here
MIC_MONITORING_W_INDEX = 0x000A  # mic monitoring level lives here


class MicrophoneEqualizerPreset(Enum):
    PRESET_1 = {0x14: 0x40C0, 0x15: 0x80C0, 0x16: 0x0000, 0x17: 0x4000, 0x18: 0x4040, 0x19: 0x40C0, 0x1A: 0x8040,
                0x1B: 0xA040},
    PRESET_2 = {0x14: 0x40C0, 0x15: 0x80C0, 0x16: 0x0000, 0x17: 0x4000, 0x18: 0x8040, 0x19: 0x00C0, 0x1A: 0x0040,
                0x1B: 0x8040},
    PRESET_3 = {0x14: 0x00C0, 0x15: 0x40C0, 0x16: 0x4040, 0x17: 0x8040, 0x18: 0x8040, 0x19: 0x80C0, 0x1A: 0x4040,
                0x1B: 0x0040},
    PRESET_4 = {0x14: 0x40C0, 0x15: 0xA0C0, 0x16: 0x0000, 0x17: 0x8040, 0x18: 0x0000, 0x19: 0x40C0, 0x1A: 0x0000,
                0x1B: 0x0000},
    PRESET_5 = {0x14: 0x00C0, 0x15: 0x40C0, 0x16: 0x0040, 0x17: 0x8040, 0x18: 0x8040, 0x19: 0x0000, 0x1A: 0x40C0,
                0x1B: 0x0040},
    PRESET_6 = {0x14: 0xA0C0, 0x15: 0x80C0, 0x16: 0x00C0, 0x17: 0x0000, 0x18: 0x4040, 0x19: 0x8040, 0x1A: 0xC040,
                0x1B: 0xE040},
    PRESET_7 = {0x14: 0x0000, 0x15: 0x4040, 0x16: 0x00C0, 0x17: 0x80C0, 0x18: 0x80C0, 0x19: 0x00C0, 0x1A: 0xA040,
                0x1B: 0xE040},
    PRESET_8 = {0x14: 0x0000, 0x15: 0x0000, 0x16: 0x0040, 0x17: 0x0040, 0x18: 0x4040, 0x19: 0x80C0, 0x1A: 0x0040,
                0x1B: 0x8040},
    PRESET_9 = {0x14: 0x0000, 0x15: 0x0000, 0x16: 0x0040, 0x17: 0x0040, 0x18: 0x00C0, 0x19: 0x0000, 0x1A: 0x80C0,
                0x1B: 0x8040},
    PRESET_10 = {0x14: 0x0000, 0x15: 0x0040, 0x16: 0x00C0, 0x17: 0x0000, 0x18: 0x4040, 0x19: 0xA040, 0x1A: 0xC040,
                 0x1B: 0xA040},
    PRESET_DM_1 = {0x14: 0x0000, 0x15: 0x0041, 0x16: 0x0000, 0x17: 0x4041, 0x18: 0x4041, 0x19: 0x8040, 0x1A: 0x0041,
                   0x1B: 0x2041},


def recording_mute(mute: bool) -> list[UsbAudioData]:
    """
    Mute or unmute recording.
    :param mute: True to mute recording, False to unmute.
    :return: The list of UsbAudioData objects to send to the G6, to mute or unmute recording.
    """
    return [
        UsbAudioData(
            b_request=RECORDING_B_REQUEST,
            w_value=0x0001,
            w_index=RECORDING_FU_W_INDEX,
            w_length=0x0001,
            data_fragment=0x01 if mute else 0x00,
        )
    ]


def mic_recording_volume(volume_percent: int) -> list[UsbAudioData]:
    """
    Set mic recording volume (both channels) to the specified percentage.
    :param volume_percent: The volume percentage for the microphone recording. Supported: 0, 10, 20, ..., 100 (as captured in the table).
    :return: The list of UsbAudioData objects to send to the G6, to set mic recording volume.
    """
    if volume_percent < 0 or volume_percent > 100:
        raise ValueError(f"Mic recording volume must be between 0 and 100, got {volume_percent}")
    if volume_percent % 10 != 0:
        raise ValueError(f"Mic recording volume must be a multiple of 10, got {volume_percent}")

    value = get_mic_recording_volume_percent_hex(volume_percent)
    return [
        UsbAudioData(
            b_request=RECORDING_B_REQUEST,
            w_value=CHANNEL_1,
            w_index=RECORDING_FU_W_INDEX,
            w_length=0x0002,
            data_fragment=value,
        ),
        UsbAudioData(
            b_request=RECORDING_B_REQUEST,
            w_value=CHANNEL_2,
            w_index=RECORDING_FU_W_INDEX,
            w_length=0x0002,
            data_fragment=value,
        ),
    ]


def mic_boost(decibel: int) -> list[UsbHidDataFragment]:
    """
    Set the microphone boost level to the specified decibels.
    :param decibel: The boost level to set, in decibels. Supported: 0, 10, 20, ..., 30 dB (as captured in the table).
    :return: The list of UsbHidDataFragment objects to send to the G6, to set microphone boost level.
    """
    if decibel < 0 or decibel > 30:
        raise ValueError(f"Mic boost must be between 0 and 30 dB, got {decibel}")
    if decibel % 10 != 0:
        raise ValueError(f"Mic boost must be a multiple of 10 dB, got {decibel}")

    value = get_mic_boost_decibel_hex(decibel)
    return [
        UsbHidDataFragment.empty_additional_payload(mode=0x3C04, intermediate=0x0000, audio_feature=0x02, value=value),
        UsbHidDataFragment.empty_additional_payload(mode=0x3C02, intermediate=0x0100, audio_feature=0x00, value=0x00),
    ]


def mic_monitoring(volume_percent: int) -> list[UsbAudioData]:
    """
    Set mic monitoring level (sidetone) for both channels.
    :param volume_percent: The monitoring level to set. Supported: 0, 10, 20, ..., 100 (as captured in the table).
    :return: The list of UsbAudioData objects to send to the G6, to set mic monitoring level.
    """
    if volume_percent < 0 or volume_percent > 100:
        raise ValueError(f"Mic monitoring level must be between 0 and 100, got {volume_percent}")
    if volume_percent % 10 != 0:
        raise ValueError(f"Mic monitoring level must be a multiple of 10, got {volume_percent}")

    value = get_mic_monitoring_volume_percent_hex(volume_percent)
    return [
        UsbAudioData(
            b_request=RECORDING_B_REQUEST,
            w_value=CHANNEL_1,
            w_index=MIC_MONITORING_W_INDEX,
            w_length=0x0002,
            data_fragment=value,
        ),
        UsbAudioData(
            b_request=RECORDING_B_REQUEST,
            w_value=CHANNEL_2,
            w_index=MIC_MONITORING_W_INDEX,
            w_length=0x0002,
            data_fragment=value,
        ),
    ]


ACTIVATE_HEX = get_slider_percent_hex(100)
DEACTIVATE_HEX = get_slider_percent_hex(0)


def _toggle_audio_feature(audio_feature: int, enable: bool) -> list[UsbHidDataFragment]:
    """
    Enable or disable a specific recording audio feature.
    :param audio_feature: The audio feature to enable or disable, e.g.: Voice Clarity, Acoustic Echo Cancellation, etc.
    :param enable: enable=True to enable the feature, disable=False to disable it.
    :return: The list of UsbHidDataFragment objects to send to the G6, to enable or disable the specified audio feature.
    """
    return [
        UsbHidDataFragment.empty_additional_payload(
            mode=DataFragmentMode.DATA.value,
            intermediate=DataFragmentStatic.RECORDING_INTERMEDIATE.value,
            audio_feature=audio_feature,
            value=ACTIVATE_HEX if enable else DEACTIVATE_HEX
        ),
        UsbHidDataFragment.empty_additional_payload(
            mode=DataFragmentMode.COMMIT.value,
            intermediate=DataFragmentStatic.RECORDING_INTERMEDIATE.value,
            audio_feature=audio_feature,
            value=DEACTIVATE_HEX
        ),
    ]


def voice_clarity_enabled(enable: bool) -> list[UsbHidDataFragment]:
    """
    Enable or disable the voice clarity feature for the microphone.
    :param enable: enable=True to enable the feature, disable=False to disable it.
    :return: The list of UsbHidDataFragment objects to send to the G6, to enable or disable the voice clarity feature.
    """
    return _toggle_audio_feature(audio_feature=0x04, enable=enable)


def voice_clarity_level(level_percent: int) -> list[UsbHidDataFragment]:
    """
    Set the voice clarity level for the microphone.
    :param level_percent: The voice clarity level to set. Supported: 0, 20, 40, ..., 100 (as captured in the table).
    :return: The list of UsbHidDataFragment objects to send to the G6, to set the voice clarity level.
    """
    if level_percent < 0 or level_percent > 100:
        raise ValueError(f"Voice clarity level must be between 0 and 100, got {level_percent}")
    if level_percent % 20 != 0:
        raise ValueError(f"Voice clarity level must be a multiple of 20, got {level_percent}")

    value = get_mic_voice_clarity_level_hex(level_percent)
    return [
        UsbHidDataFragment.empty_additional_payload(mode=DataFragmentMode.DATA.value,
                                                    intermediate=DataFragmentStatic.RECORDING_INTERMEDIATE.value,
                                                    audio_feature=0x05,
                                                    value=value),
        UsbHidDataFragment.empty_additional_payload(mode=DataFragmentMode.COMMIT.value,
                                                    intermediate=DataFragmentStatic.RECORDING_INTERMEDIATE.value,
                                                    audio_feature=0x05,
                                                    value=0x00)
    ]


def acoustic_echo_cancellation_enabled(enable: bool) -> list[UsbHidDataFragment]:
    """
    Enable or disable the acoustic echo cancellation feature for the microphone.
    :param enable: True to enable the feature, False to disable it.
    :return: The list of UsbHidDataFragment objects to send to the G6, to enable or disable the acoustic echo cancellation feature.
    """
    return _toggle_audio_feature(audio_feature=0x00, enable=enable)


def smart_volume_enabled(enable: bool) -> list[UsbHidDataFragment]:
    """
    Enable or disable the smart volume feature for the microphone.
    :param enable: True to enable the feature, False to disable it.
    :return: The list of UsbHidDataFragment objects to send to the G6, to enable or disable the smart volume feature.
    """
    return _toggle_audio_feature(audio_feature=0x2C, enable=enable)


def mic_equalizer_enabled(enable: bool) -> list[UsbHidDataFragment]:
    """
    Enable or disable the microphone equalizer feature for the microphone.
    :param enable: True to enable the feature, False to disable it.
    :return: The list of UsbHidDataFragment objects to send to the G6, to enable or disable the microphone equalizer feature.
    """
    return _toggle_audio_feature(audio_feature=0x13, enable=enable)


def mic_equalizer_preset(preset: MicrophoneEqualizerPreset) -> list[UsbHidDataFragment]:
    """
    Activate the specified microphone equalizer preset.
    :param preset: The preset to activate.
    :return: The list of UsbHidDataFragment objects to send to the G6, to activate the specified microphone equalizer preset.
    """
    fragment_list: list[UsbHidDataFragment] = []
    for audio_feature in range(0x14, 0x1C):
        fragment_list.append(
            UsbHidDataFragment.empty_additional_payload(mode=DataFragmentMode.DATA.value,
                                                        intermediate=DataFragmentStatic.RECORDING_INTERMEDIATE.value,
                                                        audio_feature=audio_feature,
                                                        value=preset.value[audio_feature]))
        fragment_list.append(
            UsbHidDataFragment.empty_additional_payload(mode=DataFragmentMode.COMMIT.value,
                                                        intermediate=DataFragmentStatic.RECORDING_INTERMEDIATE.value,
                                                        audio_feature=audio_feature,
                                                        value=0x00))
    return fragment_list
