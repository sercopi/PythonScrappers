import tkinter 
from PIL import Image, ImageTk
from tkinter import ttk
ventana=tkinter.Tk()
ventana.geometry("600x600")
#label = tkinter.Label(ventana,text="hola mundo",bg="blue")
#label.pack(fill=tkinter.BOTH,expand=True)
labelTwo = tkinter.Label(ventana)

def saludo():
    print("hola")
buttonOne = tkinter.Button(ventana, text="click here",padx=50,pady=30,bg="blue",command=saludo)
def setText():
    labelTwo["text"]=textFieldOne.get()
buttonTwo=tkinter.Button(ventana,text="get Text",padx=10,pady=5,bg="green",command=setText)
textFieldOne= tkinter.Entry(ventana,font="Helvetica 15")
def disableButtonTwo(buttonTwo):
    if (buttonTwo["state"]=="normal"):
        buttonTwo["state"]="disabled"
    else:
        buttonTwo["state"]="normal"
buttonFour=tkinter.Button(ventana,text="disable getText",padx=10,pady=5,bg="lightblue",command=lambda:disableButtonTwo(buttonTwo))
textShown=True
def manageText(textShown,labelTwo):
    if (textShown):
        labelTwo.pack_forget()
        textShown=False
    else:
        labelTwo.pack()
        textShown=True
buttonThree=tkinter.Button(ventana,bg="pink" ,width=10,height=5,text="clear text",command= lambda: manageText(textShown,labelTwo))
comboBoxOne = ttk.Combobox(ventana,state="readonly")
comboBoxOne["values"]=["one","two","three"]
textFieldOne.grid(column=2,row=0)
buttonOne.grid(column=2,row=4)
buttonTwo.grid(column=2,row=5)
buttonFour.grid(column=2,row=6)
labelTwo.grid(column=2,row=7)
buttonThree.grid(column=2,row=1)
comboBoxOne.grid(column=3,row=3)
load = Image.open("parrot.png")
image = load.resize((200, 200), Image.ANTIALIAS)
render = ImageTk.PhotoImage(image)
img = tkinter.Label(ventana, image=render)
img.image = render
img.grid(column=7,row=0)
ventana.mainloop()