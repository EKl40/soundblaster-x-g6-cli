from g6_cli.g6_spec import (
    UsbAudioData,
    get_mic_monitoring_volume_percent_hex,
    get_mic_recording_volume_percent_hex,
)

MIXER_B_REQUEST = 0x01
CHANNEL_1 = 0x0102
CHANNEL_2 = 0x0202

PLAYBACK = 0x0001

MONITORING_LINE_IN = 0x0009
MONITORING_EXTERNAL_MIC = 0x000A
MONITORING_SPDIF_IN = 0x000C

RECORDING_LINE_IN = 0x0003
RECORDING_EXTERNAL_MIC = 0x0004
RECORDING_SPDIF_IN = 0x0005
RECORDING_WHAT_U_HEAR = 0x0006


def _validate_volume_percent(volume_percent: int) -> None:
    if volume_percent < 0 or volume_percent > 100:
        raise ValueError(f"Volume percentage must be between 0 and 100, got {volume_percent}")
    if volume_percent % 10 != 0:
        raise ValueError(f"Volume percentage must be a multiple of 10, got {volume_percent}")


def _unit_mute(w_index: int, mute: bool) -> list[UsbAudioData]:
    return [
        UsbAudioData(
            b_request=MIXER_B_REQUEST,
            w_value=0x0001,
            w_index=w_index,
            w_length=0x0100,
            data_fragment=0x01 if mute else 0x00,
        )
    ]


def _unit_volume(w_index: int, volume_hex: int) -> list[UsbAudioData]:
    return [
        UsbAudioData(
            b_request=MIXER_B_REQUEST,
            w_value=CHANNEL_1,
            w_index=w_index,
            w_length=0x0200,
            data_fragment=volume_hex,
        ),
        UsbAudioData(
            b_request=MIXER_B_REQUEST,
            w_value=CHANNEL_2,
            w_index=w_index,
            w_length=0x0200,
            data_fragment=volume_hex,
        ),
    ]


def playback_mute(mute: bool) -> list[UsbAudioData]:
    """
    Mute or unmute the playback.
    :param mute: Whether to mute or unmute playback.
    :return: The list of UsbAudioData objects to send to the G6, to mute or unmute playback.
    """
    return _unit_mute(w_index=PLAYBACK, mute=mute)


def monitoring_line_in_mute(mute: bool) -> list[UsbAudioData]:
    """
    Mute or unmute the monitoring for the Line-In.
    :param mute: Whether to mute or unmute monitoring for the Line-In.
    :return: The list of UsbAudioData objects to send to the G6, to mute or unmute monitoring.
    """
    return _unit_mute(MONITORING_LINE_IN, mute)


def monitoring_line_in_volume(volume_percent: int) -> list[UsbAudioData]:
    """
    Set the Line-In monitoring volume (0..100, step 10).
    :param volume_percent: The volume percentage to set for Line-In monitoring (0..100, step 10).
    :return: The list of UsbAudioData objects to send to the G6, to set the monitoring volume.
    """
    _validate_volume_percent(volume_percent)
    volume_hex = get_mic_monitoring_volume_percent_hex(volume_percent)
    return _unit_volume(MONITORING_LINE_IN, volume_hex)


def monitoring_external_mic_mute(mute: bool) -> list[UsbAudioData]:
    """
    Mute or unmute the monitoring for the External-Mic.
    :param mute: Whether to mute or unmute monitoring for the External-Mic.
    :return: The list of UsbAudioData objects to send to the G6, to mute or unmute monitoring.
    """
    return _unit_mute(MONITORING_EXTERNAL_MIC, mute)


def monitoring_external_mic_volume(volume_percent: int) -> list[UsbAudioData]:
    """
    Set the External-Mic monitoring volume (0..100, step 10).
    :param volume_percent: The volume percentage to set for External-Mic monitoring (0..100, step 10).
    :return: The list of UsbAudioData objects to send to the G6, to set the monitoring volume.
    """
    _validate_volume_percent(volume_percent)
    volume_hex = get_mic_monitoring_volume_percent_hex(volume_percent)
    return _unit_volume(MONITORING_EXTERNAL_MIC, volume_hex)


def monitoring_spdif_in_mute(mute: bool) -> list[UsbAudioData]:
    """
    Mute or unmute the monitoring for the SPDIF-In.
    :param mute: Whether to mute or unmute monitoring for the SPDIF-In.
    :return: The list of UsbAudioData objects to send to the G6, to mute or unmute monitoring.
    """
    return _unit_mute(MONITORING_SPDIF_IN, mute)


