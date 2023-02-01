from tkinter import *
from PIL import Image,ImageTk
import os,sys
    
root = Tk()
main = ImageTk.PhotoImage(Image.open('static/Loading_Screen.png'))

width = int(root.winfo_screenwidth()/2-200)
height = int(root.winfo_screenheight()/2-175)

root.geometry("400x350+%s+%s" %(width,height))
root.overrideredirect(True)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

background_image = Label(root,image=main)
background_image.place(x=0, y=0, relwidth=1, relheight=1)

root.update()
root.after(3000)
root.destroy()
import Main_Window
root.mainloop()
