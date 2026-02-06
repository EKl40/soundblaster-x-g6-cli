from enum import Enum

from g6_cli.g6_spec import UsbAudioData, UsbHidDataFragment, get_mic_recording_volume_percent_bytes, \
    get_mic_monitoring_volume_percent_bytes, get_mic_boost_decibel_bytes, DataFragmentMode, \
    get_mic_voice_clarity_level_bytes, DataFragmentStatic, get_slider_percent_bytes

RECORDING_B_REQUEST = bytes.fromhex('01')
CHANNEL_1 = bytes.fromhex('0201')
CHANNEL_2 = bytes.fromhex('0202')

# Audio (USB Audio class) wIndex targets from the table
RECORDING_FU_W_INDEX = bytes.fromhex('0004')  # mute + mic recording volume live here
MIC_MONITORING_W_INDEX = bytes.fromhex('000A')  # mic monitoring level lives here


class MicrophoneEqualizerPreset(Enum):
    PRESET_1 = {'14': '0000 40C0', '15': '0000 80C0', '16': '0000 0000', '17': '0000 4000', '18': '0000 4040',
                '19': '0000 40C0', '1A': '0000 8040',
                '1B': '0000 A040'}
    PRESET_2 = {'14': '0000 40C0', '15': '0000 80C0', '16': '0000 0000', '17': '0000 4000', '18': '0000 8040',
                '19': '0000 00C0', '1A': '0000 0040',
                '1B': '0000 8040'}
    PRESET_3 = {'14': '0000 00C0', '15': '0000 40C0', '16': '0000 4040', '17': '0000 8040', '18': '0000 8040',
                '19': '0000 80C0', '1A': '0000 4040',
                '1B': '0000 0040'}
    PRESET_4 = {'14': '0000 40C0', '15': '0000 A0C0', '16': '0000 0000', '17': '0000 8040', '18': '0000 0000',
                '19': '0000 40C0', '1A': '0000 0000',
                '1B': '0000 0000'}
    PRESET_5 = {'14': '0000 00C0', '15': '0000 40C0', '16': '0000 0040', '17': '0000 8040', '18': '0000 8040',
                '19': '0000 0000', '1A': '0000 40C0',
                '1B': '0000 0040'}
    PRESET_6 = {'14': '0000 A0C0', '15': '0000 80C0', '16': '0000 00C0', '17': '0000 0000', '18': '0000 4040',
                '19': '0000 8040', '1A': '0000 C040',
                '1B': '0000 E040'}
    PRESET_7 = {'14': '0000 0000', '15': '0000 4040', '16': '0000 00C0', '17': '0000 80C0', '18': '0000 80C0',
                '19': '0000 00C0', '1A': '0000 A040',
                '1B': '0000 E040'}
    PRESET_8 = {'14': '0000 0000', '15': '0000 0000', '16': '0000 0040', '17': '0000 0040', '18': '0000 4040',
                '19': '0000 80C0', '1A': '0000 0040',
                '1B': '0000 8040'}
    PRESET_9 = {'14': '0000 0000', '15': '0000 0000', '16': '0000 0040', '17': '0000 0040', '18': '0000 00C0',
                '19': '0000 0000', '1A': '0000 80C0',
                '1B': '0000 8040'}
    PRESET_10 = {'14': '0000 0000', '15': '0000 0040', '16': '0000 00C0', '17': '0000 0000', '18': '0000 4040',
                 '19': '0000 A040', '1A': '0000 C040',
                 '1B': 'A040'}
    PRESET_DM_1 = {'14': '0000 0000', '15': '0000 0041', '16': '0000 0000', '17': '0000 4041', '18': '0000 4041',
                   '19': '0000 8040', '1A': '0000 0041',
                   '1B': '0000 2041'}


