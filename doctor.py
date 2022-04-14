import requests
import datetime
#import http.client #this if for python3
#import httplib #python2
#import urllib.request
#import webbrowser
import time
from Tkinter import *
#from Tkinter import messagebox
import tkMessageBox

dummy_commands = {
	"Move right hand" : "Q11",
	"Move left hand" : "Q12",
	"Make a C loop around right hand" : "Q13",
    "Pick up needle with right hand" : "Q14",
	"Pick up needle with left hand" : "Q15",
	"Pick up suture with right hand" : "Q16",
	"Pull suture with both hands to tie a knot" : "Q17"
}

dummy_feedback = {
	"Move right hand" : " Wait till the robot move right hand.",
	"Move left hand" : " You should move to the next step.",
	"Make a C loop around right hand" : " C loop done.",
        "Pick up needle with right hand" : " Robot failed to picked up needle.",
	"Pick up needle with left hand" : " PLease wait until robot respond.",
	"Pick up suture with right hand" : " Do you want move to next step.",
	"Pull suture with both hands to tie a knot" : " Knot done."
}

#timer to keep track of threshold.
def timer(t1,t2):
 t = t2-t1
 return t

# Tactile module will be called if the time exceed the threshold
def tactile_feedback(command):
 global lb2
 global rb_tactile
 lb2 = Label(root,text="Response from Tactile:"+str(dummy_feedback[command]))
 lb2.pack()
 rb_tactile = Button(root,text="Refresh Tactile command", command=refTactile, bg='SlateBlue1')
 rb_tactile.pack()

def refTactile():
 lb2.destroy()
 rb_tactile.destroy()

# This module will send commands to the robot
def command_generator(command,t1):
 if command in dummy_commands :
  #q = "http://localhost:8080/"+ dummy_commands[command]
  q = "http://10.0.0.2:8080/"+ dummy_commands[command]
  #send get req & put res in response variable
  response = requests.get(q)
  threshold = timer(t1,time.time())
  tkMessageBox.showinfo("Success","Status Code:"+str(response.status_code)+" Ok")    
  #content = str(response.content) #puts res inside content variable
  if threshold > 10 : # Check the threshold time if more than 10 seconds.
   tkMessageBox.showwarning("Threshold Exceeded","Robot has exceed the threshold!")
   tactile_feedback(command)
  else :#print(str(response.content))//webbrowser.open(q) #Open to the requested url command
   global rb_robot
   global msg
   global lb1
   lb1 =Label(root,text="The response from Robot:",font=('times',18,'bold'), bg="pink",fg='navy')
   lb1.pack()
   msg = Label(root, text= str(response.content), font=5,bg='pink',fg='purple') #Message
   #msg.config(bg="lightgreen",font=18)
   msg.pack()
   rb_robot= Button(root,text="Refresh Robot command",command=refRobot, bg='SlateBlue1')
   rb_robot.pack()
 else: tkMessageBox.showerror("Wrong Command","Please enter correct command.")

def refRobot():
 msg.destroy()
 lb1.destroy()
 rb_robot.destroy() 

#Get the reponse code
#urladd = urllib.request.urlopen('http://localhost:8080')
#print("result code: " + str(urladd.getcode()))

root = Tk()
root.configure(bg = 'pink')
root.title("Welcome to the Remote Robotic Surgery.")
root.geometry("800x800")
l = Label(root,text="Please enter your command:", font = ('times',20,'bold'), bg='pink',fg='purple')
l.pack()
#getting input from user.
e = Entry(root, width= 800,font=("times",24),bg="misty rose") #Helvetica
e.pack()
img = PhotoImage(file = "la.PNG")
label1 = Label( root, image = img)
label1.place(x = 150, y = 250)
#e.insert(0, "Please enter your command: ")

def refresh_Click():
 myLabel.destroy()
 myButton['state'] = NORMAL

def gui_Click():
 global myLabel
 c = e.get()
 e.delete(0,'end')
 myLabel = Label(root, text="Your command is being send.",bg='pink',fg='violet red')
 myLabel.pack()
 command_generator(c,time.time())
 myButton['state'] = DISABLED
myButton = Button(root, text="Enter", command=gui_Click,bg='sky blue')
myButton.pack()
refresh_Button = Button(root, text="Refresh", command=refresh_Click, bg='SlateBlue1')
refresh_Button.pack()
root.mainloop()
#r = requests.get('http://localhost:8080/Q11',{'Content-Type':'text/html'})
#print(r.text)
#print(post_response.text)

