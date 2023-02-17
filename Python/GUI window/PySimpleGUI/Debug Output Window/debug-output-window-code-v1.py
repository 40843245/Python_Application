import time

import PySimpleGUI as sg

for i in range(100):
    sg.Print(i)

time.sleep(10)    
sg.easy_print_close()
