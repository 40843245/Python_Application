import tkinter
from tkinter import *

if __name__ == '__main__':

    def test():
        root = tkinter.Tk()
        
        #Runtime Error
        #root.minsize=(20,20)
        #root.maxsize=(20,20)
        
        root.minsize(200,200)
        root.maxsize(200,200)
        
        def CloseWindow(root=root):
            print("The quit Button is clicked.")
            root.destroy()
            
        def doit(root=root):
            d = tkinter.simpledialog.Dialog(parent=root,title=[
                              "This is a test dialog.  "
                              "Would this have been an actual dialog, "
                              "the buttons below would have been glowing "
                              "in soft pink light.\n"
                              "Do you believe this?",
                         ["Yes", "No", "Cancel"]]
                         )
            
            print(dir(d))
            print("----------------------")
            print(tkinter.simpledialog.askinteger("Spam", "Egg count", initialvalue=12*12))
            print(tkinter.simpledialog.askfloat("Spam", "Egg weight\n(in tons)", minvalue=1,
                           maxvalue=100))
            print(tkinter.simpledialog.askstring("Spam", "Egg label"))
        t = tkinter.Button(root, text='Test', command=doit)
        t.pack()
        
        q = tkinter.Button(root, text='Quit', command=CloseWindow)
        q.pack()
        root.mainloop()

    test()