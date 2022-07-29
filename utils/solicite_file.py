from os import mkdir
from time import sleep
from os.path import basename, join, isdir

from database.database import get_files_collection

def solicite_file():
    path = input('Enter path: ')
    get_files_collection().insert_one({'path': path, 'status': 'pending', 'edit': False})
    while True:
        file = get_files_collection().find_one({'path': path, 'edit': False})
        if file['status'] == 'done':
            if not isdir('out'):
                mkdir('out')
            saved = open(join('out', basename(file['path'])), 'wb')
            saved.write(file['file'])
            saved.close()
            get_files_collection().delete_one({'_id': file['_id']})
            print('File saved!')
            break
        else:
            print('Waiting for file...')
            sleep(1)