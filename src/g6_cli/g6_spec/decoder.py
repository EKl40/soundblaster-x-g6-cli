from enum import Enum

from g6_cli.g6_spec import UsbHidDataFragment, DataFragmentMode, DataFragmentStatic

DECODER_AUDIO_FEATURE = bytes.fromhex('02')


class DecoderMode(Enum):
    NORMAL = bytes.fromhex('00000040')
    FULL = bytes.fromhex('0000803F')
    NIGHT = bytes.fromhex('00004040')


def decoder_mode(decoder_mode_enum: DecoderMode) -> list[UsbHidDataFragment]:
    """
    Set decoder mode.
    :param decoder_mode_enum: The decoder mode to set, e.g.: Normal, Night or Full.
    :return: The list of UsbHidDataFragment objects to send to the G6, to set the decoder mode.
    """
    return [
        UsbHidDataFragment.empty_additional_payload(
            mode=DataFragmentMode.DATA.value,
            intermediate=DataFragmentStatic.DECODER_INTERMEDIATE.value,
            audio_feature=DECODER_AUDIO_FEATURE,
            value=decoder_mode_enum.value,
        ),
        UsbHidDataFragment.empty_additional_payload(
            mode=DataFragmentMode.COMMIT.value,
            intermediate=DataFragmentStatic.DECODER_INTERMEDIATE.value,
            audio_feature=DECODER_AUDIO_FEATURE,
            value=bytes.fromhex('00000000'),
        ),
    ]
