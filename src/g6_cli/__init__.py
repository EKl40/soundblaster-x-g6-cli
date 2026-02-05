import argparse
import os.path
import tempfile

from g6_cli.g6_api.g6_core import send_to_device, detect_device, device_set_audio_effects
from g6_cli.g6_api.g6_payload import Payload
from g6_cli.g6_spec import Audio

# The name of the temporary file to remember the last toggle state in. If the file could not be found. The program
# lets the G6 to toggle to Speakers by default.
TOGGLE_STATE_TEMP_FILE_NAME = 'g6-cli-toggle-state'
TOGGLE_STATE_SPEAKERS = 'Speakers'
TOGGLE_STATE_HEADPHONES = 'Headphones'


def parse_cli_args():
    """
    Parse the CLI arguments using argparse.
    Prints the CLI help to console and raises an error, if the arguments are invalid.
    :return: the parsed cli args object
    """
    numbers = [i for i in range(0, 101)]
    enabled_disabled = ['Enabled', 'Disabled']

    parser = argparse.ArgumentParser(description='SoundBlaster X G6 CLI')
    #
    # Base options
    #
    # -- toggle-output
    parser.add_argument('--toggle-output', required=False, action='store_true',
                        help='Toggles the sound output between Speakers and Headphones')
    # --set-output
    parser.add_argument('--set-output', required=False, type=str,
                        choices=[TOGGLE_STATE_SPEAKERS, TOGGLE_STATE_HEADPHONES])
    # --dry-run
    parser.add_argument('--dry-run', required=False, action='store_true',
                        help='Used to verify the available hex_line files, without making '
                             'any calls against the G6 device.')
    #
    # Sound Effects
    #
    # --set-surround
    parser.add_argument('--set-surround', required=False, type=str, choices=enabled_disabled,
                        help='Enables or disables the Surround sound effect: [\'Enabled\', \'Disabled\']')
    parser.add_argument('--set-surround-value', required=False, type=int, choices=numbers,
                        help='Set the value for the Surround sound effect as integer: [0 .. 100].')
    # --set-crystalizer
    parser.add_argument('--set-crystalizer', required=False, type=str, choices=enabled_disabled,
                        help='Enables or disables the Crystalizer sound effect: [\'Enabled\', \'Disabled\']')
    parser.add_argument('--set-crystalizer-value', required=False, type=int, choices=numbers,
                        help='Set the value for the Crystalizer sound effect as integer: [0 .. 100].')
    # --set-bass
    parser.add_argument('--set-bass', required=False, type=str, choices=enabled_disabled,
                        help='Enables or disables the Bass sound effect: [\'Enabled\', \'Disabled\']')
    parser.add_argument('--set-bass-value', required=False, type=int, choices=numbers,
                        help='Set the value for the Bass sound effect as integer: [0 .. 100].')
    # --set-smart-volume
    parser.add_argument('--set-smart-volume', required=False, type=str, choices=enabled_disabled,
                        help='Enables or disables the Smart-Volume sound effect: [\'Enabled\', \'Disabled\']')
    parser.add_argument('--set-smart-volume-value', required=False, type=int, choices=numbers,
                        help='Set the value for the Smart-Volume sound effect as value: [0 .. 100].')
    parser.add_argument('--set-smart-volume-special-value', required=False, type=str, choices=['Night', 'Loud'],
                        help='Set the value for the Smart-Volume sound effect as string: \'Night\', \'Loud\'. '
                             'Supersedes the value from \'--set-smart-volume-value\'!')
    # --set-dialog-plus
    parser.add_argument('--set-dialog-plus', required=False, type=str, choices=enabled_disabled,
                        help='Enables or disables the Dialog-Plus sound effect: [\'Enabled\', \'Disabled\']')
    parser.add_argument('--set-dialog-plus-value', required=False, type=int, choices=numbers,
                        help='Set the value for the Dialog-Plus sound effect as integer: : [0 .. 100].')

    # parse args and verify
    args = parser.parse_args()
    if args.toggle_output is False \
            and args.set_output is None \
            and args.set_surround is None \
            and args.set_surround_value is None \
            and args.set_crystalizer is None \
            and args.set_crystalizer_value is None \
            and args.set_bass is None \
            and args.set_bass_value is None \
            and args.set_smart_volume is None \
            and args.set_smart_volume_value is None \
            and args.set_smart_volume_special_value is None \
            and args.set_dialog_plus is None \
            and args.set_dialog_plus_value is None:
        message = 'No meaningful argument has been specified!'
        print(message)
        parser.print_help()
        raise ValueError(message)
    elif args.toggle_output is True and args.set_output is not None:
        message = 'Only one of the following CLI arguments may be specified: \'--toggle-output', '--set-output\'!'
        print(message)
        parser.print_help()
        raise ValueError(message)

    return args


