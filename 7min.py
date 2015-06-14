#!/usr/bin/python

import os
import time

def countdown(sec,activity,tick=True):

    for t in reversed(range(sec)):
        print str(t) + " " + activity
        if(tick):
            os.system(wave_player + ' histicks.wav 2> /dev/null &')
        time.sleep(1)

def do_workout(intervaltime=30,rest=10):
    activities = ['Jumping Jacks','Wall Sit','Pushup','Situp','Step Up On Chair','Squat','Triceps Dips','Plank','High-Knees Running','Lunge','Pushup and Rotation','Side-Plank']
    for act in activities:
        countdown(rest,"REST -- Next up: " + act,tick=False)
        countdown(intervaltime,act)

if os.system('which aplay') == 0:
    wave_player = 'aplay'
elif os.system('which afplay') == 0:
    wave_player = 'afplay'


###############################################################################
###############################################################################
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='The 7 minute Workout')
    parser.add_argument('-t','--intervaltime',help='Do each interval for this many seconds',default=30)
    parser.add_argument('-r','--rest',help='rest for this many seconds',default=10)

    args = parser.parse_args()
    do_workout(int(args.intervaltime),int(args.rest))