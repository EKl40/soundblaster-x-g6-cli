import os
from enum import Enum

# The payloads available to send to the G6
PAYLOAD_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'payloads')
PAYLOAD_HEX_LINE_PATTERN = r'^[a-f0-9]{128}$'


class Payload(Enum):
    ZERO_TO_ONE_HUNDRED = 0
    TOGGLE_OUTPUT_TO_HEADPHONES = 1
    TOGGLE_OUTPUT_TO_SPEAKERS = 2

    AUDIO_BITRATE_16 = 10
    AUDIO_BITRATE_24 = 11
    AUDIO_BITRATE_32 = 12

    AUDIO_DECODER_FULL = 20
    AUDIO_DECODER_NIGHT = 21
    AUDIO_DECODER_NORMAL = 22

    AUDIO_MODE_STEREO = 30
    AUDIO_MODE_5_1 = 31
    AUDIO_MODE_7_1 = 32

    AUDIO_PHASE_FAST_LINEAR = 40
    AUDIO_PHASE_FAST_MINIMAL = 41
    AUDIO_PHASE_SLOW_LINEAR = 42
    AUDIO_PHASE_SLOW_MINIMAL = 43

    AUDIO_PLAYBACK_SAMPLE_RATE_48 = 50
    AUDIO_PLAYBACK_SAMPLE_RATE_88 = 51
    AUDIO_PLAYBACK_SAMPLE_RATE_96 = 52

    AUDIO_RECORDING_SAMPLE_RATE_44 = 60
    AUDIO_RECORDING_SAMPLE_RATE_48 = 61
    AUDIO_RECORDING_SAMPLE_RATE_88 = 62
    AUDIO_RECORDING_SAMPLE_RATE_96 = 63
    AUDIO_RECORDING_SAMPLE_RATE_176 = 64
    AUDIO_RECORDING_SAMPLE_RATE_192 = 65

    def get_relative_file_path(self) -> str:
        match self:
            case self.ZERO_TO_ONE_HUNDRED:
                return '0-100.hex'
            case self.TOGGLE_OUTPUT_TO_HEADPHONES:
                return 'toggle-output-to-headphones.hex'
            case self.TOGGLE_OUTPUT_TO_SPEAKERS:
                return 'toggle-output-to-speakers.hex'
            case self.AUDIO_BITRATE_16:
                return f"audio-bitrate{os.sep}audio-bitrate-16.hex"
            case self.AUDIO_BITRATE_24:
                return f"audio-bitrate{os.sep}audio-bitrate-24.hex"
            case self.AUDIO_BITRATE_32:
                return f"audio-bitrate{os.sep}audio-bitrate-32.hex"
            case self.AUDIO_DECODER_FULL:
                return f"audio-decoder{os.sep}audio-decoder-full.hex"
            case self.AUDIO_DECODER_NIGHT:
                return f"audio-decoder{os.sep}audio-decoder-night.hex"
            case self.AUDIO_DECODER_NORMAL:
                return f"audio-decoder{os.sep}audio-decoder-normal.hex"
            case self.AUDIO_MODE_STEREO:
                return f"audio-mode{os.sep}audio-mode-stereo.hex"
            case self.AUDIO_MODE_5_1:
                return f"audio-mode{os.sep}audio-mode-5-1.hex"
            case self.AUDIO_MODE_7_1:
                return f"audio-mode{os.sep}audio-mode-7-1.hex"
            case self.AUDIO_PHASE_FAST_LINEAR:
                return f"audio-phase{os.sep}audio-phase-fast-linear.hex"
            case self.AUDIO_PHASE_FAST_MINIMAL:
                return f"audio-phase{os.sep}audio-phase-fast-minimal.hex"
            case self.AUDIO_PHASE_SLOW_LINEAR:
                return f"audio-phase{os.sep}audio-phase-slow-linear.hex"
            case self.AUDIO_PHASE_SLOW_MINIMAL:
                return f"audio-phase{os.sep}audio-phase-slow-minimal.hex"
            case self.AUDIO_PLAYBACK_SAMPLE_RATE_48:
                return f"audio-playback-sample-rate{os.sep}audio-playback-sample-rate-48.hex"
            case self.AUDIO_PLAYBACK_SAMPLE_RATE_88:
                return f"audio-playback-sample-rate{os.sep}audio-playback-sample-rate-88.hex"
            case self.AUDIO_PLAYBACK_SAMPLE_RATE_96:
                return f"audio-playback-sample-rate{os.sep}audio-playback-sample-rate-96.hex"
            case self.AUDIO_RECORDING_SAMPLE_RATE_44:
                return f"audio-recording-sample-rate{os.sep}audio-recording-sample-rate-44.hex"
            case self.AUDIO_RECORDING_SAMPLE_RATE_48:
                return f"audio-recording-sample-rate{os.sep}audio-recording-sample-rate-48.hex"
            case self.AUDIO_RECORDING_SAMPLE_RATE_88:
                return f"audio-recording-sample-rate{os.sep}audio-recording-sample-rate-88.hex"
            case self.AUDIO_RECORDING_SAMPLE_RATE_96:
                return f"audio-recording-sample-rate{os.sep}audio-recording-sample-rate-96.hex"
            case self.AUDIO_RECORDING_SAMPLE_RATE_176:
                return f"audio-recording-sample-rate{os.sep}audio-recording-sample-rate-176.hex"
            case self.AUDIO_RECORDING_SAMPLE_RATE_192:
                return f"audio-recording-sample-rate{os.sep}audio-recording-sample-rate-192.hex"
            case _:
                raise ValueError(f"Unexpected Payload enum value: {self}!")

    def get_file_path(self) -> str:
        return os.path.join(PAYLOAD_DIR_PATH, self.get_relative_file_path())

    def read_hex_lines(self) -> [str]:
        """
        Read the hex data from a payload text file as list, omitting any line separators
        :return: the stripped file content lines as list
        """
        with open(self.get_file_path(), 'r') as file:
            return [line.strip() for line in file.readlines()]
