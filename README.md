
# onkeypress

Allows users to make terminal react to keypresses

# installation

```
pip install onkeypress
```

# quickstart

```python
from onkeypress import while_not_exit, onkeypress, Key

def print_up():
    print("up is pressed")

def print_down():
    print("down is pressed")

while_not_exit(
    onkeypress(Key.UP).call(print_up),
    onkeypress(Key.DOWN).call(print_down),
    exit_key=Key.ENTER,
)
```

| key pressed | printed text |
| ----------- | ------------ |
| Up | up is pressed |
| Down | down is pressed |

If you hit Enter (or Control-C), the program exits

# A slightly harder example using .args(*args) and .kwargs(**kwargs)

```python
from onkeypress import while_not_exit, onkeypress, Key

def myfunc(*args, **kwargs):
    print(f"{args=} {kwargs=}")

while_not_exit(
    onkeypress(Key.UP).call(myfunc).args("up"),
    onkeypress(Key.DOWN).call(myfunc).kwargs(key="down"),
    onkeypress("a").call(myfunc).args("a").kwargs(key="a"),
    onkeypress("s").call(myfunc).args("s", "s").kwargs(key="s", val="s"),
    exit_key=Key.ENTER,
)
```

| key pressed | printed text |
| ----------- | ------------ |
| Up | args=('up',) kwargs={} |
| Down | args=() kwargs={'key': 'down'} |
| a | args=('a',) kwargs={'key': 'a'} |
| s | args=('s', 's') kwargs={'key': 's', 'val': 's'} |

# We can use Key.ALL_OTHERS to match all other keys

```python
from onkeypress import while_not_exit, onkeypress, Key
import random

def print_1_to_5_chars(char: str):
    if char.isalnum():
        print(char * random.randrange(1, 5), end="")
    else:
        print(char, end="")

while_not_exit(
    onkeypress(Key.ALL_OTHERS).call(print_1_to_5_chars),
    exit_key=Key.CONTROL_C,
)
```

Key.ALL_OTHERS match all other keys which were not declared

^ when we type a letter, it randomly repeats itself 1-5 times

# More advanced example: Arrow keys to move "X" around in 6x6 board

```python
from onkeypress import while_not_exit, onkeypress, Key
from copy import deepcopy
from unprint import unprint

BOARD = [["-"]*6 for _ in range(6)]

def print_board(board: list, user_row: int, user_col: int):
    board = deepcopy(board)
    board[user_row][user_col] = "X"
    [print(*row, sep=" ") for row in board]
    print()

print_board(BOARD, 0, 0)

state = {"row":0 , "col": 0}

def handle_keypress(row_diff: int, col_diff: int, state: dict):
    new_row = state["row"] + row_diff
    new_col = state["col"] + col_diff
    if new_row not in range(6) or new_col not in range(6):
        return
    state["row"], state["col"] = new_row, new_col
    unprint(7)
    print_board(BOARD, new_row, new_col)

while_not_exit(
    onkeypress(Key.UP).call(handle_keypress).args(-1, 0, state),
    onkeypress(Key.DOWN).call(handle_keypress).args(1, 0, state),
    onkeypress(Key.LEFT).call(handle_keypress).args(0, -1, state),
    onkeypress(Key.RIGHT).call(handle_keypress).args(0, 1, state),
    exit_key=Key.CONTROL_C,
)
```

Note - try hitting your arrow keys. Notice that your "X" moves around
