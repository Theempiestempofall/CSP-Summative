import turtle

start_x_pos = -350
start_y_pos = 50
turtle.setup(width=800, height=600)
turtle.bgcolor("lightblue")
turtle.textinput("Physics Simulation", "Press OK to start the simulation.")
gravity = turtle.textinput("Gravity factor", "Enter a gravity factor (suggested: 1 to 5)")
x_start_velocity = turtle.textinput("velocity factor", "Enter a horizontal velocity factor (suggested: 10 to 100)")
iteration_distance = turtle.textinput("iteration distance", "Enter the distance between iterations (suggested: 0.5 to 2)")
ball = turtle.Turtle(shape="circle")
ball.teleport(start_x_pos, start_y_pos)
ball.color("red")
ball.shapesize(stretch_wid=0.2, stretch_len=0.2)
for i in range(200):
    x_pos = ball.xcor()
    y_pos = ball.ycor()
    new_x_pos = x_pos + ((float(x_start_velocity)) * (float(iteration_distance)))
    new_y_pos = y_pos - ((float(gravity) * (float(iteration_distance) * i))) * float(iteration_distance)
    ball.goto(new_x_pos, new_y_pos)
    ball.stamp()
    turtle.delay(0)
    turtle.update()






wn = turtle.Screen()
wn.mainloop()