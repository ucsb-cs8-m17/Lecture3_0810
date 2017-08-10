import turtle

t = turtle.Turtle()

# Invoke the shape method,
#  passing the string "turtle"
#  as a parameter

t.shape("turtle") 

# A better approach... now we can draw many Ts
# But this is very repetitive.. it works, but...??!?!?

def drawT():
   '''
   draw a T
   assume turtle facing east (0), and leave it facing east
   assume pen is down
   no assumptions about position.
   '''
   t.forward (50)
   t.backward (25)
   t.right (90)
   t.forward (100)
   t.left(90)

# CONTINUE TO GENERALIZE...
#  The old version had y hard-coded at 0
#  The new version makes that a parameter

def moveToNewPlace(x,y):
  t.up()
  t.goto(x,y)   
  t.down()
  drawT()

moveToNewPlace(-200,0)

moveToNewPlace(-100,0)

moveToNewPlace(0,0)

moveToNewPlace(-200,-100)

moveToNewPlace(-100,-100)

moveToNewPlace(0,-100)

