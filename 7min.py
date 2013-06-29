#!/usr/bin/python

import os
import time

def countdown(sec,activity,tick=True):

    for t in reversed(range(sec)):
        print str(t) + " " + activity
        if(tick):
            os.system('aplay histicks.wav 2> /dev/null &')
        time.sleep(1)

def do_workout():
    activities = ['Jumping Jacks','Wall Sit','Pushup','Situp','Step Up On Chair','Squat','Triceps Dips','Plank','High-Knees Running','Lunge','Pushup and Rotation','Side-Plank']
    for act in activities:
        countdown(10,"REST -- Next up: " + act,tick=False)
        countdown(30,act)

do_workout()

