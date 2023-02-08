import PySimpleGUI as sg

submitButton="Submit"
layout=[
    [
        sg.Input(key="-INPUT-"),
        sg.Button(submitButton,key="-SUBMIT-",size=(40,1))
    ]
]
window=sg.Window("Title"
                 ,layout=layout
                 ,resizable=True
                 )


while True:
    event,values=window.read()
    if event == "-SUBMIT-" :
        print(window["-SUBMIT-"].get_size())
        window["-SUBMIT-"].set_size((20,1))
        
    if event == sg.WIN_CLOSED:
        break

window.close()
