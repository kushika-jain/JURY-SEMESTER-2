"""Instantiate class Turtle
Demo_1
Pass Demo_1 as an argument to the function repeat_shape( Demo_1)
What to include in function definition?
“”” repeat_shape( ) takes one argument i.e Turtle Object (Demo_1) and iterate the
following sequence of event 15 times forward(50), left(90),forward(50),left(90), forward(50),
left(90),forward(50),left(90) and finally left(30)
"""


import turtle
def repeat_shape(turtle_obj):
for _ in range(15):
turtle_obj.forward(50)
turtle_obj.left(90)
turtle_obj.forward(50)
turtle_obj.left(90)
turtle_obj.forward(50)
turtle_obj.left(90)
turtle_obj.forward(50)
turtle_obj.left(90)
turtle_obj.left(30)
demo_1 = turtle.Turtle()
repeat_shape(demo_1)
turtle.done()