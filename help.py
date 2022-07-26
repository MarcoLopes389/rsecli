def show_help():
    print('Usage: index.py [-h]')
    print('\t-h\t\t\tPrint this help message')
    print('\t--shell\t\t\tStart a normal shell')
    print('\t--shell-realtime\tStart a realtime shell')
    print('\t--ip\t\t\tThe ip of the target machine')
    print('\t--command\t\tThe command to execute')
    print('\t--create-script\t\tCreate a new script')
    print('\t--get-all-results\tGet all registred results of commands')
    print('\trun\t\t\tExecute the command')
    return True

def show_run_help():
    print('Usage: run [options]')
    print('\tip\tThe ip of the target machine')
    print('\tcommand\tThe command to execute')

def show_get_help():
    print('Usage: get [option]')
    print('\tips\tGet all registred ips')
    print('\tresults\tGet all registred results of commands')
    print('\tfile\tGet a file from other machine')

def show_create_help():
    print('Usage: create [option]')
    print('\tscript\t\tCreate a new script')

def show_delete_help():
    print('Usage: delete [option]')
    print('\tresults\tDelete all registred results of commands')