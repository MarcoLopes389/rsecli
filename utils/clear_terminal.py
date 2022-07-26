from os import system
from platform import system as system_name

def clear_terminal():
    if(system_name() == 'Windows'):
        system('cls')
    if(system_name() == 'Linux'):
        system('clear')