# levish: Create your own shell 🐢

## Installation

Install levish using PIP:

```txt
pip install levish
```

## How to use

### Example Code

```python
from levish import Shell

def cmd_hello(args):
    print("hello friend!")

myshell = Shell("MyShell")
mshell.add_command("hello", cmd_hello, "greets you")
myshell.run()
```

### Output

```txt
[>] hello
hello friend!
```
