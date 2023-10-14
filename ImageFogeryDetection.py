from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile
import tkinter.messagebox as messagebox
import cv2
import tkinter as tk
window=Tk()
window.geometry("1920x1080")
window.title("IMAGE FORGERY DETECTION")
window.configure(bg='#8fbc8f')
image=Image.open("PSG.jpeg")
resized=image.resize((250,250),Image.LANCZOS)
new_pic=ImageTk.PhotoImage(resized)

def new_window1():
    window.destroy()
    window1=Tk()
    window1.geometry("1920x1000")
    window1.configure(bg='#8fbc8f')
    window1.title("IMAGE FORGERY DETECTION")
    l1=Label(window1,text="Image Forgery Detection",font=("Angsana New",40,"bold"),bg="#8fbc8f").place(relx=0.5,rely=0.15,anchor="n")
    image1=Image.open("project.png")
    resized1=image1.resize((300,250),Image.LANCZOS)
    new_pic1=ImageTk.PhotoImage(resized1)
    l2=Label(window1,image=new_pic1).place(relx=0.5,rely=0.45,anchor="center")
    button1=Button(window1,text="Open File",font=("Georgia",20),bg="black",fg="white",activebackground="#8fbc8f",command=img_to_text_converter).place(relx=0.5,rely=0.75,anchor="s")
   
    window1.mainloop()
    

data=""

def img_to_text_converter():
        global data,Img,Img1,img1,img,G,window1,button1,button2,tk
        path=filedialog.askopenfilename()
        fath=filedialog.askopenfilename()
        
        

       
        if not path:
            data = "YOU DIDN'T SELECT FIRST IMAGE"
            messagebox.showinfo("ERROR!",data)
        elif not fath:
            data = "YOU DIDN'T SELECT SECOND IMAGE"
            messagebox.showinfo("ERROR!",data)
        elif not path and fath:
            data = "YOU HAVE SELECTED NOTHING"
            messagebox.showerror("ERROR!",data)
        else:
            Img=cv2.imread(path,-1)
            Img1=cv2.imread(fath,-1)
            img=cv2.calcHist([Img], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
            img1=cv2.calcHist([Img1],[0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
            G=cv2.compareHist(img,img1,cv2.HISTCMP_CORREL)

            if G ==1.0:
                data = "They are the same images"
            else:
                data = "Image Forgery Is Done"
            messagebox.showinfo("Information",data)


#place function here is used to place the label at the required place.

l1=Label(window,text="PSG Institute of Technology and Applied Research",font=("Angsana New",40,"bold"),bg="#8fbc8f").place(relx=0.5,rely=0.15,anchor="n")
l2=Label(window,image=new_pic).place(relx=0.5,rely=0.5,anchor="center")

button=Button(window,text="START",font=("Georgia",20),bg="black",fg="white",activebackground="#8fbc8f",command=new_window1).place(relx=0.5,rely=0.80,anchor="s")


window.mainloop()
