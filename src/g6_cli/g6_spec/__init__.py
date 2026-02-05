from enum import Enum

__slider_percent_to_hex_dict: dict[int, int] = {
    0: 0x00000000,
    1: 0x0ad7233c,
    2: 0x0ad7a33c,
    3: 0x8fc2f53c,
    4: 0x0ad7233d,
    5: 0xcdcc4c3d,
    6: 0x8fc2753d,
    7: 0x295c8f3d,
    8: 0x0ad7a33d,
    9: 0xec51b83d,
    10: 0xcdcccc3d,
    11: 0xae47e13d,
    12: 0x8fc2f53d,
    13: 0xb81e053e,
    14: 0x295c0f3e,
    15: 0x9a99193e,
    16: 0x0ad7233e,
    17: 0x7b142e3e,
    18: 0xec51383e,
    19: 0x5c8f423e,
    20: 0xcdcc4c3e,
    21: 0x3d0a573e,
    22: 0xae47613e,
    23: 0x1f856b3e,
    24: 0x8fc2753e,
    25: 0x0000803e,
    26: 0xb81e853e,
    27: 0x713d8a3e,
    28: 0x295c8f3e,
    29: 0xe17a943e,
    30: 0x9a99993e,
    31: 0x52b89e3e,
    32: 0x0ad7a33e,
    33: 0xc3f5a83e,
    34: 0x7b14ae3e,
    35: 0x3333b33e,
    36: 0xec51b83e,
    37: 0xa470bd3e,
    38: 0x5c8fc23e,
    39: 0x14aec73e,
    40: 0xcdcccc3e,
    41: 0x85ebd13e,
    42: 0x3d0ad73e,
    43: 0xf628dc3e,
    44: 0xae47e13e,
    45: 0x6666e63e,
    46: 0x1f85eb3e,
    47: 0xd7a3f03e,
    48: 0x8fc2f53e,
    49: 0x48e1fa3e,
    50: 0x0000003f,
    51: 0x5c8f023f,
    52: 0xb81e053f,
    53: 0x14ae073f,
    54: 0x713d0a3f,
    55: 0xcdcc0c3f,
    56: 0x295c0f3f,
    57: 0x85eb113f,
    58: 0xe17a143f,
    59: 0x3d0a173f,
    60: 0x9a99193f,
    61: 0xf6281c3f,
    62: 0x52b81e3f,
    63: 0xae47213f,
    64: 0x0ad7233f,
    65: 0x6666263f,
    66: 0xc3f5283f,
    67: 0x1f852b3f,
    68: 0x7b142e3f,
    69: 0xd7a3303f,
    70: 0x3333333f,
    71: 0x8fc2353f,
    72: 0xec51383f,
    73: 0x48e13a3f,
    74: 0xa4703d3f,
    75: 0x0000403f,
    76: 0x5c8f423f,
    77: 0xb81e453f,
    78: 0x14ae473f,
    79: 0x713d4a3f,
    80: 0xcdcc4c3f,
    81: 0x295c4f3f,
    82: 0x85eb513f,
    83: 0xe17a543f,
    84: 0x3d0a573f,
    85: 0x9a99593f,
    86: 0xf6285c3f,
    87: 0x52b85e3f,
    88: 0xae47613f,
    89: 0x0ad7633f,
    90: 0x6666663f,
    91: 0xc3f5683f,
    92: 0x1f856b3f,
    93: 0x7b146e3f,
    94: 0xd7a3703f,
    95: 0x3333733f,
    96: 0x8fc2753f,
    97: 0xec51783f,
    98: 0x48e17a3f,
    99: 0xa4707d3f,
    100: 0x0000803f,
}

__playback_volume_percent_to_hex_dict: dict[int, int] = {
    0: 0x00c0,
    10: 0xe7de,
    20: 0x69e8,
    30: 0x37ee,
    40: 0x68f2,
    50: 0xb0f5,
    60: 0x62f8,
    70: 0xacfa,
    80: 0xaafc,
    90: 0x6cfe,
    100: 0x0000,
}

