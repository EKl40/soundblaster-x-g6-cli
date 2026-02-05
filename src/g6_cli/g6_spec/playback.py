from g6_cli.g6_spec import UsbAudioData, UsbHidDataFragment, get_playback_volume_percent_hex, PlaybackFilter

PLAYBACK_B_REQUEST = 0x01
CHANNEL_1 = 0x0102
CHANNEL_2 = 0x0202
DIRECT_MODE = 0x0005
SPDIF_OUT_DIRECT_MODE = 0x000d


def playback_mute(mute: bool) -> list[UsbAudioData]:
    """
    Mute or activate the playback.
    :param: mute: True to mute, False to activate
    :return: The list of UsbAudioData objects to send to the G6, to mute or unmute playback.
    """
    return [UsbAudioData(b_request=PLAYBACK_B_REQUEST, w_value=0x0001, w_index=0x0001, w_length=0x0001,
                         data_fragment=0x01 if mute else 0x00)]


def toggle_to_speakers() -> list[UsbHidDataFragment]:
    """
    Toggle the playback to speakers.
    :return: The list of UsbHidDataFragment objects to send to the G6, to toggle playback to speakers.
    """
    return [
        UsbHidDataFragment.empty_additional_payload(mode=0x2c05, intermediate=0x0002, audio_feature=0x00, value=0x0000),
        UsbHidDataFragment.empty_additional_payload(mode=0x2c01, intermediate=0x0100, audio_feature=0x00, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x0A, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x0A, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x0B, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x0B, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x0C, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x0C, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x0D, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x0D, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x0E, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x0E, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x0F, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x0F, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x10, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x10, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x11, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x11, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x12, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x12, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x13, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x13, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x14, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x14, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x09, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x09, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x09, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x09, value=0x0000),
    ]


def toggle_to_headphones() -> list[UsbHidDataFragment]:
    """
    Toggle the playback to headphones.
    :return: The list of UsbHidDataFragment objects to send to the G6, to toggle playback to headphones.
    """
    return [
        UsbHidDataFragment.empty_additional_payload(mode=0x2c05, intermediate=0x0004, audio_feature=0x00, value=0x0000),
        UsbHidDataFragment.empty_additional_payload(mode=0x2c01, intermediate=0x0100, audio_feature=0x00, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x0A, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x0A, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x0B, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x0B, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x0C, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x0C, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x0D, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x0D, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x0E, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x0E, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x0F, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x0F, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x10, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x10, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x11, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x11, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x12, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x12, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x13, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x13, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x14, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x14, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x09, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x09, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x06, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x06, value=0x0000),
        UsbHidDataFragment.being_data(audio_feature=0x09, value=0x0000),
        UsbHidDataFragment.being_commit(audio_feature=0x09, value=0x0000),
    ]


def speakers_to_stereo() -> list[UsbAudioData]:
    """
    Set speakers to stereo output.
    :return: The list of UsbAudioData objects to send to the G6, to set speakers to stereo output.
    """
    return [UsbAudioData(b_request=PLAYBACK_B_REQUEST, w_value=CHANNEL_1, w_index=0x0001, w_length=0x0002,
                         data_fragment=0x00f4)]


def speakers_to_5_1() -> list[UsbAudioData]:
    """
    Set speakers to 5.1 output.
    Note: Actually SoundBlasterCommand sends the same packets to the G6, regardless of the selected output mode.
    Maybe this the output is achieved by a system call from SoundBlasterCommand to the OS?
    :return: The list of UsbAudioData objects to send to the G6, to set speakers to 5.1 output.
    """
    return speakers_to_stereo()


def speakers_to_7_1() -> list[UsbAudioData]:
    """
    Set speakers to 5.1 output.
    Note: Actually SoundBlasterCommand sends the same packets to the G6, regardless of the selected output mode.
    Maybe this the output is achieved by a system call from SoundBlasterCommand to the OS?
    :return: The list of UsbAudioData objects to send to the G6, to set speakers to 5.1 output.
    """
    return speakers_to_stereo()


