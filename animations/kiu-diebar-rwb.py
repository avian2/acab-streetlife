import acabsl
import random
import time

c =	[ [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
          [2,2,2,1,2,1,2,2,1,2,2,2,0,2,2,2,2,2,2,2,2,2,2,2],
          [2,2,2,1,2,2,2,1,2,1,2,2,0,2,2,2,2,2,2,2,2,2,2,2],
          [2,2,1,1,2,1,2,1,1,1,2,2,0,0,2,2,2,0,0,2,2,0,0,2],
          [2,1,2,1,2,1,2,1,2,2,2,2,0,2,0,2,0,2,0,2,0,2,0,2],
          [2,1,1,1,2,1,2,1,1,1,2,2,0,0,0,2,0,0,0,2,0,2,2,2]
	]

idx = 0
cx = 0
tick = 0.25
acabsl.update()
while 1:

    for x in range(0,16):
	cx = x + idx;
	if (cx > 23):
	    cx = cx - 24
	    
	for y in range(0,6):	    
	    col = c[y][cx]
	    
	    if (col == 0):
		acabsl.send(x,y,255,0,0,tick/1.5)

	    if (col == 1):
		acabsl.send(x,y,255,255,255,tick/1.5)

	    if (col == 2):
		acabsl.send(x,y,0,0,0,tick/1.5)
    
    acabsl.update()
    time.sleep(tick)
    
    idx = idx + 1
    if (idx > 23):
	idx = 0
