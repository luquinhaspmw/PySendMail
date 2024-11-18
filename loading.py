import os
import sys
from termcolor import colored
from time import sleep

def clear_screen():
    if os.name == 'nt':
        os.system('cls')  
    else:
        os.system('clear') 

def load():
    clear_screen()
    string_start = "============= Starting ============="
    string_start_center = ""
    
    
    supports_color = sys.stdout.isatty() and os.name != 'nt'

    try:
        if supports_color:
            string_start_center = string_start.center(os.get_terminal_size().columns)
        else:
            string_start_center = string_start
    except (OSError, ValueError):
        pass
    
    if supports_color:
        print(colored(string_start_center, 'green'))
    else:
        print(string_start_center)
        
    sleep(1)
    text = "                            PyMailSend"
    text_complete = ''
    for c in range(len(text)):
        sleep(0.1)
        text_complete = text_complete + text[c]
        clear_screen()
        if supports_color:
            print(colored(text_complete, 'magenta', attrs=['bold']))
        else:
            print(text_complete)
    clear_screen()
    if supports_color:
        print(colored(text_complete, "magenta", attrs=['bold']))
    else:
        print(text_complete)
