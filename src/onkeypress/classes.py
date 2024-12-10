from enum import Enum
from typing import Any, Callable, Sequence, Mapping, Self, Optional

class Key(Enum):
    ESCAPE = "\x1b"
    ENTER = "\n"
    UP = "\x1b[A"
    DOWN = "\x1b[B"
    LEFT = "\x1b[D"
    RIGHT = "\x1b[C"
    # TODO: add more

class KeyPressInfo:
    def __init__(
        self,
        user_input_key: Key | str
    ) -> None:
        """initializes a KeyPressInfo object"""

        self.key_str_value: str
        self.function: Callable
        self.args: Sequence[Any]
        self.kwargs: dict[str, Any]

        if isinstance(user_input_key, Key):
            self.key_str_value = user_input_key.value
        elif isinstance(user_input_key, str):
            self.key_str_value = user_input_key
        else:
            raise ValueError(f"Invalid key {user_input_key}. Should be either Key or string")

        self.function = lambda : None
        self.args = None
        self.kwargs = None

    def invoke(
        self,
        function: Callable,
        args: Optional[Sequence[Any]] = None,
        kwargs: Optional[Mapping[str, Any]] = None,
    ) -> Self:
        """
        Declares that a certain keypress invokes a certain function with *args & **kwargs

        Note - this doesn't actually invoke any functions

        Args:
            function (Callable): function that user wishes to invoke
            args (Sequence[Any]): args passed as *args into function
            kwargs (Mapping[Any]): kwargs passed as **kwargs into function
        """
        self.function = function
        self.args = args or []
        self.kwargs = kwargs or {}

        return self
    
    def actually_invoke(self) -> Any:
        """
        Actually invoke self.function with *args and **kwargs
        """
        return self.function(*self.args, **self.kwargs)