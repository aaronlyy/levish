from levish import Shell
import pyfiglet

def cmd_stars(args):
    for i in range(1, args[0]):
        print("*"*int(i))

myshell = Shell("MyShell")
myshell.add_command("stars", cmd_stars, "prints any amounts of stars")

print(pyfiglet.figlet_format("leviSH"))

myshell.run()