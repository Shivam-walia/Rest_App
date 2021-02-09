# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:44:34 2020

@author: CSIO
"""
"http://127.0.0.1:8080/api/documentation"
from flask_restplus import Api,Resource
from flask import Flask, Blueprint,request
import serial.tools.list_ports
import cv2
import time
import os 
import datetime
import math


#%%

MyApp=Flask(__name__)
api=Api(MyApp)

#%%
capture=cv2.VideoCapture(0)
ST=0.1
Slide=1
callib=4


        
@api.route("/Radio5")
class Radio5m(Resource):
    def get(self):
        global ST
        Radio5=Stepsize(0.05)
        ST=Radio5
        return ("Radio 5μm [[Info]]:Step Size Button  "+str(ST)+"Button Is Pressed")
"""*************Establishing Connection to start processing*****************"""

@api.route('/Connect')
class Connect(Resource):
    def get(self):
        global ser
        print('[Info]:Search...Com Port...')
        ports = serial.tools.list_ports.comports(include_links=False)
        for port in ports :
            print('Find port '+ port.device)
        ser = serial.Serial()
        if ser.isOpen():
            ser.close()
        ser = serial.Serial(port.device, 115200, timeout=1)
        ser.flushInput()
        ser.flushOutput()
        
        
        print('Connect ' + ser.name)
        
        print("[Info]:Setting Up the Microscope")
        wline='$H'
        print(wline)
        wline = wline.strip()
        ser.write((wline + '\n').encode())
        if ser.isOpen():
            print("Sending" + wline)
            ser.flushInput()
            ser.flushOutput()
        

        
        return ("Success", ser.name),200
            
        

#%%  
if __name__=='__main__':
    MyApp.run(debug=True)
        
        
        

        

        
        
        
        
        
        
        
        