def headphones_to_stereo() -> list[UsbAudioData]:
    """
    Set headphones to stereo output.
    :return: The list of UsbAudioData objects to send to the G6, to set headphones to stereo output.
    """
    return [
        UsbAudioData(b_request=PLAYBACK_B_REQUEST, w_value=CHANNEL_1, w_index=0x0001, w_length=0x0002,
                     data_fragment=0x00f4),
        UsbAudioData(b_request=PLAYBACK_B_REQUEST, w_value=CHANNEL_2, w_index=0x0001, w_length=0x0002,
                     data_fragment=0x00f4)
    ]


def headphones_to_5_1() -> list[UsbAudioData]:
    """
    Set headphones to 5.1 output.
    Note: Actually SoundBlasterCommand sends the same packets to the G6, regardless of the selected output mode.
    Maybe this the output is achieved by a system call from SoundBlasterCommand to the OS?
    :return: The list of UsbAudioData objects to send to the G6, to set headphones to 5.1 output.
    """
    return headphones_to_stereo()


def headphones_to_7_1() -> list[UsbAudioData]:
    """
    Set headphones to 7.1 output.
    Note: Actually SoundBlasterCommand sends the same packets to the G6, regardless of the selected output mode.
    Maybe this the output is achieved by a system call from SoundBlasterCommand to the OS?
    :return: The list of UsbAudioData objects to send to the G6, to set headphones to 7.1 output.
    """
    return headphones_to_stereo()


def playback_volume(volume_percent: int) -> list[UsbAudioData]:
    """
    Set playback volume to the specified percentage.
    :param volume_percent: The volume percentage to set (10, 20, 30, ..., 100).
    :return: The list of UsbAudioData objects to send to the G6, to set playback volume.
    """
    if volume_percent < 0 or volume_percent > 100:
        raise ValueError(f"Volume percentage must be between 0 and 100, got {volume_percent}")
    if volume_percent % 10 != 0:
        raise ValueError(f"Volume percentage must be a multiple of 10, got {volume_percent}")
    volume_percent_hex = get_playback_volume_percent_hex(volume_percent)
    return [
        UsbAudioData(b_request=PLAYBACK_B_REQUEST, w_value=CHANNEL_1, w_index=0x0001, w_length=0x0002,
                     data_fragment=volume_percent_hex),
        UsbAudioData(b_request=PLAYBACK_B_REQUEST, w_value=CHANNEL_2, w_index=0x0001, w_length=0x0002,
                     data_fragment=volume_percent_hex)
    ]


def enable_direct_mode(enable: bool) -> list[UsbHidDataFragment]:
    """
    Enable or disable direct mode.
    :param enable: True to enable direct mode, False to disable.
    :return: The list of UsbHidDataFragment objects to send to the G6, to enable or disable direct mode.
    """
    return [
        UsbHidDataFragment.empty_additional_payload(mode=0x3903, intermediate=DIRECT_MODE,
                                                    audio_feature=0x01 if enable else 0x00, value=0x00),
        UsbHidDataFragment.empty_additional_payload(mode=0x3901, intermediate=0x0100, audio_feature=0x00, value=0x00)
    ]


def enable_spdif_out_direct_mode(enable: bool) -> list[UsbHidDataFragment]:
    """
    Enable or disable SPDIF-Out direct mode.
    :param enable: True to enable direct mode, False to disable.
    :return: The list of UsbHidDataFragment objects to send to the G6, to enable or disable SPDIF-Out direct mode.
    """
    return [
        UsbHidDataFragment.empty_additional_payload(mode=0x3903, intermediate=SPDIF_OUT_DIRECT_MODE,
                                                    audio_feature=0x01 if enable else 0x00,
                                                    value=0x00),
        UsbHidDataFragment.empty_additional_payload(mode=0x3901, intermediate=0x0100, audio_feature=0x00, value=0x00)
    ]


def playback_filter(playback_filter_enum: PlaybackFilter) -> list[UsbHidDataFragment]:
    """
    Set the playback filter.
    :param playback_filter_enum: The playback filter value to set.
    :return: The list of UsbHidDataFragment objects to send to the G6, to set the playback filter.
    """
    return [
        UsbHidDataFragment.empty_additional_payload(mode=0x6c03, intermediate=playback_filter_enum.value, audio_feature=0x00,
                                                    value=0x00),
        UsbHidDataFragment.empty_additional_payload(mode=0x6c01, intermediate=0x0100, audio_feature=0x00, value=0x00)
    ]
