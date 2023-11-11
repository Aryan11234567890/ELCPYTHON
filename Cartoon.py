#hi guys, Aryan here!!!
import numpy as np
import cv2
import tkinter as tk
from tkinter import *
import easygui
import os
class Result:
    def upload(self):
        self.pathImage=easygui.fileopenbox()
        self.ELC(self.pathImage)
    def save(self):
        newName = "cartoonizedImage"
        path1 = os.path.dirname(self.pathImage)
        extension=os.path.splitext(self.pathImage)[1]
        path = os.path.join(path1,newName+extension)
        cv2.imwrite(path, self.resized2)
        I = "Image saved by name " + newName +" at "+ path
        tk.messagebox.showinfo(title=None, message=I)
    def ELC(self,pathImage,):
        ORIGINALIMAGE = cv2.imread(pathImage)
        if ORIGINALIMAGE is None:
            print("No Image Found")
        ReSizedOG = cv2.resize(ORIGINALIMAGE, (960, 640))
        cv2.imshow('ORIGINALIMAGE', ReSizedOG)
        data = np.float32(ORIGINALIMAGE).reshape((-1, 3))
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
        _, label, center = cv2.kmeans(data, 8, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        print(center)
        result = center[label.flatten()]
        result = result.reshape(ORIGINALIMAGE.shape)
        ReSized = cv2.resize(result, (960, 540))
        #cv2.imshow('result', ReSized)
        gray = cv2.cvtColor(ORIGINALIMAGE, cv2.COLOR_BGR2GRAY)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)
        ReSized1 = cv2.resize(edges, (960, 540))
        # cv2.imshow('edges', ReSized1)
        blurred = cv2.medianBlur(result, 3)
        cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
        self.resized2 = cv2.resize(cartoon, (960, 540))
        cv2.imshow('final', self.resized2)
r = Result() #Instance of Result created
top=tk.Tk() #UI creation
top.geometry('480x480')
top.title('Cartoonize Your Desired Image !')
top.configure(background='teal')
label=Label(top,background='#00B2EE', font=('ariel',20,'italic'))
upload=Button(top,text="Cartoonize!!!!",command=r.upload,padx=50,pady=10)#Button creation
upload.configure(background='white', foreground='black',font=('calibri',10,'italic'))
upload.pack(side=TOP,pady=50)
save=Button(top,text="Save cartoon image",command=r.save,padx=100,pady=20)#Button creation
save.configure(background='yellow', foreground='black',font=('times new roman',10,'bold'))
save.pack(side=TOP,pady=50)
top.mainloop()