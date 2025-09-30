import turtle as trtl
import random
#ask the user questions
#set the answers to varibles 
#make turtle draw a shape the changes depending on what the user said
shape_color = input ("What is you favorite color?")
shape_num_edges = input ("Pick a number between 1 and 10")
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
for i in range (int(shape_num_edges)):
    shape_edges_list.remove(random.choice(shape_edges_list))
shape_edges_tuple = tuple(shape_edges_list)
trtl.addshape( "polygon", shape_edges_tuple )

pg = trtl.Turtle(shape = "polygon")
pg.color(shape_color)

wn = trtl.Screen()
wn.mainloop()