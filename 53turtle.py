import turtle
# tur=turtle.Turtle()
# square 
# for i in range(5):
#     tur.forward(50)
#     tur.right(90)

# import turtle
# tur=turtle.Turtle()
# for i in range(50):
#     tur.forward(50)
#     tur.right(144)
# turtle.done()

# import turtle
# tur=turtle.Turtle()
# for i in range(6):
#     tur.forward(50)
#     tur.right(144)
# turtle.done()

#C8A2C8
import turtle
  
# taking input for the radius of the circle
r = int(input("Enter the radius of the circle: "))
  
# taking the input for the color
col = input("Enter the color name or hex value of color(# RRGGBB): ")
  
t = turtle.Turtle()
# set the fillcolor
t.fillcolor(col)
  
# start the filling color
t.begin_fill()
  
# drawing the circle of radius r
t.circle(r)
  
# ending the filling of the color
# t.end_fill()