from tkinter import BOTH, RIGHT, Y, X, Entry, Label, Scrollbar, Text, Tk, messagebox
from tkinter import messagebox

from database.database import get_commands_collection, get_files_collection

def init_editor(text='', edit=False, path='', ip=''):
    def onclose():
        if messagebox.askokcancel('Save', 'Do you want to save changes?'):
            ip = entry.get()
            commands = text_info.get('1.0', 'end-1c')
            if(ip != '' and commands != ''):
                get_commands_collection().insert_one({
                    'commands': commands, 
                    'ip': ip, 
                    'realtime': False
                })
                print('Script created!')
                root.destroy()
            else:
                messagebox.showerror('Error', 'You must enter an IP and commands!')
        elif messagebox.askokcancel('Quit', 'Do you want to quit?'):
            root.destroy()
    
    def oncloseedit():
        if messagebox.askokcancel('Save', 'Do you want to save changes?'):
            ip = entry.get()
            if(ip != ''):
                get_files_collection().update_one({'path': path, 'ip': ip}, {'$set': {'file': text_info.get('1.0', 'end-1c'), 'ready': True}})
                print('File updated!')
                root.destroy()
            else:
                messagebox.showerror('Error', 'You must enter an IP!')
        elif messagebox.askokcancel('Quit', 'Do you want to quit?'):
            root.destroy()
  
    root = Tk() 
    root.geometry("500x350") 
    root.title("Text Editor") 
    root.minsize(height=500, width=350) 
    root.maxsize(height=1000, width=350)
    root.protocol("WM_DELETE_WINDOW", oncloseedit if edit else onclose)
    
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y) 
    
    text_info = Text(root, yscrollcommand=scrollbar.set)
    text_info.pack(fill=BOTH, expand=1)
    text_info.insert('1.0', text)
    
    Label(root, text="IP:", font='sans-serif').pack()
    entry = Entry(root)
    entry.pack(fill=X)
    
    scrollbar.config(command=text_info.yview)
    
    root.mainloop()
    