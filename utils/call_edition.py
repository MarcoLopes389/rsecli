from time import sleep, time
from database.database import get_files_collection
from editor.editor import init_editor

def call_edition():
    ip = input('IP: ')
    path = input('Path: ')
    text = ''

    get_files_collection().insert_one({'path': path, 'ip': ip, 'status': 'pending', 'edit': True, 'ready': False})

    init_time = time()

    while True:
        file = get_files_collection().find_one({'path': path, 'ip': ip})

        if time() - init_time > 30:
            raise TimeoutError('The target machine is not responding')

        if file['status'] == 'done':
            text = file['file']
            break
        else:
            print('Waiting for file...')
            sleep(1)

    init_editor(ip=ip, path=path, edit=True, text=text)