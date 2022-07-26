def print_banner(type='shell'):
    if type == 'script':
        print('>>> Remote command line executor. Version 1.0')
        print('Enter create mode, press Ctrl+C to finish and save.')
    elif type == 'shell':
        print('>>> Remote command line executor. Version 1.0')
        print('Enter help for more information.')
        print('Enter exit to exit.')
    elif type == 'realtime':
        print('>>> Remote command line executor. Version 1.0')
        print('Warning: This is a realtime shell. All commands will be executed in realtime.')
        print('Enter help for more information.')
        print('Enter exit to exit.')