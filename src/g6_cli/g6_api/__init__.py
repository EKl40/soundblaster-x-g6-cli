from g6_cli.g6_core import (
    detect_device,
    send_audio_data_to_device,
    send_hid_data_to_device,
)
from g6_cli.g6_spec import AudioFeature, PlaybackFilter, SmartVolumeSpecialHex
from g6_cli.g6_spec.decoder import DecoderMode
from g6_cli.g6_spec.decoder import decoder_mode as decoder_mode_spec
from g6_cli.g6_spec.lighting import (
    lighting_disable as lighting_disable_spec,
    lighting_enable_set_rgb as lighting_enable_set_rgb_spec,
)
from g6_cli.g6_spec.mixer import (
    monitoring_external_mic_mute as monitoring_external_mic_mute_spec,
    monitoring_external_mic_volume as monitoring_external_mic_volume_spec,
    monitoring_line_in_mute as monitoring_line_in_mute_spec,
    monitoring_line_in_volume as monitoring_line_in_volume_spec,
    monitoring_spdif_in_mute as monitoring_spdif_in_mute_spec,
    monitoring_spdif_in_volume as monitoring_spdif_in_volume_spec,
    playback_mute as mixer_playback_mute_spec,
    recording_external_mic_mute as recording_external_mic_mute_spec,
    recording_external_mic_volume as recording_external_mic_volume_spec,
    recording_line_in_mute as recording_line_in_mute_spec,
    recording_line_in_volume as recording_line_in_volume_spec,
    recording_spdif_in_mute as recording_spdif_in_mute_spec,
    recording_spdif_in_volume as recording_spdif_in_volume_spec,
    recording_what_u_hear_mute as recording_what_u_hear_mute_spec,
    recording_what_u_hear_volume as recording_what_u_hear_volume_spec,
)
from g6_cli.g6_spec.playback import (
    enable_direct_mode as enable_direct_mode_spec,
    enable_spdif_out_direct_mode as enable_spdif_out_direct_mode_spec,
    headphones_to_5_1 as headphones_to_5_1_spec,
    headphones_to_7_1 as headphones_to_7_1_spec,
    headphones_to_stereo as headphones_to_stereo_spec,
    playback_filter as playback_filter_spec,
    playback_mute as playback_mute_spec,
    playback_volume as playback_volume_spec,
    speakers_to_5_1 as speakers_to_5_1_spec,
    speakers_to_7_1 as speakers_to_7_1_spec,
    speakers_to_stereo as speakers_to_stereo_spec,
    toggle_to_headphones as toggle_to_headphones_spec,
    toggle_to_speakers as toggle_to_speakers_spec,
)
from g6_cli.g6_spec.recording import MicrophoneEqualizerPreset
from g6_cli.g6_spec.recording import (
    acoustic_echo_cancellation_enabled as acoustic_echo_cancellation_enabled_spec,
    mic_boost as mic_boost_spec,
    mic_equalizer_enabled as mic_equalizer_enabled_spec,
    mic_equalizer_preset as mic_equalizer_preset_spec,
    mic_monitoring as mic_monitoring_spec,
    mic_recording_volume as mic_recording_volume_spec,
    recording_mute as recording_mute_spec,
    smart_volume_enabled as smart_volume_enabled_spec,
    voice_clarity_enabled as voice_clarity_enabled_spec,
    voice_clarity_level as voice_clarity_level_spec,
)
from g6_cli.g6_spec.sbx import (
    sbx_slider as sbx_slider_spec,
    sbx_smart_volume_special as sbx_smart_volume_special_spec,
    sbx_toggle as sbx_toggle_spec,
)


