# tests/test_g6_api_init.py
from __future__ import annotations

from unittest.mock import MagicMock

import pytest

import g6_cli.g6_api as g6_api
from g6_cli.g6_core import G6Device


@pytest.fixture()
def api(monkeypatch: pytest.MonkeyPatch) -> g6_api.G6Api:
    """
    Always construct with dry_run=True (per requirement) and never touch real hardware.
    """
    monkeypatch.setattr(g6_api, "detect_device",
                        MagicMock(return_value=G6Device(device_path_audio_interface="/dev/fake-g6/audio",
                                                        device_path_hid_interface="/dev/fake-g6/hid")))
    monkeypatch.setattr(g6_api, "send_audio_data_to_device", MagicMock())
    monkeypatch.setattr(g6_api, "send_hid_data_to_device", MagicMock())
    return g6_api.G6Api(dry_run=True)


AUDIO_CASES = [
    # --- Playback (audio) ---
    ("playback_mute", "playback_mute_spec", (True,), {}),
    ("playback_mute", "playback_mute_spec", (False,), {}),
    ("playback_speakers_to_stereo", "speakers_to_stereo_spec", (), {}),
    ("playback_speakers_to_5_1", "speakers_to_5_1_spec", (), {}),
    ("playback_speakers_to_7_1", "speakers_to_7_1_spec", (), {}),
    ("playback_headphones_to_stereo", "headphones_to_stereo_spec", (), {}),
    ("playback_headphones_to_5_1", "headphones_to_5_1_spec", (), {}),
    ("playback_headphones_to_7_1", "headphones_to_7_1_spec", (), {}),
    ("playback_volume", "playback_volume_spec", (0,), {}),
    ("playback_volume", "playback_volume_spec", (50,), {}),
    ("playback_volume", "playback_volume_spec", (100,), {}),
    # --- Mixer (audio) ---
    ("mixer_playback_mute", "mixer_playback_mute_spec", (True,), {}),
    ("mixer_playback_mute", "mixer_playback_mute_spec", (False,), {}),
    ("mixer_monitoring_line_in_mute", "monitoring_line_in_mute_spec", (True,), {}),
    ("mixer_monitoring_line_in_mute", "monitoring_line_in_mute_spec", (False,), {}),
    ("mixer_monitoring_line_in_volume", "monitoring_line_in_volume_spec", (0,), {}),
    ("mixer_monitoring_line_in_volume", "monitoring_line_in_volume_spec", (37,), {}),
    ("mixer_monitoring_line_in_volume", "monitoring_line_in_volume_spec", (100,), {}),
    ("mixer_monitoring_external_mic_mute", "monitoring_external_mic_mute_spec", (True,), {}),
    ("mixer_monitoring_external_mic_mute", "monitoring_external_mic_mute_spec", (False,), {}),
    ("mixer_monitoring_external_mic_volume", "monitoring_external_mic_volume_spec", (0,), {}),
    ("mixer_monitoring_external_mic_volume", "monitoring_external_mic_volume_spec", (12,), {}),
    ("mixer_monitoring_external_mic_volume", "monitoring_external_mic_volume_spec", (100,), {}),
    ("mixer_monitoring_spdif_in_mute", "monitoring_spdif_in_mute_spec", (True,), {}),
    ("mixer_monitoring_spdif_in_mute", "monitoring_spdif_in_mute_spec", (False,), {}),
    ("mixer_monitoring_spdif_in_volume", "monitoring_spdif_in_volume_spec", (0,), {}),
    ("mixer_monitoring_spdif_in_volume", "monitoring_spdif_in_volume_spec", (88,), {}),
    ("mixer_monitoring_spdif_in_volume", "monitoring_spdif_in_volume_spec", (100,), {}),
    ("mixer_recording_line_in_mute", "recording_line_in_mute_spec", (True,), {}),
    ("mixer_recording_line_in_mute", "recording_line_in_mute_spec", (False,), {}),
    ("mixer_recording_line_in_volume", "recording_line_in_volume_spec", (0,), {}),
    ("mixer_recording_line_in_volume", "recording_line_in_volume_spec", (61,), {}),
    ("mixer_recording_line_in_volume", "recording_line_in_volume_spec", (100,), {}),
    ("mixer_recording_external_mic_mute", "recording_external_mic_mute_spec", (True,), {}),
    ("mixer_recording_external_mic_mute", "recording_external_mic_mute_spec", (False,), {}),
    ("mixer_recording_external_mic_volume", "recording_external_mic_volume_spec", (0,), {}),
    ("mixer_recording_external_mic_volume", "recording_external_mic_volume_spec", (73,), {}),
    ("mixer_recording_external_mic_volume", "recording_external_mic_volume_spec", (100,), {}),
    ("mixer_recording_spdif_in_mute", "recording_spdif_in_mute_spec", (True,), {}),
    ("mixer_recording_spdif_in_mute", "recording_spdif_in_mute_spec", (False,), {}),
    ("mixer_recording_spdif_in_volume", "recording_spdif_in_volume_spec", (0,), {}),
    ("mixer_recording_spdif_in_volume", "recording_spdif_in_volume_spec", (9,), {}),
    ("mixer_recording_spdif_in_volume", "recording_spdif_in_volume_spec", (100,), {}),
    ("mixer_recording_what_u_hear_mute", "recording_what_u_hear_mute_spec", (True,), {}),
    ("mixer_recording_what_u_hear_mute", "recording_what_u_hear_mute_spec", (False,), {}),
    ("mixer_recording_what_u_hear_volume", "recording_what_u_hear_volume_spec", (0,), {}),
    ("mixer_recording_what_u_hear_volume", "recording_what_u_hear_volume_spec", (44,), {}),
    ("mixer_recording_what_u_hear_volume", "recording_what_u_hear_volume_spec", (100,), {}),
    # --- Recording (audio) ---
    ("recording_mute", "recording_mute_spec", (True,), {}),
    ("recording_mute", "recording_mute_spec", (False,), {}),
    ("recording_mic_recording_volume", "mic_recording_volume_spec", (0,), {}),
    ("recording_mic_recording_volume", "mic_recording_volume_spec", (29,), {}),
    ("recording_mic_recording_volume", "mic_recording_volume_spec", (100,), {}),
    ("recording_mic_monitoring", "mic_monitoring_spec", (0,), {}),
    ("recording_mic_monitoring", "mic_monitoring_spec", (65,), {}),
    ("recording_mic_monitoring", "mic_monitoring_spec", (100,), {}),
]