__mic_recording_volume_percent_to_hex_dict: dict[int, int] = {
    0: 0x00d0,
    10: 0x2ee6,
    20: 0xd7ee,
    30: 0x52f4,
    40: 0x57f8,
    50: 0x84fb,
    60: 0x25fe,
    70: 0x6400,
    80: 0xc202,
    90: 0x8f05,
    100: 0x0009,
}

__mic_monitoring_volume_percent_to_hex_dict: dict[int, int] = __playback_volume_percent_to_hex_dict

__mic_boost_decibel_to_hex_dict: dict[int, int] = {
    0: 0x0000,
    10: 0x0a000000,
    20: 0x14000000,
    30: 0x1e000000
}

__mic_voice_clarity_level_to_hex_dict: dict[int, int] = {
    0: 0x00000000,
    20: 0xcdcccc3d,
    40: 0xcdcc4c3e,
    60: 0x9a99993e,
    80: 0xcdcccc3e,
    100: 0x0000003f
}


def get_slider_percent_hex(percent_value: int) -> int:
    return __slider_percent_to_hex_dict[percent_value]


def get_playback_volume_percent_hex(percent_value: int) -> int:
    return __playback_volume_percent_to_hex_dict[percent_value]


def get_mic_recording_volume_percent_hex(percent_value: int) -> int:
    return __mic_recording_volume_percent_to_hex_dict[percent_value]


def get_mic_monitoring_volume_percent_hex(percent_value: int) -> int:
    return __mic_monitoring_volume_percent_to_hex_dict[percent_value]


def get_mic_boost_decibel_hex(decibel: int) -> int:
    return __mic_boost_decibel_to_hex_dict[decibel]


def get_mic_voice_clarity_level_hex(level: int) -> int:
    return __mic_voice_clarity_level_to_hex_dict[level]


class DataFragmentStatic(Enum):
    PREFIX = 0x5a
    RECORDING_INTERMEDIATE = 0x0195
    PLAYBACK_INTERMEDIATE = 0x0196
    DECODER_INTERMEDIATE = 0x0197


class DataFragmentMode(Enum):
    DATA = 0x1207
    COMMIT = 0x1103


class SmartVolumeSpecialHex(Enum):
    SMART_VOLUME_NIGHT = 0x00000040
    SMART_VOLUME_LOUD = 0x0000803f


class AudioFeature(Enum):
    SURROUND_TOGGLE = 0x00,
    SURROUND_SLIDER = 0x01,
    CRYSTALIZER_TOGGLE = 0x07,
    CRYSTALIZER_SLIDER = 0x08,
    BASS_TOGGLE = 0x18,
    BASS_SLIDER = 0x19,
    SMART_VOLUME_TOGGLE = 0x04,
    SMART_VOLUME_SLIDER = 0x05,
    SMART_VOLUME_SPECIAL = 0x06
    DIALOG_PLUS_TOGGLE = 0x02,
    DIALOG_PLUS_SLIDER = 0x03


class PlaybackFilter(Enum):
    FAST_ROLL_OFF_MINIUM_PHASE = 0x0001
    SLOW_ROLL_OFF_MINIUM_PHASE = 0x0002
    FAST_ROLL_OFF_LINEAR_PHASE = 0x0004
    SLOW_ROLL_OFF_LINEAR_PHASE = 0x0005


class UsbAudioData:
    def __init__(self, b_request: int, w_value: int, w_index: int, w_length: int, data_fragment: int):
        self.__bmRequestType = to_hex_str(0x21).zfill(2)
        self.__bRequest = to_hex_str(b_request).zfill(2)
        self.__wValue = to_hex_str(w_value).zfill(4)
        self.__wIndex = to_hex_str(w_index).zfill(4)
        self.__wLength = to_hex_str(w_length).zfill(4)
        self.__data_fragment = to_hex_str(data_fragment)


