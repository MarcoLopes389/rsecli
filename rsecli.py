from sys import argv
from help import show_create_help, show_delete_help, show_get_help, show_cli_help, show_run_cli_help
from repo.delete_ips import delete_ips
from shell.normal_shell import exec_command

from shell.shell import init_shell
from utils.create_script import create_script
from repo.delete_results import delete_results
from utils.print_registred_ips import print_registred_ips
from utils.print_results import print_results

ip = ''
command = ''

def main(argv=argv):
    if len(argv) <= 1:
        show_cli_help()
        return

    for i in range(1, len(argv)):
        match argv[i]:
            case '-h' | '--help' | 'help':
                show_cli_help()
                return

            case '--shell' | 'shell':
                init_shell()
                return

            case '--shell-realtime' | 'shell-realtime':
                init_shell(realtime=True)
                return

            case 'create' | '-c' | '--create':
                if len(argv) != i+2:
                    show_create_help()
                    return
                match argv[i+1]:
                    case 'script':
                        create_script()
                        return
                    case _:
                        show_create_help()
                        return
                        
            case 'get' | '-g' | '--get':
                if len(argv) != i+2:
                    show_get_help()
                    return
                match argv[i+1]:
                    case 'results':
                        print_results()
                    case 'ips':
                        print_registred_ips()
                    case _:
                        show_get_help()
                return

            case 'run' | '-r' | '--run':
                for j in range(1, len(argv)):
                    match argv[j]:
                        case '--ip':
                            ip = argv[j+1]
                        case '--command':
                            command = argv[j+1]

                if(ip == '' or command == ''):
                    show_run_cli_help()
                    return
                else:
                    exec_command(command, ip) 

            case 'delete' | '-d' | '--delete':
                if len(argv) != i+2:
                    show_delete_help()
                    return
                match argv[i+1]:
                    case 'results':
                        delete_results()
                    case 'ips':
                        delete_ips()
                    case _:
                        show_delete_help()
                return

if __name__ == '__main__':
    main()