HID_CASES = [
    # --- Playback (hid) ---
    ("playback_toggle_to_speakers", "toggle_to_speakers_spec", (), {}),
    ("playback_toggle_to_headphones", "toggle_to_headphones_spec", (), {}),
    ("playback_enable_direct_mode", "enable_direct_mode_spec", (True,), {}),
    ("playback_enable_direct_mode", "enable_direct_mode_spec", (False,), {}),
    ("playback_enable_spdif_out_direct_mode", "enable_spdif_out_direct_mode_spec", (True,), {}),
    ("playback_enable_spdif_out_direct_mode", "enable_spdif_out_direct_mode_spec", (False,), {}),
    ("playback_filter", "playback_filter_spec", (object(),), {}),
    # --- Decoder (hid) ---
    ("decoder_mode", "decoder_mode_spec", (object(),), {}),
    # --- Lighting (hid) ---
    ("lighting_disable", "lighting_disable_spec", (), {}),
    ("lighting_enable_set_rgb", "lighting_enable_set_rgb_spec", (), {"red": 0, "green": 0, "blue": 0}),
    ("lighting_enable_set_rgb", "lighting_enable_set_rgb_spec", (), {"red": 12, "green": 34, "blue": 56}),
    ("lighting_enable_set_rgb", "lighting_enable_set_rgb_spec", (), {"red": 255, "green": 255, "blue": 255}),
    # --- Recording (hid) ---
    ("recording_mic_boost", "mic_boost_spec", (0,), {}),
    ("recording_mic_boost", "mic_boost_spec", (10,), {}),
    ("recording_voice_clarity_enabled", "voice_clarity_enabled_spec", (True,), {}),
    ("recording_voice_clarity_enabled", "voice_clarity_enabled_spec", (False,), {}),
    ("recording_voice_clarity_level", "voice_clarity_level_spec", (0,), {}),
    ("recording_voice_clarity_level", "voice_clarity_level_spec", (33,), {}),
    ("recording_voice_clarity_level", "voice_clarity_level_spec", (100,), {}),
    ("recording_acoustic_echo_cancellation_enabled", "acoustic_echo_cancellation_enabled_spec", (True,), {}),
    ("recording_acoustic_echo_cancellation_enabled", "acoustic_echo_cancellation_enabled_spec", (False,), {}),
    ("recording_smart_volume_enabled", "smart_volume_enabled_spec", (True,), {}),
    ("recording_smart_volume_enabled", "smart_volume_enabled_spec", (False,), {}),
    ("recording_mic_equalizer_enabled", "mic_equalizer_enabled_spec", (True,), {}),
    ("recording_mic_equalizer_enabled", "mic_equalizer_enabled_spec", (False,), {}),
    ("recording_mic_equalizer_preset", "mic_equalizer_preset_spec", (object(),), {}),
    # --- SBX (hid) ---
    (
        "sbx_toggle",
        "sbx_toggle_spec",
        (),
        {"audio_feature": object(), "activate": True},
    ),
    (
        "sbx_toggle",
        "sbx_toggle_spec",
        (),
        {"audio_feature": object(), "activate": False},
    ),
    (
        "sbx_slider",
        "sbx_slider_spec",
        (),
        {"audio_feature": object(), "value": 0},
    ),
    (
        "sbx_slider",
        "sbx_slider_spec",
        (),
        {"audio_feature": object(), "value": 42},
    ),
    (
        "sbx_slider",
        "sbx_slider_spec",
        (),
        {"audio_feature": object(), "value": 100},
    ),
    (
        "sbx_smart_volume_special",
        "sbx_smart_volume_special_spec",
        (),
        {"smart_volume_special_hex": object()},
    ),
]