class UsbHidDataFragment:
    def __init__(self, mode: int, audio_feature: int, intermediate: int, value: int, additional_payload: int):
        self.__static_prefix = to_hex_str(DataFragmentStatic.PREFIX.value).zfill(2)
        self.__mode = to_hex_str(mode).zfill(4)
        self.__static_intermediate = to_hex_str(intermediate).zfill(4)
        self.__audio_feature = to_hex_str(audio_feature).zfill(2)
        self.__value = to_hex_str(value).zfill(8)
        self.__additional_payload = to_hex_str(additional_payload).ljust(56, '0')

    @classmethod
    def from_enum(cls, mode: DataFragmentMode, audio_feature: AudioFeature, value: int):
        return cls(mode=mode.value, audio_feature=audio_feature.value[0],
                   intermediate=DataFragmentStatic.PLAYBACK_INTERMEDIATE.value, value=value, additional_payload=0x00)

    @classmethod
    def being_data(cls, audio_feature: int, value: int):
        return cls(mode=DataFragmentMode.DATA.value, audio_feature=audio_feature,
                   intermediate=DataFragmentStatic.PLAYBACK_INTERMEDIATE.value, value=value, additional_payload=0x00)

    @classmethod
    def being_commit(cls, audio_feature: int, value: int):
        return cls(mode=DataFragmentMode.COMMIT.value, audio_feature=audio_feature,
                   intermediate=DataFragmentStatic.PLAYBACK_INTERMEDIATE.value, value=value, additional_payload=0x00)

    @classmethod
    def empty_additional_payload(cls, mode: int, audio_feature: int, intermediate: int, value: int):
        return cls(mode=mode, audio_feature=audio_feature, intermediate=intermediate, value=value,
                   additional_payload=0x00)

    def __str__(self):
        value = f'{self.__static_prefix}{self.__mode}{self.__static_intermediate}{self.__audio_feature}{self.__value}{self.__additional_payload}'
        if not len(value) == 128:
            raise ValueError(f'Generated hex-line string has unexpected length \'{len(value)}\'! '
                             f'Expected length is 128, but was \'{value}\'!')
        return value

    def __repr__(self):
        return self.__str__()


