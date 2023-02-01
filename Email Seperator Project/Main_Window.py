from tkinter import *
from PIL import Image,ImageTk
import os,sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

def action():
    values = Input_Field.get()
    if values.find("@") == -1 or (values.find('.com') == -1 and values.find('.pk') == -1):
        Input_Field.config(fg='red')
        Result.config(text="")
    else:
        if values.find(".com") != -1:
            n = values.find(".com")
        elif values.find(".pk") != -1:
            n = values.find(".pk")

        Input_Field.config(fg='black')

        name = values[0:values.find("@")]
        after_sign = values[values.find("@")+1:n]
        last = values[n:]

        final_text = name,'-',after_sign,'-',last
        Result.config(text=final_text)
root = Tk()

main = ImageTk.PhotoImage(Image.open('E:\AH\Python Projects\Email Seperator Project\static\Main_Window.png'))
button = ImageTk.PhotoImage(Image.open('E:\AH\Python Projects\Email Seperator Project\static\Submit.png'))

width = int(root.winfo_screenwidth()/2-250)
height = int(root.winfo_screenheight()/2-225)

root.geometry("500x450+%s+%s" %(width,height))
root.title("Email Scraping")

background_image = Label(root,image=main)
background_image.place(x=0, y=0, relwidth=1, relheight=1)

Submit = Button(root,image=button,bd=0,highlightthickness=0,command=action)
Submit.place(x=200,y=252)

Input_Field = Entry(root,bd=0,width=28,font=("Verdana 15"))
Input_Field.place(x=60,y=186,height=40)

Result = Label(root,text="",bg='white',font=("Verdana 15"))
Result.place(x=60,y=362)
root.mainloop()