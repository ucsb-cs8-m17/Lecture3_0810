import turtle

t = turtle.Turtle()

# Invoke the shape method,
#  passing the string "turtle"
#  as a parameter

t.shape("turtle") 

# A better approach... now we can draw many Ts
# But this is very repetitive.. it works, but...??!?!?

def drawT(width,height):
   '''
   draw a T
   assume turtle facing east (0), and leave it facing east
   assume pen is down
   no assumptions about position.
   '''
   t.forward (width)
   t.backward (width/2)
   t.right (90)
   t.forward (height)
   t.left(90)

# CONTINUE TO GENERALIZE...
# 

def moveToNewPlaceAndDrawT(x,y,width,height=100):
  t.up()
  t.goto(x,y)   
  t.down()
  drawT(width,height)

moveToNewPlaceAndDrawT(-200,0,40,50)

moveToNewPlaceAndDrawT(-100,0,40,50)

moveToNewPlaceAndDrawT(0,0,40,50)

moveToNewPlaceAndDrawT(-200,-100,50)

moveToNewPlaceAndDrawT(-100,-100,50)

moveToNewPlaceAndDrawT(0,-100,50)

