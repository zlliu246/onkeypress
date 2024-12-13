from src.onkeypress import while_not_exit, onkeypress, Key

def print_up():
    print("up is pressed")

def print_down():
    print("down is pressed")

while_not_exit(
    onkeypress(Key.UP).call(print_up),
    onkeypress(Key.DOWN).call(print_down),
    exit_key=Key.ENTER,
)