class Audio:
    def __init__(self):
        pass

    def build_hex_lines_toggle(self, audio_feature: AudioFeature, enabled: bool):
        """
        Build a list of 64 byte hex-line commands for the given AudioFeature's toggle.
        :param audio_feature: the enum value of the AudioFeature to build the hex-line for
        :param enabled: the boolean value, whether to enable or disable the AudioFeature.
        :return: a list of hex-line commands, designated to being sent to the G6.
        """
        if type(audio_feature) is not AudioFeature:
            raise ValueError(f'Argument \'audio_feature_enum\' should be of type \'{type(AudioFeature)}\','
                             f' but was \'{type(audio_feature)}\'!')
        if type(enabled) is not bool:
            raise ValueError(f'Argument \'enabled\' should be of type \'{type(bool)}\','
                             f' but was \'{type(enabled)}\'!')

        audio_feature_hex = audio_feature.value[0]
        value_hex = get_slider_percent_hex(100) if enabled else get_slider_percent_hex(0)

        return [
            self.__build_hex_line(DataFragmentMode.DATA, audio_feature_hex, value_hex),
            self.__build_hex_line(DataFragmentMode.COMMIT, audio_feature_hex, 0)
        ]

    def build_hex_lines_slider(self, audio_feature: AudioFeature, value: int):
        """
        Build a list of 64 byte hex-line commands for the given AudioFeature's slider value.
        :param audio_feature: the enum value of the AudioFeature to build the hex-line for
        :param value: the integer value for the slider of the corresponding AudioFeature (0 - 100)
        :return: a list of hex-line commands, designated to being sent to the G6.
        """
        if type(audio_feature) is not AudioFeature:
            raise ValueError(f'Argument \'audio_feature_enum\' should be of type \'{type(AudioFeature)}\','
                             f' but was \'{type(audio_feature)}\'!')
        if type(value) is not int:
            raise ValueError(f'Argument \'value\' should be of type \'{type(int)}\','
                             f' but was \'{type(value)}\'!')
        if value < 0 or value > 100:
            raise ValueError(f'Argument \'value\' should be between \'0\' and \'100\', but was \'{value}\'!')

        audio_feature_hex = audio_feature.value[0]
        value_hex = get_slider_percent_hex(value)

        return [
            self.__build_hex_line(DataFragmentMode.DATA, audio_feature_hex, value_hex),
            self.__build_hex_line(DataFragmentMode.COMMIT, audio_feature_hex, 0)
        ]

    def build_hex_lines_slider_special(self, audio_feature: AudioFeature,
                                       smart_volume_special_hex: SmartVolumeSpecialHex):
        """
        Build a list of 64 byte hex-line commands for the given AudioFeature's slider special value.
        :param audio_feature: the enum value of the AudioFeature to build the hex-line for
        :param smart_volume_special_hex: the value to set as SmartVolumeSpecialHex enum value
        :return: a list of hex-line commands, designated to being sent to the G6.
        """
        if type(audio_feature) is not AudioFeature:
            raise ValueError(f'Argument \'audio_feature_enum\' should be of type \'{type(AudioFeature)}\','
                             f' but was \'{type(audio_feature)}\'!')
        if type(smart_volume_special_hex) is not SmartVolumeSpecialHex:
            raise ValueError(f'Argument \'audio_feature_special_value_enum\' should be of type '
                             f'\'{type(SmartVolumeSpecialHex)}\','
                             f' but was \'{type(smart_volume_special_hex)}\'!')

        if audio_feature is AudioFeature.SMART_VOLUME_SPECIAL and \
                (smart_volume_special_hex is SmartVolumeSpecialHex.SMART_VOLUME_NIGHT
                 or smart_volume_special_hex is SmartVolumeSpecialHex.SMART_VOLUME_LOUD):
            audio_feature_hex = audio_feature.value[0]
            value_hex = smart_volume_special_hex.value[0]
        else:
            raise ValueError(f'Unexpected combination of audio_feature_enum \'{audio_feature}\' and '
                             f'audio_feature_special_value_enum \'{smart_volume_special_hex}\'!')

        return [
            self.__build_hex_line(DataFragmentMode.DATA, audio_feature_hex, value_hex),
            self.__build_hex_line(DataFragmentMode.COMMIT, audio_feature_hex, 0)
        ]

    @staticmethod
    def __build_hex_line(data_fragment_mode: DataFragmentMode, audio_feature_hex: int, value_hex: int):
        if type(data_fragment_mode) is not DataFragmentMode:
            raise ValueError(f'Argument \'data_fragment_mode\' should be of type \'{type(DataFragmentMode)}\','
                             f' but was \'{type(data_fragment_mode)}\'!')
        if type(audio_feature_hex) is not int:
            raise ValueError(f'Argument \'audio_feature_hex\' should be of type \'{type(int)}\','
                             f' but was \'{type(audio_feature_hex)}\'!')
        if type(value_hex) is not int:
            raise ValueError(f'Argument \'value_hex\' should be of type \'{type(int)}\','
                             f' but was \'{type(value_hex)}\'!')

        static_prefix = to_hex_str(DataFragmentStatic.PREFIX.value).zfill(2)
        mode = to_hex_str(data_fragment_mode.value).zfill(4)
        static_intermediate = to_hex_str(DataFragmentStatic.PLAYBACK_INTERMEDIATE.value).zfill(4)

        audio_feature = to_hex_str(audio_feature_hex).zfill(2)
        value = to_hex_str(value_hex).zfill(8)

        assembled = f'{static_prefix}{mode}{static_intermediate}{audio_feature}{value}'
        assembled_len = len(assembled)
        if assembled_len != 20:
            raise RuntimeError(f'The assembled hex_line part should have 20 characters, but it'
                               f' had {assembled_len}: \'{assembled}\'!')

        hex_line = assembled + '0' * 108
        hex_line_len = len(hex_line)
        if hex_line_len != 128:
            raise RuntimeError(f'The assembled hex_line should have 128 characters, but it'
                               f' had {hex_line_len}: \'{hex_line}\'!')

        return hex_line


def to_hex_str(int_value):
    return format(int_value, 'x')


class Decoder:
    pass


class Mixer:
    pass


class Lighting:
    pass
