
# onkeypress

Allows users to make terminal react to keypresses

# installation

```
pip install onkeypress
```

# quickstart

```python
from onkeypress import while_not_exit, onkeypress, Key

def func1(key):
    print(f"{key} was pressed")

def func2(key, num):
    print(f"{key} was pressed.", num)

while_not_exit(
    onkeypress(Key.UP).invoke(func1, ["up"]),
    onkeypress(Key.DOWN).invoke(func1, ["down"]),
    onkeypress("a").invoke(func2, ["a", 100]),
    exit_key=Key.ENTER,
)
```

When you run this, your terminal awaits your keypresses
- if you hit ArrowUp,
    - the `func1` function is called with the args `["up"]`
    - this is equivalent to calling `func1("up")`
    - hence, `"up was pressed"` is printed

- if you hit ArrowDown,
    - the `func1` function is called with the args `["down"]`
    - this is equivalent to calling `func1("down")`
    - hence, `"down was pressed"` is printed

- if you hit "a",
    - the `func2` function is called with the args `["a", 100]`
    - this is equivalent to calling `func2("a", 100)`
    - hence, `"a was pressed. 100"` is printed

- if you hit Enter, this function ends, and your terminal goes back to normal

