from levish import Shell


def cmd_stars(args):
    for i in range(1, args[0]):
        print("*"*int(i))


myshell = Shell("MyShell")
myshell.add_command("stars", cmd_stars, "prints any amounts of stars")
myshell.run()