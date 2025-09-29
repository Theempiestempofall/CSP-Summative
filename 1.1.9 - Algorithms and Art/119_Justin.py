import turtle as trtl
#ask the user questions
#set the answers to varibles 
#make turtle draw a shape the changes depending on what the user said
shape_color = input ("What is you favorite color?")
shape_num_edges = input ("Pick a number between 1 and 10")
shape_edges_list = ((0, 0), (0, 50), (10, 40), (25, 25), (40, 10), (50, 0), (40, -10), (25, -25), (10, -40), (0, -50), (-50, 0))
trtl.addshape( "polygon", shape_edges_list )

pg = trtl.Turtle(shape = "polygon")

wn = trtl.Screen()
wn.mainloop()