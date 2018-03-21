import sys, pygame
import time
import datetime
import MySQLdb
import csv
import os
import signal
import subprocess
import RPi.GPIO as GPIO

def handle1():
    print("1 ingedrukt")

def handle2():
    print("2 ingedrukt")

events = {
    KP_1: handle1
    KP_2: handle2
}

for event in pygame.event.get():
    if event.type == KEYDOWN:
        events[event.key]()