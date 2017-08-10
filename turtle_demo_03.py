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
   t.forward (50)
   t.goto (25, 0)
   t.right (90)
   t.forward (100)

drawT()

t.goto(0,75)

drawT()
