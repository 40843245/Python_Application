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
        print(window["-SUBMIT-"].Size)
        
        # At Runtime AttributeError since the Button has NO attribute size
        #print(window["-SUBMIT-"].size())
        
        # At Runtime AttributeError since the Button has NO method size()
        #print(window["-SUBMIT-"].size)
        
    if event == sg.WIN_CLOSED:
        
        break

window.close()
