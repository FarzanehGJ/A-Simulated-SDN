# A Simulated SDN – Environment for Remote Robotic Surgery
This repository contains the python and nodejs sorce cods of our Tactile project.
<br/>
<br/> Course: Cloud Networking and Service Provisioning – ENCS 691K / Fall 2021
<br/> Course Instructor: Professor Roch Glitho - a part of research prject colaborating with Zayed University, Dubai, United Arab Emirates
<br/> Team Members: Farzaneh Ghasemi Javid, Zarin Tasnim
<br/>
<br/>
### 1. Introduction
The project consists of designing and implementing a very simple remote robotic surgery
system which consists of a simulated surgeon console module, a simulated robot module, and
a simulated tactile learner module. The messages will be exchanged through an SDN network.
<br/>
<br/>
### 2. Description
The simulated console will be used to send dummy commands to the simulated robot module,
and the robot module will send back dummy feedbacks. If the feedbacks do not reach the
surgeon console within a set threshold, the surgeon console will consult the tactile learner
which will give back the predicted feedback. The tactile learner should be pre-configured for
simplicity sake, although machine learning algorithms are used in real life. The SDN
simulator could be used to give higher priority to some of surgeries if we assume that the
same network is used by different surgeons to perform operations on different patients.
<br/>
<br/>
### How to use these files:
<br/>Please download the mytopo.py, la.PNG, doctor.py and robot.js files and put them in the machine that Mininet emulator runs in it. Then you can run the mytopo.py file to create a mininet network. After that, open the xterm of Docotr and Robot hosts. First run the robot.js in xterm of Robot to start your server, then run the docotor.py file to open the application of the doctor side. 
<br/> In the doctor application, you can write the following command to see the result returning from the robot side:
<br/>
<br/>"Move right hand" : "Q11",
<br/>"Move left hand" : "Q12",
<br/>"Make a C loop around right hand" : "Q13",
<br/>"Pick up needle with right hand" : "Q14",
<br/>"Pick up needle with left hand" : "Q15",
<br/>"Pick up suture with right hand" : "Q16",
<br/>"Pull suture with both hands to tie a knot" : "Q17"
<br/>
<br/> This project is going to improve ...
