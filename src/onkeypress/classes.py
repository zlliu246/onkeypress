from enum import Enum
from typing import Any, Callable, Sequence, Mapping, Self, Optional

import platform
WINDOWS = platform.system() in ["Windows", "CYGWIN"]

class Key(Enum):
    ALL_OTHERS = "ALL_OTHERS"
    ESCAPE = "\x1b"
    BACKSPACE = "\x7f" if not WINDOWS else "\x08"

    ENTER = "\n" if not WINDOWS else "\r"
    UP = "\x1b[A" if not WINDOWS else "\xe0H"
    DOWN = "\x1b[B" if not WINDOWS else "\xe0P"
    LEFT = "\x1b[D" if not WINDOWS else "\xe0K"
    RIGHT = "\x1b[C" if not WINDOWS else "\xe0M"

    CONTROL_Z = "\x19" if not WINDOWS else "\x1a"
    CONTROL_X = "\x18" if not WINDOWS else "\x18"
    CONTROL_C = "\x17" if not WINDOWS else "\x03"
    CONTROL_V = "\x16" # overridden by paste in Windows (lol)
    CONTROL_B = "\x02" if not WINDOWS else "\x02"

class KeyPressInfo:
    def __init__(
        self,
        user_input_key: Key | str
    ) -> None:
        """initializes a KeyPressInfo object"""

        if isinstance(user_input_key, Key):
            self._key_str: str = user_input_key.value
        elif isinstance(user_input_key, str):
            self._key_str: str = user_input_key
        else:
            raise ValueError(f"Invalid key {user_input_key}. Should be either Key or string")

        self._func = lambda : None
        self._args = ()
        self._kwargs = {}

    def call(
        self,
        func: Callable,
    ) -> Self:
        """Initializes self._func - when self._key_str is pressed, self._func is called"""
        self._func = func
        return self
    
    def args(self, *args: Any) -> Self:
        """Initializes self._args - self._func is called using self._func(*self._args, **self._kwargs)"""
        self._args = args or []
        return self
    
    def kwargs(self, **kwargs: Any) -> Self:
        """Initializes self._kwargs - self._func is called using self._func(*self._args, **self._kwargs)"""
        self._kwargs = kwargs or {}
        return self
    
    def invoke(self, char: Optional[str] = None) -> Any:
        """
        Actually call self._func(*self._args, **self._kwargs)

        Args:
            char (Optional[str]): character to pass in (usually used with Key.ALL_OTHERS)
        """
        if char is not None:
            # char is passed as first arg to self._func
            output: Any = self._func(char, *self._args, **self._kwargs)
            print(end="", flush=True)
            return output

        output: Any = self._func(*self._args, **self._kwargs)
        print(end="", flush=True)
        return output