class G6Api:
    def __init__(self, dry_run: bool):
        self.__dry_run = dry_run
        self.__device = detect_device()

    # --- Playback ---

    def playback_mute(self, mute: bool) -> None:
        audio_data_list = playback_mute_spec(mute)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def playback_toggle_to_speakers(self) -> None:
        hid_data_list = toggle_to_speakers_spec()
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    def playback_toggle_to_headphones(self) -> None:
        hid_data_list = toggle_to_headphones_spec()
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    def playback_speakers_to_stereo(self) -> None:
        audio_data_list = speakers_to_stereo_spec()
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def playback_speakers_to_5_1(self) -> None:
        audio_data_list = speakers_to_5_1_spec()
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def playback_speakers_to_7_1(self) -> None:
        audio_data_list = speakers_to_7_1_spec()
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def playback_headphones_to_stereo(self) -> None:
        audio_data_list = headphones_to_stereo_spec()
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def playback_headphones_to_5_1(self) -> None:
        audio_data_list = headphones_to_5_1_spec()
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def playback_headphones_to_7_1(self) -> None:
        audio_data_list = headphones_to_7_1_spec()
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def playback_volume(self, volume_percent: int) -> None:
        audio_data_list = playback_volume_spec(volume_percent)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def playback_enable_direct_mode(self, enable: bool) -> None:
        hid_data_list = enable_direct_mode_spec(enable)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    def playback_enable_spdif_out_direct_mode(self, enable: bool) -> None:
        hid_data_list = enable_spdif_out_direct_mode_spec(enable)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    def playback_filter(self, playback_filter_enum: PlaybackFilter) -> None:
        hid_data_list = playback_filter_spec(playback_filter_enum)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    # --- Decoder ---

    def decoder_mode(self, decoder_mode_enum: DecoderMode) -> None:
        hid_data_list = decoder_mode_spec(decoder_mode_enum)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    # --- Lighting ---

    def lighting_disable(self) -> None:
        hid_data_list = lighting_disable_spec()
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    def lighting_enable_set_rgb(self, red: int, green: int, blue: int) -> None:
        hid_data_list = lighting_enable_set_rgb_spec(red=red, green=green, blue=blue)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    # --- Mixer ---

    def mixer_playback_mute(self, mute: bool) -> None:
        audio_data_list = mixer_playback_mute_spec(mute)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def mixer_monitoring_line_in_mute(self, mute: bool) -> None:
        audio_data_list = monitoring_line_in_mute_spec(mute)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def mixer_monitoring_line_in_volume(self, volume_percent: int) -> None:
        audio_data_list = monitoring_line_in_volume_spec(volume_percent)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def mixer_monitoring_external_mic_mute(self, mute: bool) -> None:
        audio_data_list = monitoring_external_mic_mute_spec(mute)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def mixer_monitoring_external_mic_volume(self, volume_percent: int) -> None:
        audio_data_list = monitoring_external_mic_volume_spec(volume_percent)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def mixer_monitoring_spdif_in_mute(self, mute: bool) -> None:
        audio_data_list = monitoring_spdif_in_mute_spec(mute)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def mixer_monitoring_spdif_in_volume(self, volume_percent: int) -> None:
        audio_data_list = monitoring_spdif_in_volume_spec(volume_percent)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def mixer_recording_line_in_mute(self, mute: bool) -> None:
        audio_data_list = recording_line_in_mute_spec(mute)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def mixer_recording_line_in_volume(self, volume_percent: int) -> None:
        audio_data_list = recording_line_in_volume_spec(volume_percent)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def mixer_recording_external_mic_mute(self, mute: bool) -> None:
        audio_data_list = recording_external_mic_mute_spec(mute)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def mixer_recording_external_mic_volume(self, volume_percent: int) -> None:
        audio_data_list = recording_external_mic_volume_spec(volume_percent)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def mixer_recording_spdif_in_mute(self, mute: bool) -> None:
        audio_data_list = recording_spdif_in_mute_spec(mute)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def mixer_recording_spdif_in_volume(self, volume_percent: int) -> None:
        audio_data_list = recording_spdif_in_volume_spec(volume_percent)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def mixer_recording_what_u_hear_mute(self, mute: bool) -> None:
        audio_data_list = recording_what_u_hear_mute_spec(mute)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def mixer_recording_what_u_hear_volume(self, volume_percent: int) -> None:
        audio_data_list = recording_what_u_hear_volume_spec(volume_percent)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    # --- Recording ---

    def recording_mute(self, mute: bool) -> None:
        audio_data_list = recording_mute_spec(mute)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def recording_mic_recording_volume(self, volume_percent: int) -> None:
        audio_data_list = mic_recording_volume_spec(volume_percent)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def recording_mic_boost(self, decibel: int) -> None:
        hid_data_list = mic_boost_spec(decibel)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    def recording_mic_monitoring(self, volume_percent: int) -> None:
        audio_data_list = mic_monitoring_spec(volume_percent)
        send_audio_data_to_device(
            device=self.__device,
            audio_data_list=audio_data_list,
            dry_run=self.__dry_run,
        )

    def recording_voice_clarity_enabled(self, enable: bool) -> None:
        hid_data_list = voice_clarity_enabled_spec(enable)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    def recording_voice_clarity_level(self, level_percent: int) -> None:
        hid_data_list = voice_clarity_level_spec(level_percent)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    def recording_acoustic_echo_cancellation_enabled(self, enable: bool) -> None:
        hid_data_list = acoustic_echo_cancellation_enabled_spec(enable)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    def recording_smart_volume_enabled(self, enable: bool) -> None:
        hid_data_list = smart_volume_enabled_spec(enable)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    def recording_mic_equalizer_enabled(self, enable: bool) -> None:
        hid_data_list = mic_equalizer_enabled_spec(enable)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    def recording_mic_equalizer_preset(self, preset: MicrophoneEqualizerPreset) -> None:
        hid_data_list = mic_equalizer_preset_spec(preset)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    # --- SBX ---

    def sbx_toggle(self, audio_feature: AudioFeature, activate: bool) -> None:
        hid_data_list = sbx_toggle_spec(audio_feature=audio_feature, activate=activate)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    def sbx_slider(self, audio_feature: AudioFeature, value: int) -> None:
        hid_data_list = sbx_slider_spec(audio_feature=audio_feature, value=value)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )

    def sbx_smart_volume_special(self, smart_volume_special_hex: SmartVolumeSpecialHex) -> None:
        hid_data_list = sbx_smart_volume_special_spec(smart_volume_special_hex=smart_volume_special_hex)
        send_hid_data_to_device(
            device=self.__device,
            hid_data_list=hid_data_list,
            dry_run=self.__dry_run,
        )
