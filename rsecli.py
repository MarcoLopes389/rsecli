from sys import argv
from help import show_create_help, show_delete_help, show_get_help, show_help, show_run_help
from shell.normal_shell import exec_command

from shell.shell import init_shell
from utils.create_script import create_script
from repo.delete_results import delete_results
from repo.get_all_results import get_all_results
from utils.print_registred_ips import print_registred_ips

ip = ''
command = ''

def main(argv=argv):
    if len(argv) <= 1:
        show_help()
        return

    for i in range(1, len(argv)):
        match argv[i]:
            case '-h' | '--help' | 'help':
                show_help()
                return
            case '--shell' | 'shell':
                init_shell()
                return
            case '--shell-realtime' | 'shell-realtime':
                init_shell(realtime=True)
                return
            case 'create':
                match argv[i+1]:
                    case 'script':
                        create_script()
                        return
                    case _:
                        show_create_help()
            case 'get':
                if len(argv) != i+2:
                    show_get_help()
                    return
                match argv[i+1]:
                    case 'results':
                        get_all_results()
                        return
                    case 'ips':
                        print_registred_ips()
                        return
            case 'run':
                for j in range(1, len(argv)):
                    match argv[j]:
                        case '--ip':
                            ip = argv[j+1]
                        case '--command':
                            command = argv[j+1]
                        case _:
                            show_run_help()

                exec_command(command, ip)   
            case 'delete':
                if len(argv) != i+2:
                    show_delete_help()
                    return
                match argv[i+1]:
                    case 'results':
                        delete_results()
                        return
            case '':
                show_help()
                return

if __name__ == '__main__':
    main()