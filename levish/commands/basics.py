from os import system as _exec
from platform import system as _system

def clear(args):
    if _system() == "Windows":
        _exec("cls")
    else:
        _exec("clear")