def recording_mute(mute: bool) -> list[UsbAudioData]:
    """
    Mute or unmute recording.
    :param mute: True to mute recording, False to unmute.
    :return: The list of UsbAudioData objects to send to the G6, to mute or unmute recording.
    """
    return [
        UsbAudioData(
            b_request=RECORDING_B_REQUEST,
            w_value=bytes.fromhex('0001'),
            w_index=RECORDING_FU_W_INDEX,
            w_length=bytes.fromhex('0100'),
            data_fragment=bytes.fromhex('01' if mute else '00'),
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

    value = get_mic_recording_volume_percent_bytes(volume_percent)
    return [
        UsbAudioData(
            b_request=RECORDING_B_REQUEST,
            w_value=CHANNEL_1,
            w_index=RECORDING_FU_W_INDEX,
            w_length=bytes.fromhex('0200'),
            data_fragment=value,
        ),
        UsbAudioData(
            b_request=RECORDING_B_REQUEST,
            w_value=CHANNEL_2,
            w_index=RECORDING_FU_W_INDEX,
            w_length=bytes.fromhex('0200'),
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

    value = get_mic_boost_decibel_bytes(decibel)
    return [
        UsbHidDataFragment.empty_additional_payload(mode=bytes.fromhex('3C04'), intermediate=bytes.fromhex('0000'),
                                                    audio_feature=bytes.fromhex('02'), value=value),
        UsbHidDataFragment.empty_additional_payload(mode=bytes.fromhex('3C02'), intermediate=bytes.fromhex('0100'),
                                                    audio_feature=bytes.fromhex('00'), value=bytes.fromhex('0000 0000')),
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

    value = get_mic_monitoring_volume_percent_bytes(volume_percent)
    return [
        UsbAudioData(
            b_request=RECORDING_B_REQUEST,
            w_value=CHANNEL_1,
            w_index=MIC_MONITORING_W_INDEX,
            w_length=bytes.fromhex('0200'),
            data_fragment=value,
        ),
        UsbAudioData(
            b_request=RECORDING_B_REQUEST,
            w_value=CHANNEL_2,
            w_index=MIC_MONITORING_W_INDEX,
            w_length=bytes.fromhex('0200'),
            data_fragment=value,
        ),
    ]


ACTIVATE_HEX = get_slider_percent_bytes(100)
DEACTIVATE_HEX = get_slider_percent_bytes(0)


def _toggle_audio_feature(audio_feature: bytes, enable: bool) -> list[UsbHidDataFragment]:
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
    return _toggle_audio_feature(audio_feature=bytes.fromhex('04'), enable=enable)


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

    value = get_mic_voice_clarity_level_bytes(level_percent)
    return [
        UsbHidDataFragment.empty_additional_payload(mode=DataFragmentMode.DATA.value,
                                                    intermediate=DataFragmentStatic.RECORDING_INTERMEDIATE.value,
                                                    audio_feature=bytes.fromhex('05'),
                                                    value=value),
        UsbHidDataFragment.empty_additional_payload(mode=DataFragmentMode.COMMIT.value,
                                                    intermediate=DataFragmentStatic.RECORDING_INTERMEDIATE.value,
                                                    audio_feature=bytes.fromhex('05'),
                                                    value=bytes.fromhex('0000 0000'))
    ]


def acoustic_echo_cancellation_enabled(enable: bool) -> list[UsbHidDataFragment]:
    """
    Enable or disable the acoustic echo cancellation feature for the microphone.
    :param enable: True to enable the feature, False to disable it.
    :return: The list of UsbHidDataFragment objects to send to the G6, to enable or disable the acoustic echo cancellation feature.
    """
    return _toggle_audio_feature(audio_feature=bytes.fromhex('00'), enable=enable)


def smart_volume_enabled(enable: bool) -> list[UsbHidDataFragment]:
    """
    Enable or disable the smart volume feature for the microphone.
    :param enable: True to enable the feature, False to disable it.
    :return: The list of UsbHidDataFragment objects to send to the G6, to enable or disable the smart volume feature.
    """
    return _toggle_audio_feature(audio_feature=bytes.fromhex('2C'), enable=enable)


def mic_equalizer_enabled(enable: bool) -> list[UsbHidDataFragment]:
    """
    Enable or disable the microphone equalizer feature for the microphone.
    :param enable: True to enable the feature, False to disable it.
    :return: The list of UsbHidDataFragment objects to send to the G6, to enable or disable the microphone equalizer feature.
    """
    return _toggle_audio_feature(audio_feature=bytes.fromhex('13'), enable=enable)


def mic_equalizer_preset(preset: MicrophoneEqualizerPreset) -> list[UsbHidDataFragment]:
    """
    Activate the specified microphone equalizer preset.
    :param preset: The preset to activate.
    :return: The list of UsbHidDataFragment objects to send to the G6, to activate the specified microphone equalizer preset.
    """
    audio_feature_hex_list = ['14', '15', '16', '17', '18', '19', '1A', '1B']
    fragment_list: list[UsbHidDataFragment] = []
    for audio_feature_hex in audio_feature_hex_list:
        audio_feature_bytes = bytes.fromhex(audio_feature_hex)
        fragment_list.append(
            UsbHidDataFragment.empty_additional_payload(mode=DataFragmentMode.DATA.value,
                                                        intermediate=DataFragmentStatic.RECORDING_INTERMEDIATE.value,
                                                        audio_feature=audio_feature_bytes,
                                                        value=bytes.fromhex(preset.value[audio_feature_hex])))
        fragment_list.append(
            UsbHidDataFragment.empty_additional_payload(mode=DataFragmentMode.COMMIT.value,
                                                        intermediate=DataFragmentStatic.RECORDING_INTERMEDIATE.value,
                                                        audio_feature=audio_feature_bytes,
                                                        value=bytes.fromhex('0000 0000')))
    return fragment_list
