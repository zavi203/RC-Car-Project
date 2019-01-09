#import evdev
#import robot class
from evdev import InputDevice, categorize, ecodes
from gpiozero import Robot

#Create Robot class
robot = Robot(left = (7, 8), right = (9, 10))

#Button code variables and speed variable
up = 103
down = 108
right = 106
left = 105
esc = 1
space = 57
speed = 0.4

#Prints the input device information
print(gamepad)

#evdev automatically creates a loop
for event in gamepad.read_loop():
if event.type == ecodes.EV_KEY:
    if event.value == 1:
        if event.code == up:
            robby.forward(speed)
            print(‘Move forward’)
	    elif event.code == down:
            robby.backward(speed)
            print(‘Move backward’)
      elif event.code == right:
            robby.right(speed)
            print(‘Turn right’)
      elif event.code == left:
            robby.left(speed)
            print(‘Turn left’)
      elif event.code == esc:
            robby.stop()
            print(‘Stop!’)
        elif event.code == space:
            if speed == 1:
	            speed = 0.2
               print(‘Maximum speed reached, back to 0.2’)
