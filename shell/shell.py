from shell.rsecli_shell import rsecli_shell
from shell.normal_shell import normal_shell

def init_shell(realtime=False):
    if realtime:
        normal_shell()
    else:
        rsecli_shell()