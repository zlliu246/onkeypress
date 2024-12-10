
# onkeypress

Allows users to make terminal react to keypresses

# installation

```
pip install onkeypress
```

# quickstart

```python
from onkeypress import while_not_exit, onkeypress, Key

def func(key):
    print(f"{key} was pressed")

while_not_exit(
    onkeypress(Key.UP).invoke(func, ["up"]),
    onkeypress(Key.DOWN).invoke(func, ["down"]),
    onkeypress("a").invoke(func, ["a!!"]),
    onkeypress("s").invoke(func, ["s!!"]),
    exit_key=Key.ENTER,
)
```

^ after running this, your terminal now waits for your keypresses
- if you hit ArrowUp, it prints "up was pressed"
- if you hit ArrowDown, it prints "down was pressed"
- if you hit "a", it prints "a was pressed"
- if you hit "s", it prints "s was pressed"
- if you hit Enter, this function ends
