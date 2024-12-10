from src.onkeypress import while_not_exit, onkeypress, Key

def func(*args, **kwargs):
    print(f"{args=} {kwargs=}")

while_not_exit(
    onkeypress(Key.UP).invoke(func, ["up"]),
    onkeypress(Key.DOWN).invoke(func, ["down"]),
    onkeypress("a").invoke(func, ["a!!"]),
    onkeypress("s").invoke(func, ["s!!"]),
    exit_key=Key.ENTER,
)
