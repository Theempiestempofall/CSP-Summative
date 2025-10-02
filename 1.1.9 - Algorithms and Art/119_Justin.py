import turtle as trtl
import random
# get user input for shape color and number of edges
ready = trtl.textinput("Fun Time","Are you ready to create a shape? (hint: 67)")
if (ready) == "no":
    trtl.bye()
if (ready) == "67":
    trtl.textinput("6 7","six seven")
acceptable_colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'black', 'white', 'gray', 'brown']
shape_color = trtl.textinput("Color","What is your favorite color?")
while shape_color is None or shape_color not in acceptable_colors:
    shape_color = trtl.textinput("Color", "Please enter a valid color")
shape_num_edges = trtl.textinput("Number", "Pick an integer between 3 and 10 (inclusive)")
while shape_num_edges is None or not shape_num_edges.isdigit() or not (3 <= int(shape_num_edges) <= 10):
    shape_num_edges = trtl.textinput("Number", "Please pick an integer between 3 and 10 (inclusive)")

shape_edges_list = []
# remove random edges from the list to create a unique shape
num_adds = max(int(shape_num_edges), 3)
for i in range(num_adds):
    rand_point_x = random.randint(-100, 100)
    rand_point_y = random.randint(-100, 100)
    rand_coord_pair = (rand_point_x,rand_point_y)
    shape_edges_list.append(rand_coord_pair)
shape_edges_tuple = tuple(shape_edges_list)
# create custom polygon turtle shape
trtl.addshape("polygon", shape_edges_tuple)
print(shape_edges_list)
pg = trtl.Turtle(shape = "polygon")
pg.color(shape_color)

wn = trtl.Screen()
wn.mainloop()