@pytest.mark.parametrize("method_name,spec_name,args,kwargs", AUDIO_CASES)
def test_g6api_audio_methods_call_audio_sender(
        api: g6_api.G6Api,
        monkeypatch: pytest.MonkeyPatch,
        method_name: str,
        spec_name: str,
        args: tuple,
        kwargs: dict,
) -> None:
    # Arrange
    expected_audio_data_list = [b"audio-payload"]
    spec_mock = MagicMock(return_value=expected_audio_data_list)
    monkeypatch.setattr(g6_api, spec_name, spec_mock)

    # noinspection PyTypeChecker
    send_audio_mock: MagicMock = g6_api.send_audio_data_to_device  # patched in fixture
    send_audio_mock.reset_mock()  # reset function call counters

    # Act
    method = getattr(api, method_name)
    method(*args, **kwargs)

    # Assert: spec called correctly
    spec_mock.assert_called_once_with(*args, **kwargs)

    # Assert: sender called correctly (and with dry_run=True)
    send_audio_mock.assert_called_once()
    call_kwargs = send_audio_mock.call_args.kwargs
    assert type(call_kwargs["device"]) is G6Device
    assert call_kwargs["device"].get_device_path_audio_interface() == "/dev/fake-g6/audio"
    assert call_kwargs["device"].get_device_path_hid_interface() == "/dev/fake-g6/hid"
    assert call_kwargs["audio_data_list"] == expected_audio_data_list
    assert call_kwargs["dry_run"] is True


@pytest.mark.parametrize("method_name,spec_name,args,kwargs", HID_CASES)
def test_g6api_hid_methods_call_hid_sender(
        api: g6_api.G6Api,
        monkeypatch: pytest.MonkeyPatch,
        method_name: str,
        spec_name: str,
        args: tuple,
        kwargs: dict,
) -> None:
    # Arrange
    expected_hid_data_list = [b"hid-payload"]
    spec_mock = MagicMock(return_value=expected_hid_data_list)
    monkeypatch.setattr(g6_api, spec_name, spec_mock)

    # noinspection PyTypeChecker
    send_hid_mock: MagicMock = g6_api.send_hid_data_to_device  # patched in fixture
    send_hid_mock.reset_mock()  # reset function call counters

    # Act
    method = getattr(api, method_name)
    method(*args, **kwargs)

    # Assert: spec called correctly
    spec_mock.assert_called_once_with(*args, **kwargs)

    # Assert: sender called correctly (and with dry_run=True)
    send_hid_mock.assert_called_once()
    call_kwargs = send_hid_mock.call_args.kwargs
    assert type(call_kwargs["device"]) is G6Device
    assert call_kwargs["device"].get_device_path_audio_interface() == "/dev/fake-g6/audio"
    assert call_kwargs["device"].get_device_path_hid_interface() == "/dev/fake-g6/hid"
    assert call_kwargs["hid_data_list"] == expected_hid_data_list
    assert call_kwargs["dry_run"] is True


def test_constructor_detects_device_once(monkeypatch: pytest.MonkeyPatch) -> None:
    detect_mock = MagicMock(return_value="/dev/fake-g6")
    monkeypatch.setattr(g6_api, "detect_device", detect_mock)
    monkeypatch.setattr(g6_api, "send_audio_data_to_device", MagicMock())
    monkeypatch.setattr(g6_api, "send_hid_data_to_device", MagicMock())

    _ = g6_api.G6Api(dry_run=True)

    detect_mock.assert_called_once_with()
