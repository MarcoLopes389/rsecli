from time import time

from database.database import get_commands_collection, get_results_collection
from utils.clear_terminal import clear_terminal
from utils.print_banner import print_banner
from utils.print_registred_ips import print_registred_ips

# area to collections vars
commands = get_commands_collection()
results = get_results_collection()

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
        exec_command(cmd, ip.strip())
        

def exec_command(cmd, ip):
    commands.insert_one({'commands': cmd, 'ip': ip, 'realtime': True})

    init_time = time()
    while True:
        result = results.find_one({'command': cmd, 'ip': ip})

        if time() - init_time > 10:
            raise TimeoutError('The target machine is not responding')

        if result:
            print(result['results'])
            commands.delete_one({'command': cmd, 'ip': ip})
            results.delete_one({'command': cmd, 'ip': ip})
            break
        else:
            continue