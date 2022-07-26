from os import mkdir
from time import sleep
from os.path import basename, join, isdir

from database.database import get_files_collection

def solicite_file():
    path = input('Enter path: ')
    get_files_collection().insert_one({'path': path, 'status': 'pending'})
    while True:
        file = get_files_collection().find_one({'path': path})
        if file['status'] == 'done':
            if not isdir('out'):
                mkdir('out')
            saved = open(join('out', basename(file['path'])), 'wb')
            saved.write(file['file'])
            saved.close()
            print('File saved!')
            break
        else:
            print('Waiting for file...')
            sleep(1)