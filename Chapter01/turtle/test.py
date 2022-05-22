import turtle as t

t.shape("turtle")
t.color("pink")
t.pensize(5)
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.color("black")

# 시계의 원을 그리는 함수
def draw_circle(length):
    t.penup()
    t.left(90)
    t.forward(length)
    t.left(90)
    t.pendown()
    t.speed(0)
    t.begin_fill()
    t.circle(200)
    t.end_fill()

#시계의 주변 숫자를 그리는 함수
def draw_number(number, angle):
    t.penup()
    t.home()
    t.left(angle)
    t.forward(250)
    t.write(number, False, "center", ("", 40))



draw_circle(220)

# 숫자 표시
draw_number("12", 90)
draw_number("3", 0)
draw_number("6", 270)
draw_number("9", 180)

# t.home()
# t.forward(220)
# t.write("3", False, "center", ("", 30))


t.mainloop()