import os
from enum import Enum

# The payloads available to send to the G6
PAYLOAD_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'payloads')
PAYLOAD_HEX_LINE_PATTERN = r'^[a-f0-9]{128}$'


class Payload(Enum):
    ZERO_TO_ONE_HUNDRED = 0
    TOGGLE_OUTPUT_TO_HEADPHONES = 1
    TOGGLE_OUTPUT_TO_SPEAKERS = 2

    def get_relative_file_path(self) -> str:
        match self:
            case self.ZERO_TO_ONE_HUNDRED:
                return '0-100.hex'
            case self.TOGGLE_OUTPUT_TO_HEADPHONES:
                return 'toggle-output-to-headphones.hex'
            case self.TOGGLE_OUTPUT_TO_SPEAKERS:
                return 'toggle-output-to-speakers.hex'
            case _:
                raise ValueError(f"Unexpected Payload enum value: {self}!")

    def get_file_path(self) -> str:
        return os.path.join(PAYLOAD_DIR_PATH, self.get_relative_file_path())

    def read_hex_lines(self) -> list[str]:
        """
        Read the hex data from a payload text file as list, omitting any line separators
        :return: the stripped file content lines as list
        """
        with open(self.get_file_path(), 'r') as file:
            return [line.strip() for line in file.readlines()]
