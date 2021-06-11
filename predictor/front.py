from tkinter import *

window = Tk()
window.geometry("800x500")
window.wm_title("Audio-Recogniser")
pane = Frame(window)
Label(pane, text = 'Press the button to recognise music', font =('Verdana', 18)).pack(side = TOP, pady = 10)
b1 = Button(pane, text = 'Audio-Recognizer',font =('Verdana', 12),compound = LEFT,padx=10,pady=10,
            bg='grey').pack(side = TOP)


pane.pack(fill = BOTH, expand = True)
pane.mainloop()