def read_toggle_state_file(toggle_state_file_path):
    """
    Read the toggle state from the temporary file to determine the state from previous runs.
    :param toggle_state_file_path: The path to the file, where the last toggle state has been remembered in.
    :return: The content of the file. Should be either 'Speakers' or 'Headphones'.
    """
    with open(toggle_state_file_path, 'r') as file:
        return file.read()


def write_toggle_state_file(toggle_state_file_path, toggle_state_value):
    """
    Write the currently used toggle_state to the temporary file for next runs.
    :param toggle_state_file_path: The path to the file for remembering the last set toggle state.
    :param toggle_state_value: The toggle state to write to the file. Should be either 'Speakers' or 'Headphones'.
    """
    with open(toggle_state_file_path, 'w') as file:
        file.write(str(toggle_state_value))


def determine_toggle_state():
    """
    Reads the last used toggle_state value from the temporary file to determine the next value.
    If the temporary file does not exist, 'Speakers' is used by default.
    :return: The just set and now active toggle state value.
    """
    toggle_state_file_path = os.path.join(tempfile.gettempdir(), TOGGLE_STATE_TEMP_FILE_NAME)
    # determine toggle state from temporary file or use SPEAKERS by default
    if os.path.exists(toggle_state_file_path):
        current_toggle_state = read_toggle_state_file(toggle_state_file_path)
        next_toggle_state = TOGGLE_STATE_SPEAKERS \
            if current_toggle_state == TOGGLE_STATE_HEADPHONES \
            else TOGGLE_STATE_HEADPHONES
        print(
            f'Toggle from '
            f'{current_toggle_state} -> {next_toggle_state}')
    else:
        next_toggle_state = TOGGLE_STATE_SPEAKERS
        print(f'Toggle to {next_toggle_state}')
    # write next toggle state to temporary file
    write_toggle_state_file(toggle_state_file_path, next_toggle_state)
    # return the next toggle state to send it to the G6
    return next_toggle_state


def device_toggle_output(device_path, dry_run):
    """
    Toggles the device's output. Either Speakers -> Headphones or Headphones -> Speakers.
    :param device_path: The detected usb device path for the G6.
    :param dry_run: whether to simulate communication with the device for program testing purposes.
                    If set to true, no data is sent to the G6!
    """
    # determine next toggle state
    toggle_state = determine_toggle_state()
    # determine payload to load
    payload = Payload.TOGGLE_OUTPUT_TO_SPEAKERS \
        if toggle_state == TOGGLE_STATE_HEADPHONES \
        else Payload.TOGGLE_OUTPUT_TO_HEADPHONES
    # read payload from file
    payload_hex_lines = payload.read_hex_lines()
    # send the payload to the device
    print(f'About to send payload to device: {payload.get_relative_file_path()}')
    send_to_device(device_path, payload_hex_lines, dry_run)


def device_set_output(device_path, toggle_state, dry_run):
    """
    Set a specific device output. Either 'Speakers' or 'Headphones'
    :param device_path: The detected usb device path for the G6.
    :param toggle_state: the toggle_state value to set the G6's output to. Should be either 'Speakers' or 'Headphones'.
    :param dry_run: whether to simulate communication with the device for program testing purposes.
                    If set to true, no data is sent to the G6!
    """
    # determine payload to load
    if toggle_state == TOGGLE_STATE_SPEAKERS:
        payload = Payload.TOGGLE_OUTPUT_TO_SPEAKERS
    elif toggle_state == TOGGLE_STATE_HEADPHONES:
        payload = Payload.TOGGLE_OUTPUT_TO_HEADPHONES
    else:
        raise ValueError(
            f'The given toggle_state must either be {TOGGLE_STATE_SPEAKERS} or {TOGGLE_STATE_HEADPHONES}, '
            f'but was {toggle_state}!')
    # read payload from file
    payload_hex_lines = payload.read_hex_lines()
    # send the payload to the device
    print(f'About to send payload to device: {payload.get_relative_file_path()}')
    send_to_device(device_path, payload_hex_lines, dry_run)


def main():
    args = parse_cli_args()
    device_path = detect_device()
    audio = Audio()

    # handle device output
    if args.toggle_output:
        device_toggle_output(device_path, args.dry_run)
    elif args.set_output is not None:
        device_set_output(device_path, args.set_output, args.dry_run)

    # handle audio effects
    device_set_audio_effects(device_path, audio, args)

