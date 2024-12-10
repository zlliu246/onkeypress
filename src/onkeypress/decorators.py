from typing import Callable, Any
from functools import wraps

from toggle_cbreak import cbreak_off, cbreak_on

def handle_cbreak_and_exceptions(
    function: Callable
) -> Callable:
    """
    At start of function, turn on cbreak mode
    At the end, always turn off cbreak mode
    """
    @wraps(function)
    def wrapper_function(*args, **kwargs) -> Any:
        try:
            cbreak_on()
            return function(*args, **kwargs)
        
        except Exception as e:
            raise e
        
        finally:
            cbreak_off()
        
    return wrapper_function
