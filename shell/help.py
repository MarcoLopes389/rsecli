help_message = """
exit              Exit the shell
help              Print this help message
create [option]   Create a new thing
        script    Create a script
get    [option]   Get a thing
        ips       Get all registred ips
        results   Get all registred results of commands
        file      Get a file
clear             Clear the terminal
clear-results     Delete all registred results of commands
run    [options]  Execute the command
        ip        The ip of the target machine
        command   The command to execute
"""

def show_help():
    print(help_message)
    return True