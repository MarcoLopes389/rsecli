def show_cli_help():
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
    print('Usage: run [ip] [command]')
    print('\tip\tThe ip of the target machine')
    print('\tcommand\tThe command to execute')

def show_run_cli_help():
    print('Usage: run --ip [ip] --command [command]')
    print('\t--ip\tThe ip of the target machine')
    print('\t--command\tThe command to execute')

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
    print('\t\tresults\t\tDelete all registred results of commands')

help_message = """
exit                   Exit the shell
help                   Print this help message
create      [option]   Create a new thing
             script    Create a script
get         [option]   Get a thing
             ips       Get all registred ips
             results   Get all registred results of commands
             file      Get a file
delete      [option]   Delete a thing
             results   Delete all registred results of commands
             file      Delete a file
             ips       Delete all registred ips
clear                  Clear the terminal
run [ip] [command]     Execute the command
             ip        The ip of the target machine
             command   The command to execute
realtime               Start the realtime shell
"""

def rsecli_shell_help():
    print(help_message)
    return True