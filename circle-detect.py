from tkinter import *
from tkinter import filedialog , messagebox
import os
from PIL import ImageTk , Image
import cv2
import matplotlib.pyplot as plt
import numpy as np



                 # ----  Functions ---- 


def find_circles(filename):
    
    image = cv2.imread(filename , 3)
    
    # blur and gr
    
    img_blured = cv2.medianBlur(cv2.imread(filename, 0),5)
    
    crc = cv2.HoughCircles(img_blured, cv2.HOUGH_GRADIENT, 1, 20,param1=200, param2=30, minRadius=0, maxRadius=250)

    if crc is not None:
        crc = np.uint16(np.around(crc))
        for i in crc[0, :]:
            #centers
            cv2.circle(image, (i[0], i[1]), 1, (0, 0, 255), 2)
            #outers
            cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
    #cropping the circles out of the image
    mask = np.full((img_blured.shape[0], img_blured.shape[1]), 0, dtype=np.uint8)

    for j in crc[0, :]:
        cv2.circle(mask, (j[0], j[1]), j[2], (205, 114, 101), 2)
        
    cv2.imshow('       Detected Circles', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

        
        
        
def open_img_file():
        
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=(("png images", ".png"), ("all files", "*.*")))


    find_circles(filename)

def try_example():

    find_circles("exp.png")
        
    

                          # ----  GUI ---- 


root = Tk ()
root.title("Circle Detect")
root.geometry("600x500")        
        
canvas = Canvas ( root, height=60, width=80 )
canvas.pack()

frame_up = Frame ( root, bg='#BAD4FF' )
frame_up.place ( relx=0.1, rely=0.01, relwidth=0.8, relheight=0.1 )
    
frame_bott = Frame ( root, bg='#D7CDEB' )
frame_bott.place ( relx=0.2, rely=0.25, relwidth=0.6, relheight=0.5 )
    

    
lbl = Label(root)
lbl.pack()
app_label = Label ( frame_up, bg="#BAD4FF", text=(" ○ ◌ Circle Detection ◌ ○ "), font="Verdana 15 " )
app_label.pack ( padx=10, pady=10 )
    
    
load = PhotoImage ( file="exp.png" )
photoimage = load.subsample ( 32, 32 )
    
btn_try = Button ( frame_bott, text="   Try Example Image ",image=photoimage, bg="#BAD4FF", compound=LEFT,command=try_example )
btn_try.pack ( padx=10, pady=10, side=LEFT )
btn_load = Button ( frame_bott, text="               Load Image [PNG]            ", bg="#BAD4FF", compound=LEFT , command=open_img_file)
btn_load.pack ( padx=10, pady=10, side=RIGHT )   



root.mainloop ()
