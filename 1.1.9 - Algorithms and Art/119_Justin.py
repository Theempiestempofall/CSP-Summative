import turtle as trtl
import random
# get user input for shape color and number of edges
trtl.textinput("Fun Time","Are you ready to create a shape?")
shape_color = trtl.textinput("Color","What is your favorite color?")
shape_num_edges = trtl.textinput ("Number","Pick a number between 1 and 10")
shape_edges_list = [
    (0, 0),
    (0, 50), 
    (80, 40), 
    (25, 25), 
    (40, 10), 
    (50, 0), 
    (40, -100), 
    (5, -25), 
    (10, -40), 
    (0, -50), 
    (-50, 0)]
# remove random edges from the list to create a unique shape
num_removals = min(11-int(shape_num_edges), len(shape_edges_list) - 3)
for i in range(num_removals):
    shape_edges_list.remove(random.choice(shape_edges_list))
shape_edges_tuple = tuple(shape_edges_list)
# create custom polygon turtle shape
trtl.addshape("polygon", shape_edges_tuple)

pg = trtl.Turtle(shape = "polygon")
pg.color(shape_color)

wn = trtl.Screen()
wn.mainloop()