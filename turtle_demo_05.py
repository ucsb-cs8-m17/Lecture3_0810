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

t.up()
t.goto(-200,0)
t.down()
drawT()

t.up()
t.goto(-100,0)
t.down()
drawT()

t.up()
t.goto(0,0)
t.down()
drawT()

t.up()
t.goto(100,0)
t.down()
drawT()

t.up()
t.goto(200,0)
t.down()
drawT()
