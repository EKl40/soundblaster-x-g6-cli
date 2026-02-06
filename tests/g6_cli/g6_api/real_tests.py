from __future__ import annotations

from collections.abc import Callable

import pytest

import g6_cli.g6_api as g6_api
from g6_cli.g6_core import G6Device
from g6_cli.g6_spec import AudioFeature, PlaybackFilter, SmartVolumeSpecialHex
from g6_cli.g6_spec.decoder import DecoderMode
from g6_cli.g6_spec.recording import MicrophoneEqualizerPreset


def _first_enum_member(enum_cls):
    return next(iter(enum_cls))


@pytest.fixture()
def api(monkeypatch: pytest.MonkeyPatch) -> g6_api.G6Api:
    return g6_api.G6Api(dry_run=True)


# Each case: (method_name, args_factory)
# args_factory returns (args_tuple, kwargs_dict)
ArgFactory = Callable[[], tuple[tuple, dict]]

CASES: list[tuple[str, ArgFactory]] = [
    # --- Playback ---
    ("playback_mute", lambda: ((True,), {})),
    ("playback_mute", lambda: ((False,), {})),
    ("playback_toggle_to_speakers", lambda: ((), {})),
    ("playback_toggle_to_headphones", lambda: ((), {})),
    ("playback_speakers_to_stereo", lambda: ((), {})),
    ("playback_speakers_to_5_1", lambda: ((), {})),
    ("playback_speakers_to_7_1", lambda: ((), {})),
    ("playback_headphones_to_stereo", lambda: ((), {})),
    ("playback_headphones_to_5_1", lambda: ((), {})),
    ("playback_headphones_to_7_1", lambda: ((), {})),
    ("playback_volume", lambda: ((0,), {})),
    ("playback_volume", lambda: ((50,), {})),
    ("playback_volume", lambda: ((100,), {})),
    ("playback_enable_direct_mode", lambda: ((True,), {})),
    ("playback_enable_direct_mode", lambda: ((False,), {})),
    ("playback_enable_spdif_out_direct_mode", lambda: ((True,), {})),
    ("playback_enable_spdif_out_direct_mode", lambda: ((False,), {})),
    ("playback_filter", lambda: ((_first_enum_member(PlaybackFilter),), {})),
    # --- Decoder ---
    ("decoder_mode", lambda: ((_first_enum_member(DecoderMode),), {})),
    # --- Lighting ---
    ("lighting_disable", lambda: ((), {})),
    ("lighting_enable_set_rgb", lambda: ((), {"red": 0, "green": 0, "blue": 0})),
    ("lighting_enable_set_rgb", lambda: ((), {"red": 12, "green": 34, "blue": 56})),
    ("lighting_enable_set_rgb", lambda: ((), {"red": 255, "green": 255, "blue": 255})),
    # --- Mixer ---
    ("mixer_playback_mute", lambda: ((True,), {})),
    ("mixer_playback_mute", lambda: ((False,), {})),
    ("mixer_monitoring_line_in_mute", lambda: ((True,), {})),
    ("mixer_monitoring_line_in_mute", lambda: ((False,), {})),
    ("mixer_monitoring_line_in_volume", lambda: ((0,), {})),
    ("mixer_monitoring_line_in_volume", lambda: ((37,), {})),
    ("mixer_monitoring_line_in_volume", lambda: ((100,), {})),
    ("mixer_monitoring_external_mic_mute", lambda: ((True,), {})),
    ("mixer_monitoring_external_mic_mute", lambda: ((False,), {})),
    ("mixer_monitoring_external_mic_volume", lambda: ((0,), {})),
    ("mixer_monitoring_external_mic_volume", lambda: ((12,), {})),
    ("mixer_monitoring_external_mic_volume", lambda: ((100,), {})),
    ("mixer_monitoring_spdif_in_mute", lambda: ((True,), {})),
    ("mixer_monitoring_spdif_in_mute", lambda: ((False,), {})),
    ("mixer_monitoring_spdif_in_volume", lambda: ((0,), {})),
    ("mixer_monitoring_spdif_in_volume", lambda: ((88,), {})),
    ("mixer_monitoring_spdif_in_volume", lambda: ((100,), {})),
    ("mixer_recording_line_in_mute", lambda: ((True,), {})),
    ("mixer_recording_line_in_mute", lambda: ((False,), {})),
    ("mixer_recording_line_in_volume", lambda: ((0,), {})),
    ("mixer_recording_line_in_volume", lambda: ((61,), {})),
    ("mixer_recording_line_in_volume", lambda: ((100,), {})),
    ("mixer_recording_external_mic_mute", lambda: ((True,), {})),
    ("mixer_recording_external_mic_mute", lambda: ((False,), {})),
    ("mixer_recording_external_mic_volume", lambda: ((0,), {})),
    ("mixer_recording_external_mic_volume", lambda: ((73,), {})),
    ("mixer_recording_external_mic_volume", lambda: ((100,), {})),
    ("mixer_recording_spdif_in_mute", lambda: ((True,), {})),
    ("mixer_recording_spdif_in_mute", lambda: ((False,), {})),
    ("mixer_recording_spdif_in_volume", lambda: ((0,), {})),
    ("mixer_recording_spdif_in_volume", lambda: ((9,), {})),
    ("mixer_recording_spdif_in_volume", lambda: ((100,), {})),
    ("mixer_recording_what_u_hear_mute", lambda: ((True,), {})),
    ("mixer_recording_what_u_hear_mute", lambda: ((False,), {})),
    ("mixer_recording_what_u_hear_volume", lambda: ((0,), {})),
    ("mixer_recording_what_u_hear_volume", lambda: ((44,), {})),
    ("mixer_recording_what_u_hear_volume", lambda: ((100,), {})),
    # --- Recording ---
    ("recording_mute", lambda: ((True,), {})),
    ("recording_mute", lambda: ((False,), {})),
    ("recording_mic_recording_volume", lambda: ((0,), {})),
    ("recording_mic_recording_volume", lambda: ((29,), {})),
    ("recording_mic_recording_volume", lambda: ((100,), {})),
    ("recording_mic_boost", lambda: ((0,), {})),
    ("recording_mic_monitoring", lambda: ((0,), {})),
    ("recording_mic_monitoring", lambda: ((65,), {})),
    ("recording_mic_monitoring", lambda: ((100,), {})),
    ("recording_voice_clarity_enabled", lambda: ((True,), {})),
    ("recording_voice_clarity_enabled", lambda: ((False,), {})),
    ("recording_voice_clarity_level", lambda: ((0,), {})),
    ("recording_voice_clarity_level", lambda: ((33,), {})),
    ("recording_voice_clarity_level", lambda: ((100,), {})),
    ("recording_acoustic_echo_cancellation_enabled", lambda: ((True,), {})),
    ("recording_acoustic_echo_cancellation_enabled", lambda: ((False,), {})),
    ("recording_smart_volume_enabled", lambda: ((True,), {})),
    ("recording_smart_volume_enabled", lambda: ((False,), {})),
    ("recording_mic_equalizer_enabled", lambda: ((True,), {})),
    ("recording_mic_equalizer_enabled", lambda: ((False,), {})),
    ("recording_mic_equalizer_preset", lambda: ((_first_enum_member(MicrophoneEqualizerPreset),), {})),
    # --- SBX ---
    ("sbx_toggle", lambda: ((), {"audio_feature": _first_enum_member(AudioFeature), "activate": True})),
    ("sbx_toggle", lambda: ((), {"audio_feature": _first_enum_member(AudioFeature), "activate": False})),
    ("sbx_slider", lambda: ((), {"audio_feature": _first_enum_member(AudioFeature), "value": 0})),
    ("sbx_slider", lambda: ((), {"audio_feature": _first_enum_member(AudioFeature), "value": 42})),
    ("sbx_slider", lambda: ((), {"audio_feature": _first_enum_member(AudioFeature), "value": 100})),
    ("sbx_smart_volume_special", lambda: ((), {"smart_volume_special_hex": _first_enum_member(SmartVolumeSpecialHex)})),
]


@pytest.mark.parametrize("method_name,args_factory", CASES)
def test_g6api_methods_execute_in_dry_run_without_errors(
        api: g6_api.G6Api,
        method_name: str,
        args_factory: ArgFactory,
) -> None:
    """
    Integration-style unit test:
    - uses the real *_spec functions
    - uses the real send_* functions
    - relies on dry_run=True to avoid hardware I/O
    """
    method = getattr(api, method_name)
    args, kwargs = args_factory()

    result = method(*args, **kwargs)

    assert result is None


def test_constructor_uses_detect_device(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []

    def _fake_detect_device() -> G6Device:
        calls.append("called")
        return G6Device(device_path_audio_interface="/dev/fake-g6/audio", device_path_hid_interface="/dev/fake-g6/hid")

    monkeypatch.setattr(g6_api, "detect_device", _fake_detect_device)

    _ = g6_api.G6Api(dry_run=True)

    assert calls == ["called"]
