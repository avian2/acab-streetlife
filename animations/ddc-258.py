# 258
import acabsl
import random
import time

cs = [[255,255,000,000,000,255],[000,255,255,255,000,000],[000,000,000,255,255,255]]

def rc():
  return random.randint(0,5)

def rid():
    return [random.randint(0,8),random.randint(0,6)]


while 1:
    acabsl.speedfade(0,0,0,0,0,1000)
    acabsl.speedfade(0,1,0,0,0,1000)
    acabsl.speedfade(1,0,0,0,0,1000)
    acabsl.speedfade(1,1,0,0,0,1000)
    acabsl.speedfade(2,0,0,0,0,1000)
    acabsl.speedfade(2,1,0,0,0,1000)
    acabsl.speedfade(3,0,0,0,0,1000)
    acabsl.speedfade(3,1,0,0,0,1000)
    acabsl.speedfade(4,0,0,0,0,1000)
    acabsl.speedfade(4,1,0,0,0,1000)
    acabsl.speedfade(5,0,0,0,0,1000)
    acabsl.speedfade(5,1,0,0,0,1000)
    acabsl.speedfade(6,1,0,0,0,1000)
    acabsl.speedfade(6,0,0,0,0,1000)
    acabsl.speedfade(7,0,0,0,0,1000)
    acabsl.speedfade(7,1,0,0,0,1000)
    acabsl.speedfade(0,2,0,0,0,1000)
    acabsl.speedfade(0,3,0,0,0,1000)
    acabsl.speedfade(1,2,0,0,0,1000)
    acabsl.speedfade(1,3,0,0,0,1000)
    acabsl.speedfade(2,2,0,0,0,1000)
    acabsl.speedfade(2,3,0,0,0,1000)
    acabsl.speedfade(3,2,0,0,0,1000)
    acabsl.speedfade(3,3,0,0,0,1000)
    acabsl.speedfade(4,2,0,0,0,1000)
    acabsl.speedfade(4,3,0,0,0,1000)
    acabsl.speedfade(5,2,0,0,0,1000)
    acabsl.speedfade(5,3,0,0,0,1000)
    acabsl.speedfade(6,3,0,0,0,1000)
    acabsl.speedfade(6,2,0,0,0,1000)
    acabsl.speedfade(7,2,0,0,0,1000)
    acabsl.speedfade(7,3,0,0,0,1000)
    acabsl.speedfade(0,4,0,0,0,1000)
    acabsl.speedfade(0,5,0,0,0,1000)
    acabsl.speedfade(1,5,0,0,0,1000)
    acabsl.speedfade(1,4,0,0,0,1000)
    acabsl.speedfade(2,4,0,0,0,1000)
    acabsl.speedfade(2,5,0,0,0,1000)
    acabsl.speedfade(3,4,0,0,0,1000)
    acabsl.speedfade(3,5,0,0,0,1000)
    acabsl.speedfade(4,4,0,0,0,1000)
    acabsl.speedfade(4,5,0,0,0,1000)
    acabsl.speedfade(5,4,0,0,0,1000)
    acabsl.speedfade(5,5,0,0,0,1000)
    acabsl.speedfade(6,4,0,0,0,1000)
    acabsl.speedfade(7,4,0,0,0,1000)
    acabsl.speedfade(6,5,0,0,0,1000)
    acabsl.speedfade(7,5,0,0,0,1000)
    time.sleep(1.0)

    acabsl.speedfade(5,2,0,0,255,453)
    acabsl.speedfade(5,3,0,0,255,453)
    acabsl.speedfade(6,3,0,0,255,453)
    time.sleep(0.5)
    acabsl.speedfade(3,2,0,0,255,453)
    acabsl.speedfade(3,3,0,0,255,453)
    acabsl.speedfade(4,2,0,0,255,453)
    acabsl.speedfade(4,3,0,0,255,453)
    time.sleep(0.5)
    acabsl.speedfade(5,2,0,0,0,453)
    acabsl.speedfade(5,3,0,0,0,453)
    acabsl.speedfade(6,3,0,0,0,453)
    acabsl.speedfade(1,3,0,0,255,453)
    acabsl.speedfade(2,2,0,0,255,453)
    acabsl.speedfade(2,3,0,0,255,453)
    time.sleep(0.5)
    acabsl.speedfade(3,2,0,0,0,453)
    acabsl.speedfade(3,3,0,0,0,453)
    acabsl.speedfade(4,2,0,0,0,453)
    acabsl.speedfade(4,3,0,0,0,453)
    acabsl.speedfade(0,2,0,0,127,225)
    acabsl.speedfade(0,3,0,0,127,225)
    acabsl.speedfade(1,2,0,0,127,225)
    acabsl.speedfade(0,0,0,0,127,225)
    acabsl.speedfade(0,1,0,0,127,225)
    acabsl.speedfade(1,0,0,0,127,225)
    time.sleep(0.5)
    acabsl.speedfade(1,1,0,0,127,225)
    acabsl.speedfade(2,0,0,0,127,225)
    acabsl.speedfade(2,1,0,0,127,225)
    acabsl.speedfade(1,3,0,0,127,225)
    acabsl.speedfade(2,2,0,0,127,225)
    acabsl.speedfade(2,3,0,0,127,225)
    acabsl.speedfade(1,4,0,0,127,225)
    acabsl.speedfade(2,4,0,0,127,225)
    acabsl.speedfade(2,5,0,0,127,225)
    time.sleep(0.5)
    acabsl.speedfade(0,4,0,0,127,225)
    acabsl.speedfade(0,5,0,0,127,225)
    acabsl.speedfade(1,5,0,0,127,225)
    time.sleep(0.5)

    acabsl.speedfade(5,2,255,0,0,453)
    acabsl.speedfade(5,3,255,0,0,453)
    acabsl.speedfade(6,3,255,0,0,453)
    time.sleep(0.5)
    acabsl.speedfade(3,2,255,0,0,453)
    acabsl.speedfade(3,3,255,0,0,453)
    acabsl.speedfade(4,2,255,0,0,453)
    acabsl.speedfade(4,3,255,0,0,453)
    time.sleep(0.5)
    acabsl.speedfade(1,3,255,0,127,453)
    acabsl.speedfade(2,2,255,0,127,453)
    acabsl.speedfade(2,3,255,0,127,453)
    acabsl.speedfade(5,2,0,0,0,453)
    acabsl.speedfade(5,3,0,0,0,453)
    acabsl.speedfade(6,3,0,0,0,453)
    acabsl.speedfade(3,0,0,0,127,225)
    acabsl.speedfade(3,1,0,0,127,225)
    acabsl.speedfade(4,0,0,0,127,225)
    acabsl.speedfade(4,1,0,0,127,225)
    acabsl.speedfade(3,4,0,0,127,225)
    acabsl.speedfade(3,5,0,0,127,225)
    acabsl.speedfade(4,4,0,0,127,225)
    acabsl.speedfade(4,5,0,0,127,225)
    time.sleep(0.5)
    acabsl.speedfade(0,0,127,0,127,225)
    acabsl.speedfade(0,1,127,0,127,225)
    acabsl.speedfade(1,0,127,0,127,225)
    acabsl.speedfade(0,2,127,0,127,225)
    acabsl.speedfade(0,3,127,0,127,225)
    acabsl.speedfade(1,2,127,0,127,225)
    time.sleep(0.5)
    acabsl.speedfade(1,1,127,0,127,225)
    acabsl.speedfade(2,0,127,0,127,225)
    acabsl.speedfade(2,1,127,0,127,225)
    acabsl.speedfade(1,4,127,0,127,225)
    acabsl.speedfade(2,4,127,0,127,225)
    acabsl.speedfade(2,5,127,0,127,225)
    acabsl.speedfade(1,3,127,0,127,225)
    acabsl.speedfade(2,2,127,0,127,225)
    acabsl.speedfade(2,3,127,0,127,225)
    time.sleep(0.5)
    acabsl.speedfade(0,4,127,0,127,225)
    acabsl.speedfade(0,5,127,0,127,225)
    acabsl.speedfade(1,5,127,0,127,225)
    time.sleep(1.0)

    acabsl.speedfade(5,2,0,255,0,435)
    acabsl.speedfade(5,3,0,255,0,435)
    acabsl.speedfade(6,3,0,255,0,435)
    time.sleep(0.5)
    acabsl.speedfade(3,2,127,255,127,435)
    acabsl.speedfade(3,3,127,255,127,435)
    acabsl.speedfade(4,2,127,255,127,435)
    acabsl.speedfade(4,3,127,255,127,435)
    acabsl.speedfade(5,0,0,0,127,225)
    acabsl.speedfade(5,1,0,0,127,225)
    acabsl.speedfade(6,1,0,0,127,225)
    acabsl.speedfade(6,0,127,0,127,225)
    acabsl.speedfade(7,0,127,0,127,225)
    acabsl.speedfade(7,1,127,0,127,225)
    acabsl.speedfade(6,2,127,0,127,225)
    acabsl.speedfade(7,2,127,0,127,225)
    acabsl.speedfade(7,3,127,0,127,225)
    acabsl.speedfade(5,4,0,0,127,225)
    acabsl.speedfade(5,5,0,0,127,225)
    acabsl.speedfade(6,4,0,0,127,225)
    acabsl.speedfade(7,4,0,0,127,225)
    acabsl.speedfade(6,5,0,0,127,225)
    acabsl.speedfade(7,5,0,0,127,225)
    time.sleep(0.5)
    acabsl.speedfade(1,3,127,255,127,435)
    acabsl.speedfade(2,2,127,255,127,435)
    acabsl.speedfade(2,3,127,255,127,435)
    acabsl.speedfade(5,2,0,0,0,435)
    acabsl.speedfade(5,3,0,0,0,435)
    acabsl.speedfade(6,3,0,0,0,435)
    time.sleep(0.5)
    acabsl.speedfade(3,2,0,0,0,435)
    acabsl.speedfade(3,3,0,0,0,435)
    acabsl.speedfade(4,2,0,0,0,435)
    acabsl.speedfade(4,3,0,0,0,435)
    time.sleep(0.5)
    acabsl.speedfade(5,2,55,0,55,225)
    acabsl.speedfade(5,3,55,0,55,225)
    acabsl.speedfade(6,3,55,0,55,225)
    acabsl.speedfade(1,3,0,0,0,435)
    acabsl.speedfade(2,2,0,0,0,435)
    acabsl.speedfade(2,3,0,0,0,435)
    acabsl.speedfade(6,0,63,0,63,225)
    acabsl.speedfade(7,0,63,0,63,225)
    acabsl.speedfade(7,1,63,0,63,225)
    acabsl.speedfade(6,2,63,0,63,225)
    acabsl.speedfade(7,2,63,0,63,225)
    acabsl.speedfade(7,3,63,0,63,225)
    time.sleep(0.5)
    acabsl.speedfade(3,2,64,0,64,117)
    acabsl.speedfade(3,3,64,0,64,117)
    acabsl.speedfade(4,2,64,0,64,117)
    acabsl.speedfade(4,3,64,0,64,117)
    acabsl.speedfade(5,0,0,0,0,225)
    acabsl.speedfade(5,1,0,0,0,225)
    acabsl.speedfade(6,1,0,0,0,225)
    acabsl.speedfade(5,4,0,0,0,225)
    acabsl.speedfade(5,5,0,0,0,225)
    acabsl.speedfade(6,4,0,0,0,225)
    acabsl.speedfade(7,4,0,0,0,225)
    acabsl.speedfade(6,5,0,0,0,225)
    acabsl.speedfade(7,5,0,0,0,225)
    acabsl.speedfade(1,1,0,0,127,225)
    acabsl.speedfade(2,0,0,0,127,225)
    acabsl.speedfade(2,1,0,0,127,225)
    acabsl.speedfade(0,4,0,0,127,225)
    acabsl.speedfade(0,5,0,0,127,225)
    acabsl.speedfade(1,5,0,0,127,225)
    time.sleep(0.5)
    acabsl.speedfade(5,2,0,0,0,117)
    acabsl.speedfade(5,3,0,0,0,117)
    acabsl.speedfade(6,3,0,0,0,117)
    acabsl.speedfade(6,0,0,0,0,117)
    acabsl.speedfade(7,0,0,0,0,117)
    acabsl.speedfade(7,1,0,0,0,117)
    acabsl.speedfade(6,2,0,0,0,117)
    acabsl.speedfade(7,2,0,0,0,117)
    acabsl.speedfade(7,3,0,0,0,117)
    time.sleep(0.5)
    acabsl.speedfade(3,0,0,0,0,225)
    acabsl.speedfade(3,1,0,0,0,225)
    acabsl.speedfade(4,0,0,0,0,225)
    acabsl.speedfade(4,1,0,0,0,225)
    acabsl.speedfade(1,1,0,0,127,225)
    acabsl.speedfade(2,0,0,0,127,225)
    acabsl.speedfade(2,1,0,0,127,225)
    acabsl.speedfade(1,4,0,0,127,225)
    acabsl.speedfade(2,4,0,0,127,225)
    acabsl.speedfade(2,5,0,0,127,225)
    acabsl.speedfade(3,4,0,0,0,225)
    acabsl.speedfade(3,5,0,0,0,225)
    acabsl.speedfade(4,4,0,0,0,225)
    acabsl.speedfade(4,5,0,0,0,225)
    acabsl.speedfade(1,3,0,0,127,225)
    acabsl.speedfade(2,2,0,0,127,225)
    acabsl.speedfade(2,3,0,0,127,225)
    time.sleep(0.5)
    acabsl.speedfade(0,0,0,0,127,225)
    acabsl.speedfade(0,1,0,0,127,225)
    acabsl.speedfade(1,0,0,0,127,225)
    acabsl.speedfade(0,2,0,0,127,225)
    acabsl.speedfade(0,3,0,0,127,225)
    acabsl.speedfade(1,2,0,0,127,225)
    time.sleep(0.5)
    acabsl.speedfade(1,1,0,0,0,225)
    acabsl.speedfade(2,0,0,0,0,225)
    acabsl.speedfade(2,1,0,0,0,225)
    acabsl.speedfade(1,4,0,0,0,225)
    acabsl.speedfade(2,4,0,0,0,225)
    acabsl.speedfade(2,5,0,0,0,225)
    acabsl.speedfade(0,4,0,0,0,225)
    acabsl.speedfade(0,5,0,0,0,225)
    acabsl.speedfade(1,5,0,0,0,225)
    acabsl.speedfade(3,2,0,0,0,225)
    acabsl.speedfade(3,3,0,0,0,225)
    acabsl.speedfade(4,2,0,0,0,225)
    acabsl.speedfade(4,3,0,0,0,225)
    time.sleep(0.5)
    acabsl.speedfade(0,0,0,0,0,225)
    acabsl.speedfade(0,1,0,0,0,225)
    acabsl.speedfade(1,0,0,0,0,225)
    acabsl.speedfade(0,2,0,0,0,225)
    acabsl.speedfade(0,3,0,0,0,225)
    acabsl.speedfade(1,2,0,0,0,225)
    time.sleep(0.5)
    acabsl.speedfade(1,3,0,0,0,225)
    acabsl.speedfade(2,2,0,0,0,225)
    acabsl.speedfade(2,3,0,0,0,225)
    time.sleep(2.0)

    acabsl.speedfade(1,3,0,255,0,435)
    acabsl.speedfade(2,2,0,255,0,435)
    acabsl.speedfade(2,3,0,255,0,435)
    time.sleep(0.5)
    acabsl.speedfade(3,2,0,255,0,435)
    acabsl.speedfade(3,3,0,255,0,435)
    acabsl.speedfade(4,2,0,255,0,435)
    acabsl.speedfade(4,3,0,255,0,435)
    time.sleep(0.5)
    acabsl.speedfade(5,2,0,255,0,435)
    acabsl.speedfade(5,3,0,255,0,435)
    acabsl.speedfade(6,3,0,255,0,435)
    acabsl.speedfade(1,3,0,0,0,435)
    acabsl.speedfade(2,2,0,0,0,435)
    acabsl.speedfade(2,3,0,0,0,435)
    time.sleep(0.5)
    acabsl.speedfade(3,2,0,0,0,435)
    acabsl.speedfade(3,3,0,0,0,435)
    acabsl.speedfade(4,2,0,0,0,435)
    acabsl.speedfade(4,3,0,0,0,435)
    time.sleep(0.5)
    acabsl.speedfade(5,2,0,0,0,435)
    acabsl.speedfade(5,3,0,0,0,435)
    acabsl.speedfade(6,3,0,0,0,435)
    time.sleep(2.0)
