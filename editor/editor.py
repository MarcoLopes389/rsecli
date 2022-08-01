from time import sleep
from tkinter import BOTH, RIGHT, Y, X, Text, Tk, ttk
from tkinter.messagebox import showerror, askokcancel

from database.database import get_commands_collection, get_files_collection

files = get_files_collection()
commands_c = get_commands_collection()

def init_editor(text='', edit=False, path='', ip=''):
    def onclose():
        if askokcancel('Save', 'Do you want to save changes?'):
            ip = entry.get()

            commands = text_info.get('1.0', 'end-1c')
            if(ip != '' and commands != ''):
                commands_c.insert_one({
                    'commands': commands, 
                    'ip': ip, 
                    'realtime': False
                })
                print('Script created!')
                root.destroy()
            else:
                showerror('Error', 'You must enter an IP and commands!')
                
        elif askokcancel('Quit', 'Do you want to quit?'):
            root.destroy()
    
    def oncloseedit():
        if askokcancel('Save', 'Do you want to save changes?'):
            ip = entry.get()

            if(ip != ''):
                files.update_one({'path': path, 'ip': ip}, {'$set': {'file': text_info.get('1.0', 'end-1c'), 'ready': True}})
                while True:
                    file = files.find_one({'path': path, 'ip': ip})
                    if file['done']:
                        print('File updated!')
                        files.delete_one({'_id': file['_id']})
                        root.destroy()
                        break
                    else:
                        sleep(1)
            else:
                showerror('Error', 'You must enter an IP!')

        elif askokcancel('Quit', 'Do you want to quit?'):
            root.destroy()
  
    root = Tk() 
    root.geometry("500x350") 
    root.title("Text Editor") 
    root.minsize(height=500, width=350) 
    root.maxsize(height=1000, width=350)
    root.protocol("WM_DELETE_WINDOW", oncloseedit if edit else onclose)
    
    scrollbar = ttk.Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    text_info = Text(root, yscrollcommand=scrollbar.set)
    text_info.pack(fill=BOTH, expand=1)
    text_info.insert('1.0', text)
    
    ttk.Label(root, text="IP:", font='sans-serif').pack()
    entry = ttk.Entry(root)
    entry.pack(fill=X)
    entry.insert(0, ip)
    
    scrollbar.config(command=text_info.yview)

    style = ttk.Style()
    style.configure('TEntry', font=('sans-serif', 12, 'bold'))
    style.configure('TText', font=('sans-serif', 12, 'bold'))
    style.configure('TLabel', font=('sans-serif', 12, 'bold'))
    style.configure('TScrollbar', font=('sans-serif', 12, 'bold'))
    
    root.mainloop()
    