import os
import sys
from typing import Sequence

from .classes import Key, KeyPressInfo
from .decorators import handle_cbreak_and_exceptions


def onkeypress(key: Key | str):
    return KeyPressInfo(key)

@handle_cbreak_and_exceptions
def while_not_exit(
    *keypressinfos: Sequence[KeyPressInfo],
    exit_key: Key = Key.ENTER,
    exit_message: str = "",
) -> Key:
    """
    Waits for user to press keys, and invoke functions accordingly

    Exits when user hits the exit_key (default Key.ENTER)

    Args:
        keypress_info_sequence (Sequence[KeyPressInfo]): KeyPressInfo objects passed as *args
        exit_key (Key): If user presses this key, this function exits.
        exit_message (str): prints when user exits
    """

    esc_char_to_keypressinfo_map: dict[str, KeyPressInfo] = {
        kpi._key_str: kpi for kpi in keypressinfos
    }

    # using 3 as escape characters are usually 1-3 characteres long
    last3chars: str = "___"

    while True:
        input_char: str = sys.stdin.read(1)
        last3chars: str = last3chars[1:] + input_char

        # first check for last3chars (usually escape characters)
        if last3chars in esc_char_to_keypressinfo_map:
            kpi: KeyPressInfo = esc_char_to_keypressinfo_map[last3chars]
            kpi.invoke()

        # then check for single chars (escape chars take precedence)
        elif input_char in esc_char_to_keypressinfo_map:
            kpi: KeyPressInfo = esc_char_to_keypressinfo_map[input_char]
            kpi.invoke()

        elif "ALL_OTHERS" in esc_char_to_keypressinfo_map:
            kpi: KeyPressInfo = esc_char_to_keypressinfo_map["ALL_OTHERS"]
            kpi.invoke(char=input_char)
            
        # check for exit condition
        exit_key_length = len(exit_key.value)
        if last3chars[-exit_key_length:] == exit_key.value:
            print(exit_message)
            return

__all__ = ["while_not_exit", "onkeypress", "Key"]
