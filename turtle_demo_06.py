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

# REFACTORED...
#  put the part that's the same into the function def
#  put the parts that's different as parameter to function call

def moveToNewPlace(x):
  t.up()
  t.goto(x,0)   
  t.down()
  drawT()

moveToNewPlace(-200)

moveToNewPlace(-100)

moveToNewPlace(0)

moveToNewPlace(100)

moveToNewPlace(200)

