# 117
import acabsl
import random
import time

cs = [[255,255,000,000,000,255],[000,255,255,255,000,000],[000,000,000,255,255,255]]

def rc():
  return random.randint(0,5)

def rid():
    return [random.randint(0,8),random.randint(0,6)]


while 1:
    acabsl.send(0,0,0,0,0)
    acabsl.send(0,1,0,0,0)
    acabsl.send(0,2,0,0,0)
    acabsl.send(0,3,0,0,0)
    acabsl.send(0,4,0,0,0)
    acabsl.send(0,5,0,0,0)
    acabsl.send(1,0,0,0,0)
    acabsl.send(1,1,0,0,0)
    acabsl.send(1,2,0,0,0)
    acabsl.send(1,3,0,0,0)
    acabsl.send(1,4,0,0,0)
    acabsl.send(1,5,0,0,0)
    acabsl.send(2,0,0,0,0)
    acabsl.send(2,1,0,0,0)
    acabsl.send(2,2,0,0,0)
    acabsl.send(2,3,0,0,0)
    acabsl.send(2,4,0,0,0)
    acabsl.send(2,5,0,0,0)
    acabsl.send(3,0,0,0,0)
    acabsl.send(3,1,0,0,0)
    acabsl.send(3,2,0,0,0)
    acabsl.send(3,3,0,0,0)
    acabsl.send(3,4,0,0,0)
    acabsl.send(3,5,0,0,0)
    acabsl.send(4,0,0,0,0)
    acabsl.send(4,1,0,0,0)
    acabsl.send(4,2,0,0,0)
    acabsl.send(4,3,0,0,0)
    acabsl.send(4,4,0,0,0)
    acabsl.send(4,5,0,0,0)
    acabsl.send(5,0,0,0,0)
    acabsl.send(5,1,0,0,0)
    acabsl.send(5,2,0,0,0)
    acabsl.send(5,3,0,0,0)
    acabsl.send(5,4,0,0,0)
    acabsl.send(5,5,0,0,0)
    acabsl.send(6,0,0,0,0)
    acabsl.send(6,1,0,0,0)
    acabsl.send(6,2,0,0,0)
    acabsl.send(6,3,0,0,0)
    acabsl.send(6,4,0,0,0)
    acabsl.send(6,5,0,0,0)
    acabsl.send(7,0,0,0,0)
    acabsl.send(7,1,0,0,0)
    acabsl.send(7,2,0,0,0)
    acabsl.send(7,3,0,0,0)
    acabsl.send(7,4,0,0,0)
    acabsl.send(7,5,0,0,0)
    time.sleep(5.0)
