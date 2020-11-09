from levish import Shell
from levish.commands import clear, ls

sh = Shell("SimpleShell", show_cwd=True, prefix="/> ", figlet=True, figlet_font="slant")

sh.add_command("ls", ls)
sh.add_command("cls", clear)

sh.run()
