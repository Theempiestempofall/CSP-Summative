import turtle as trtl
import random
# get user input for shape color and number of edges
if (trtl.textinput("Fun Time","Are you ready to create a shape? (hint: 67)") == "67"):
    trtl.textinput("6 7","six seven")
acceptable_colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'black', 'white', 'gray', 'brown']
shape_color = trtl.textinput("Color","What is your favorite color?")
while shape_color is None or shape_color not in acceptable_colors:
    shape_color = trtl.textinput("Color", "Please enter a valid color")
shape_num_edges = trtl.textinput("Number", "Pick an integer between 1 and 10 (inclusive)")
while shape_num_edges is None or not shape_num_edges.isdigit() or not (1 <= int(shape_num_edges) <= 10):
    shape_num_edges = trtl.textinput("Number", "Please pick an integer between 1 and 10 (inclusive)")

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