def monitoring_spdif_in_volume(volume_percent: int) -> list[UsbAudioData]:
    """
    Set the SPDIF-In monitoring volume (0..100, step 10).
    :param volume_percent: The volume percentage to set for SPDIF-In monitoring (0..100, step 10).
    :return: The list of UsbAudioData objects to send to the G6, to set the monitoring volume.
    """
    _validate_volume_percent(volume_percent)
    volume_hex = get_mic_monitoring_volume_percent_hex(volume_percent)
    return _unit_volume(MONITORING_SPDIF_IN, volume_hex)


def recording_line_in_mute(mute: bool) -> list[UsbAudioData]:
    """
    Mute or unmute the recording for the Line-In.
    :param mute: Whether to mute or unmute recording for the Line-In.
    :return: The list of UsbAudioData objects to send to the G6, to mute or unmute recording.
    """
    return _unit_mute(RECORDING_LINE_IN, mute)


def recording_line_in_volume(volume_percent: int) -> list[UsbAudioData]:
    """
    Set the Line-In recording volume (0..100, step 10).
    :param volume_percent: The volume percentage to set for Line-In recording (0..100, step 10).
    :return: The list of UsbAudioData objects to send to the G6, to set the recording volume.
    """
    _validate_volume_percent(volume_percent)
    volume_hex = get_mic_recording_volume_percent_hex(volume_percent)
    return _unit_volume(RECORDING_LINE_IN, volume_hex)


def recording_external_mic_mute(mute: bool) -> list[UsbAudioData]:
    """
    Mute or unmute the recording for the External-Mic.
    :param mute: Whether to mute or unmute recording for the External-Mic.
    :return: The list of UsbAudioData objects to send to the G6, to mute or unmute recording.
    """
    return _unit_mute(RECORDING_EXTERNAL_MIC, mute)


def recording_external_mic_volume(volume_percent: int) -> list[UsbAudioData]:
    """
    Set the External-Mic recording volume (0..100, step 10).
    :param volume_percent: The volume percentage to set for External-Mic recording (0..100, step 10).
    :return: The list of UsbAudioData objects to send to the G6, to set the recording volume.
    """
    _validate_volume_percent(volume_percent)
    volume_hex = get_mic_recording_volume_percent_hex(volume_percent)
    return _unit_volume(RECORDING_EXTERNAL_MIC, volume_hex)


def recording_spdif_in_mute(mute: bool) -> list[UsbAudioData]:
    """
    Mute or unmute the recording for the SPDIF-In.
    :param mute: Whether to mute or unmute recording for the SPDIF-In.
    :return: The list of UsbAudioData objects to send to the G6, to mute or unmute recording.
    """
    return _unit_mute(RECORDING_SPDIF_IN, mute)


def recording_spdif_in_volume(volume_percent: int) -> list[UsbAudioData]:
    """
    Set the SPDIF-In recording volume (0..100, step 10).
    :param volume_percent: The volume percentage to set for SPDIF-In recording (0..100, step 10).
    :return: The list of UsbAudioData objects to send to the G6, to set the recording volume.
    """
    _validate_volume_percent(volume_percent)
    volume_hex = get_mic_recording_volume_percent_hex(volume_percent)
    return _unit_volume(RECORDING_SPDIF_IN, volume_hex)


def recording_what_u_hear_mute(mute: bool) -> list[UsbAudioData]:
    """
    Mute or unmute the recording for the What-U-Hear.
    :param mute: Whether to mute or unmute recording for the What-U-Hear.
    :return: The list of UsbAudioData objects to send to the G6, to mute or unmute recording.
    """
    return _unit_mute(RECORDING_WHAT_U_HEAR, mute)


def recording_what_u_hear_volume(volume_percent: int) -> list[UsbAudioData]:
    """
    Set the What-U-Hear recording volume (0..100, step 10).
    :param volume_percent: The volume percentage to set for What-U-Hear recording (0..100, step 10).
    :return: The list of UsbAudioData objects to send to the G6, to set the recording volume.
    """
    _validate_volume_percent(volume_percent)
    volume_hex = get_mic_recording_volume_percent_hex(volume_percent)
    return _unit_volume(RECORDING_WHAT_U_HEAR, volume_hex)
