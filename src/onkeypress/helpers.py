import sys
import platform

WINDOWS = platform.system() in ["Windows", "CYGWIN"]

def get_input_char() -> str:
    if WINDOWS:
        import msvcrt
        char_bytes: bytes = msvcrt.getch()
        try:
            return char_bytes.decode("unicode_escape")
        except:
            return char_bytes.decode("utf-8")
    else:
        return sys.stdin.read(1)