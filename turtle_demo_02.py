import turtle

t = turtle.Turtle()

# Invoke the shape method,
#  passing the string "turtle"
#  as a parameter

t.shape("turtle") 

# Try making several Ts
# What I want is T T T
# Is that what I will get?

for i in range(3):
  t.forward (50)
  t.goto (25, 0)
  t.right (90)
  t.forward (100)
