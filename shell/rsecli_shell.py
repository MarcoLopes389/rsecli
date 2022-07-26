from help import show_create_help, show_get_help, show_run_help
from shell.normal_shell import exec_command, normal_shell
from utils.clear_terminal import clear_terminal
from utils.create_script import create_script
from shell.help import show_help
from repo.delete_results import delete_results
from repo.get_all_results import get_all_results
from utils.print_banner import print_banner
from utils.print_registred_ips import print_registred_ips
from utils.solicite_file import solicite_file

def rsecli_shell():
    clear_terminal()
    print_banner(type='shell')
    while True:
        print('$ ', end='')
        cmd = input()
        if cmd == 'exit':
            print('bye bye!')
            break
        elif cmd == 'help':
            show_help()
        elif cmd == 'create':
            show_create_help()
        elif ' ' in cmd and cmd.split(' ')[0] == 'create':
            if(cmd.split(' ')[1] == 'script'):
                create_script()
            else:
                print('Unknown create option')
        elif cmd == 'clear':
            clear_terminal()
        elif cmd == 'get':
            show_get_help()
        elif ' ' in cmd and cmd.split(' ')[0] == 'get':
            if(cmd.split(' ')[1] == 'ips'):
                print_registred_ips()
            elif(cmd.split(' ')[1] == 'results'):
                get_all_results()
            elif cmd.split(' ')[1] == 'file':
                solicite_file()
            else:
                print('Unknown get option')
                show_get_help()
        elif cmd == 'clear-results':
            delete_results()
        elif cmd == 'realtime':
            normal_shell()
        elif cmd == 'run':
            show_run_help()
        elif ' ' in cmd and cmd.split(' ')[0] == 'run':
            if(len(cmd.split(' ')) == 3):
                exec_command(cmd.split(' ')[2], cmd.split(' ')[1])
            else:
                show_run_help()
        else:
            print('Unknown command: ' + cmd)