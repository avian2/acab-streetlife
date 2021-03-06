This is the software behind the ACAB wall.
You can get our software on github: https://github.com/muccc/acab-streetlife

## Writing animations

Animations are created as python scripts which run on the
computer controlling the installation.

The wall has 14x6 Pixels.

The setup looks like this: (x,y)

    (0,0), (1,0) ... (12,0), (13,0)
    (0,1), (1,1) ... (12,1), (13,1)
      .      .          .       .
      .      .          .       .
      .      .          .       .
    (0,4), (1,4) ... (12,4), (13,4)
    (0,5), (1,5) ... (12,5), (13,5)

Use the acabsl library from our git repository to create your own scripts.

It provides two methods:

    acabsl.send(x,y,r,g,b,time,w):

        Send a new color to pixel (<x>,<y>) on wall no <w>. If you omit 'w', the
        server will choose a wall for you, when the script gets executed.

        'r','g','b' are in [0-255]

        time is in seconds:
            'time'=0  => Instant update
            'time'>0  => Fade to the new color in <time> seconds


    acabsl.update():

        Use this command if you want to use double buffering.
        Use it once before you do your first acabsl.send() call.
        Then use it every time you want new commands to be executed.
      
        This command only affects walls which have been modified since the
        last call to acabsl.update()

It also provides the following constants:

    acabsl.WALLSIZEX:
        Size of a wall in X direction

    acabsl.WALLSIZEY:
        Size of a wall in X direction

    acabsl.NOOFWALLS:
        Number of walls available

Example:

    import acabsl
    
    #enable double buffering
    acabsl.update()
    
    # let every pixel of the wall chosen by the server fade to red
    for x in range(acabsl.WALLSIZEX):
        for y in range(range.WALLSIZEY):
            acabsl.send(x,y,255,0,0,500)
    '''
    # let every pixel of every wall fade to red
    for wall in range(acabsl.NOOFWALLS):
        for x in range(acabsl.WALLSIZEX):
            for y in range(range.WALLSIZEY):
                acabsl.send(x,y,255,0,0,500,wall)
    '''

    #execute all fades at once
    acabsl.update()


Have a look at the scripts in the animations directory for examples. We also have audio examples ;)

## Test animations using simulator

A simulator is available for local animation testing. To use it you have to install the pygame library. The command to install pygame on Debian based systems is:

    apt-get install python-pygame

Execute the startsimulation file to run a simulation of the walls on your computer:

    ./startsimulation

Optionally you can modify the size of the simulator window by adding a resize factor. The follow example will reduce the simulator to half size:

    ./startsimulation 0.5

It will open two windows with simulated ACAB walls.

Then execute the script you wrote to display it on the simulator.

Send new scripts via a pull request to our github account: https://github.com/muccc/acab-streetlife and we will put them
into rotation on the walls.

## Send animation to real wall

There are two ways to send your animation to the real wall

###From the ep14-wireless network
Supply your script with the following arguments: '--host=172.16.0.90 --port=6002'

###Alternative
You need to connect to the WLAN with SSID and Password "AllColorsAreBeautiful".

Supply your script with the following arguments: '--host=192.168.0.100 --port=6002'


Generally speaking: you can always edit the IP-address in acabsl.py to match the IP and port you want to stream to. This eliminates the need to provide the parameters above.

Have fun :)

