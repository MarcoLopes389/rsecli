
from help import rsecli_shell_help, show_create_help, show_delete_help, show_edit_help, show_get_help, show_run_help
from repo.delete_ips import delete_ips
from editor.editor import init_editor
from shell.normal_shell import exec_command, normal_shell
from utils.call_edition import call_edition
from utils.clear_terminal import clear_terminal
from repo.delete_results import delete_results
from utils.print_banner import print_banner
from utils.print_registred_ips import print_registred_ips
from utils.print_results import print_results
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
            rsecli_shell_help()
        elif cmd == 'create':
            show_create_help()
        elif ' ' in cmd and cmd.split(' ')[0] == 'create':
            if(cmd.split(' ')[1] == 'script'):
                init_editor()
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
                print_results()
            elif cmd.split(' ')[1] == 'file':
                solicite_file()
            else:
                print('Unknown get option')
                show_get_help()
        elif cmd == 'delete':
            show_delete_help()
        elif ' ' in cmd and cmd.split(' ')[0] == 'delete':
            if(cmd.split(' ')[1] == 'ips'):
                delete_ips()
            elif(cmd.split(' ')[1] == 'results'):
                delete_results()
            else:
                print('Unknown delete option')
                show_delete_help()
        elif cmd == 'realtime':
            normal_shell()
        elif cmd == 'run':
            show_run_help()
        elif ' ' in cmd and cmd.split(' ')[0] == 'run':
            if(len(cmd.split(' ')) == 3):
                exec_command(cmd.split(' ')[2], cmd.split(' ')[1])
            else:
                show_run_help()
        elif cmd == 'edit':
            show_edit_help()
        elif ' ' in cmd and cmd.split(' ')[0] == 'edit':
            if(cmd.split(' ')[1] == 'file'):
                call_edition()
            else:
                print('Unknown edit option')
        else:
            print('Unknown command: ' + cmd)
            rsecli_shell_help()