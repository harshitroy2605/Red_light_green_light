import cv2
import numpy as np
import time
from time import sleep
from tkinter import *
from tkinter import messagebox
import threading
import os


def detect(): 
    delay=20*1   ###for 1 minutes delay 
    close_time=time.time()+delay
    cap = cv2.VideoCapture(0)


    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    while cap.isOpened():
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            print(contour)
            if cv2.contourArea(contour) < 900:
                print("in frame")
                continue
            messagebox.showinfo("showinfo", "You are Dead")
            os._exit(1)
            
        cv2.imshow("feed", frame1)
        frame1 = frame2
        ret, frame2 = cap.read()

        if time.time()>close_time:
            break

        key=cv2.waitKey(1)
        if key==ord('q'):
          break

    cv2.destroyAllWindows()
    cap.release()
    #cap=detect().cap
    #return cap
    main_loop_func()


def finsh_game():
    messagebox.showinfo("showinfo", "You Won")
    os._exit(1)

def end_Gui():
    root1=Tk()
    root1.geometry("500x600")

    b3=Button(root1,text="open file",command=finsh_game)
    b3.place(x=120,y=10)

    root1.mainloop()


def main_loop_func():
    while True:
        sleep(20)
        detect()


def first_func():
    root.destroy()
    t=threading.Thread(target=end_Gui)
    t.start()
    print("first function running")
    detect()
    

root=Tk()
root.geometry("500x600")

b3=Button(root,text="open file",command=first_func)
b3.place(x=120,y=10)



root.mainloop()


    
    
