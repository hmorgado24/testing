
import RPi.GPIO as IO         # we are calling for header file which helps us use GPIO’s of PI
import time                            # we are calling for time to provide delays in program
IO.setwarnings(False)           # do not show any warnings
x=1                                         # integer for storing the delay multiple
IO.setmode (IO.BCM)
IO.setup(5,IO.OUT)             # initialize GPIO5 as an output.
IO.setup(17,IO.OUT)
IO.setup(27,IO.OUT)
IO.setup(22,IO.OUT)
IO.setup(19,IO.IN)              # initialize GPIO19 as an input.
IO.setup(26,IO.IN) 
while 1:                               # execute loop forever
    IO.output(5,1)                 # Step1 go high
    IO.output(22,0)
    for y in range(x):             # sleep for  x*100msec
        time.sleep(0.1)
    IO.output(17,1)               # step2 go high
    IO.output(5,0)
    for y in range(x):
        time.sleep(0.1)         # sleep for  x*100msec
    IO.output(27,1)              #step 3 go high
    IO.output(17,0)
    for y in range(x):
        time.sleep(0.1)         # sleep for  x*100msec
    IO.output(22,1)              #step 4 go high
    IO.output(27,0)
    for y in range(x):
        time.sleep(0.1)                           # sleep for  x*100msec