from levish import Shell

def cmd_hello(args):
    print("hello friend!")

myshell = Shell("MyShell")
myshell.add_command("hello", cmd_hello, "greets you")
myshell.run()