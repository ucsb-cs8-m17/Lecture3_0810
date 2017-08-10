import turtle

t = turtle.Turtle()

# Invoke the shape method,
#  passing the string "turtle"
#  as a parameter

t.shape("turtle") 

# One approach to T T T
# Does not work:
#  Assumptions about where we start,
#  Which way we are facing
#  Whether pen is up or down

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

drawT()

t.up()
t.goto(75,0)
t.down()
drawT()
