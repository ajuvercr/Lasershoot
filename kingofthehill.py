import time
import datetime
import MySQLdb
import csv
import os
import signal
import subprocess
import RPi.GPIO as GPIO

def handle1() {
    
}

def handle2() {
    
}

events = {
    K_1: handle1
    K_2: handle2
}

for event in pygame.event.get():
    if event.type == KEYDOWN:
        events[event.key]()