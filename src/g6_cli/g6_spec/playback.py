from g6_cli.g6_spec import UsbAudioData, UsbHidDataFragment, get_playback_volume_percent_bytes, PlaybackFilter

PLAYBACK_B_REQUEST = bytes.fromhex('01')
CHANNEL_1 = bytes.fromhex('0201')
CHANNEL_2 = bytes.fromhex('0202')
DIRECT_MODE = bytes.fromhex('0005')
SPDIF_OUT_DIRECT_MODE = bytes.fromhex('000d')


def playback_mute(mute: bool) -> list[UsbAudioData]:
    """
    Mute or activate the playback.
    :param: mute: True to mute, False to activate
    :return: The list of UsbAudioData objects to send to the G6, to mute or unmute playback.
    """
    return [UsbAudioData(b_request=PLAYBACK_B_REQUEST, w_value=bytes.fromhex('0001'), w_index=bytes.fromhex('0001'),
                         w_length=bytes.fromhex('0100'),
                         data_fragment=bytes.fromhex('01' if mute else '00'))]


def toggle_to_speakers() -> list[UsbHidDataFragment]:
    """
    Toggle the playback to speakers.
    :return: The list of UsbHidDataFragment objects to send to the G6, to toggle playback to speakers.
    """
    return [
        UsbHidDataFragment.empty_additional_payload(mode=bytes.fromhex('2c05'), intermediate=bytes.fromhex('0002'),
                                                    audio_feature=bytes.fromhex('00'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.empty_additional_payload(mode=bytes.fromhex('2c01'), intermediate=bytes.fromhex('0100'),
                                                    audio_feature=bytes.fromhex('00'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('0A'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('0A'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('0B'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('0B'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('0C'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('0C'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('0D'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('0D'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('0E'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('0E'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('0F'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('0F'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('10'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('10'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('11'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('11'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('12'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('12'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('13'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('13'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('14'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('14'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('09'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('09'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('09'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('09'), value=bytes.fromhex('0000 0000')),
    ]


def toggle_to_headphones() -> list[UsbHidDataFragment]:
    """
    Toggle the playback to headphones.
    :return: The list of UsbHidDataFragment objects to send to the G6, to toggle playback to headphones.
    """
    return [
        UsbHidDataFragment.empty_additional_payload(mode=bytes.fromhex('2c05'), intermediate=bytes.fromhex('0004'),
                                                    audio_feature=bytes.fromhex('00'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.empty_additional_payload(mode=bytes.fromhex('2c01'), intermediate=bytes.fromhex('0100'),
                                                    audio_feature=bytes.fromhex('00'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('0A'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('0A'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('0B'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('0B'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('0C'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('0C'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('0D'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('0D'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('0E'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('0E'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('0F'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('0F'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('10'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('10'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('11'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('11'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('12'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('12'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('13'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('13'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('14'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('14'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('09'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('09'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('06'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('06'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_data(audio_feature=bytes.fromhex('09'), value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.being_commit(audio_feature=bytes.fromhex('09'), value=bytes.fromhex('0000 0000')),
    ]


def speakers_to_stereo() -> list[UsbAudioData]:
    """
    Set speakers to stereo output.
    :return: The list of UsbAudioData objects to send to the G6, to set speakers to stereo output.
    """
    return [UsbAudioData(b_request=PLAYBACK_B_REQUEST, w_value=CHANNEL_1, w_index=bytes.fromhex('0001'),
                         w_length=bytes.fromhex('0200'),
                         data_fragment=bytes.fromhex('00f4'))]


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
        UsbAudioData(b_request=PLAYBACK_B_REQUEST, w_value=CHANNEL_1, w_index=bytes.fromhex('0001'),
                     w_length=bytes.fromhex('0200'),
                     data_fragment=bytes.fromhex('00f4')),
        UsbAudioData(b_request=PLAYBACK_B_REQUEST, w_value=CHANNEL_2, w_index=bytes.fromhex('0001'),
                     w_length=bytes.fromhex('0200'),
                     data_fragment=bytes.fromhex('00f4'))
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
    volume_percent_bytes = get_playback_volume_percent_bytes(volume_percent)
    return [
        UsbAudioData(b_request=PLAYBACK_B_REQUEST, w_value=CHANNEL_1, w_index=bytes.fromhex('0001'),
                     w_length=bytes.fromhex('0200'),
                     data_fragment=volume_percent_bytes),
        UsbAudioData(b_request=PLAYBACK_B_REQUEST, w_value=CHANNEL_2, w_index=bytes.fromhex('0001'),
                     w_length=bytes.fromhex('0200'),
                     data_fragment=volume_percent_bytes)
    ]


def enable_direct_mode(enable: bool) -> list[UsbHidDataFragment]:
    """
    Enable or disable direct mode.
    :param enable: True to enable direct mode, False to disable.
    :return: The list of UsbHidDataFragment objects to send to the G6, to enable or disable direct mode.
    """
    return [
        UsbHidDataFragment.empty_additional_payload(mode=bytes.fromhex('3903'), intermediate=DIRECT_MODE,
                                                    audio_feature=bytes.fromhex('01' if enable else '00'),
                                                    value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.empty_additional_payload(mode=bytes.fromhex('3901'), intermediate=bytes.fromhex('0100'),
                                                    audio_feature=bytes.fromhex('00'), value=bytes.fromhex('0000 0000'))
    ]


def enable_spdif_out_direct_mode(enable: bool) -> list[UsbHidDataFragment]:
    """
    Enable or disable SPDIF-Out direct mode.
    :param enable: True to enable direct mode, False to disable.
    :return: The list of UsbHidDataFragment objects to send to the G6, to enable or disable SPDIF-Out direct mode.
    """
    return [
        UsbHidDataFragment.empty_additional_payload(mode=bytes.fromhex('3903'), intermediate=SPDIF_OUT_DIRECT_MODE,
                                                    audio_feature=bytes.fromhex('01' if enable else '00'),
                                                    value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.empty_additional_payload(mode=bytes.fromhex('3901'), intermediate=bytes.fromhex('0100'),
                                                    audio_feature=bytes.fromhex('00'), value=bytes.fromhex('0000 0000'))
    ]


def playback_filter(playback_filter_enum: PlaybackFilter) -> list[UsbHidDataFragment]:
    """
    Set the playback filter.
    :param playback_filter_enum: The playback filter value to set.
    :return: The list of UsbHidDataFragment objects to send to the G6, to set the playback filter.
    """
    return [
        UsbHidDataFragment.empty_additional_payload(mode=bytes.fromhex('6c03'), intermediate=playback_filter_enum.value,
                                                    audio_feature=bytes.fromhex('00'),
                                                    value=bytes.fromhex('0000 0000')),
        UsbHidDataFragment.empty_additional_payload(mode=bytes.fromhex('6c01'), intermediate=bytes.fromhex('0100'),
                                                    audio_feature=bytes.fromhex('00'), value=bytes.fromhex('0000 0000'))
    ]
