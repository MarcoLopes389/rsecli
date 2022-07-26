from database.database import get_commands_collection
from utils.clear_terminal import clear_terminal
from utils.print_banner import print_banner
from utils.print_registred_ips import print_registred_ips

def create_script():
    print_registred_ips()
    ip = input('First, enter the ip of the target machine: ')
    clear_terminal()

    commands = ''
    print_banner('script')

    while True:
        try:
            command = input("")
            commands += command + '\n'
        except KeyboardInterrupt:
            break
    
    print('Your script is:')
    print(commands)

    sure = input('Are you sure you want to create this script? [y/n] ')
    if sure == 'y':
        print('Script created!')
        get_commands_collection().insert_one({'commands': commands, 'ip': ip, 'realtime': False})
    elif sure == 'n':
        remake = input('Want to remake this? [y/n]')
        if remake == 'y':
            commands = create_script()
        elif remake == 'n':
            print('bye bye!')
            return


    return commands