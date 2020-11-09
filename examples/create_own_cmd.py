from levish import Shell

# define your command functions with a *args argument
def hello(*args):
    print("what's up?")

# create a new shell instance
sh = Shell("leviSh")

# add our defined command function
sh.add_command(hello, description="print hello")

# run the shell
sh.run()