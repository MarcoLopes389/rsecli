from time import sleep
from database.database import get_files_collection
from editor.editor import init_editor

def call_edition():
    ip = input('IP: ')
    path = input('Path: ')
    text = ''
    get_files_collection().insert_one({'path': path, 'ip': ip, 'status': 'pending', 'edit': True, 'ready': False})
    while True:
        file = get_files_collection().find_one({'path': path, 'ip': ip})
        if file['status'] == 'done':
            text = file['file']
            break
        else:
            print('Waiting for file...')
            sleep(1)

    init_editor(ip=ip, path=path, edit=True, text=text)