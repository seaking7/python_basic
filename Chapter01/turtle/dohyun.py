from re import T
import turtle as t

# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.mainloop()
t.speed(10)
d = 250
t.color('blue')
t.begin_fill()
t.forward(d)
t.right(120)
t.forward(d)
t.right(120)
t.forward(d)
t.right(120)
t.forward(d)
t.end_fill()
t.color("red")
t.begin_fill()
t.circle(100)
t.end_fill()

t.mainloop()
