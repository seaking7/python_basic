import turtle as t

t.speed(0)
t.color("lightblue")
t.begin_fill()
t.pensize(5)
t.right(180)
t.up()
t.forward(200)
t.up()
t.left(90)
t.down()
t.circle(200)
t.end_fill()



def draw_number(angle, number):
    t.up()
    t.home()
    t.right(angle)
    t.forward(180)
    t.down()
    t.color("black")
    t.forward(30)
    t.write(number, False, "center", ("", 40))


draw_number(270, "12")
draw_number(0, "3")
draw_number(90, '6')
draw_number(180, "9")
draw_number(330, "2")

t.mainloop()


# t.up()
# t.home()
# t.right(90)
# t.forward(180)
# t.down()
# t.forward(25)
# t.write("6", False, "center", ("", 30))


# t.up()
# t.home()
# t.right(180)
# t.forward(180)
# t.down()
# t.forward(25)
# t.write("9", False, "center", ("", 30))

# t.up()
# t.home()
# t.left(30)
# t.forward(180)
# t.down()
# t.forward(30)
# t.write("2", False, "center", ("", 30))

t.up()
t.home()




t.mainloop()