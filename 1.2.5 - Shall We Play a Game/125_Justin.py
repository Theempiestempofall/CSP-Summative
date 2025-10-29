import turtle as trtl
import random as rand
import keyboard




bet_turtle1 = trtl.Turtle(shape="turtle")
bet_turtle1.color("red")
bet_turtle1.teleport(-200, 250)
bet_turtle1.write("$1", font=("Arial", 20, "normal"))
bet_turtle5 = trtl.Turtle(shape="turtle")
bet_turtle5.color("blue")
bet_turtle5.teleport(-100, 250)
bet_turtle5.write("$5", font=("Arial", 20, "normal"))
bet_turtle10 = trtl.Turtle(shape="turtle")
bet_turtle10.color("yellow")
bet_turtle10.teleport(0, 250)
bet_turtle10.write("$10", font=("Arial", 20, "normal"))
bet_turtle50 = trtl.Turtle(shape="turtle")
bet_turtle50.color("green")
bet_turtle50.teleport(100, 250)
bet_turtle50.write("$50", font=("Arial", 20, "normal"))
bet_turtle250 = trtl.Turtle(shape="turtle")
bet_turtle250.color("purple")
bet_turtle250.teleport(200, 250)
bet_turtle250.write("$250", font=("Arial", 20, "normal"))
bet_writer = trtl.Turtle(visible=False)
bet_writer.penup()
bet_writer.goto(0, 200)
money_writer = trtl.Turtle(visible=False)
money_writer.penup()
money_writer.goto(0, 300)
Slot1Pen = trtl.Turtle(shape = "circle",visible=True)
Slot1Pen.shapesize(stretch_wid=10, stretch_len=10)
Slot1Pen. teleport(-200,0)
Slot2Pen = trtl.Turtle(shape = "circle",visible=True)
Slot2Pen.shapesize(stretch_wid=10, stretch_len=10)
Slot2Pen. teleport(0,0)
Slot3Pen = trtl.Turtle(shape = "circle", visible=True)
Slot3Pen.shapesize(stretch_wid=10, stretch_len=10)
Slot3Pen. teleport(200,0)
Possible_colors = ["red", "blue", "yellow", "green", "purple", "orange"]
Possible_shapes = ["circle", "square", "triangle", "turtle", "arrow", "classic"]
wn = trtl.Screen()
wn.bgcolor("#3fa652")
money = 1000
bet = 0
timer = 0
timer_up = False
i = 1
trtl.textinput
#---------Function Setup---------------
# Display money
def update_money_display():
    money_writer.clear()
    money_writer.write("Money: $" + str(money), align='center', font=("Arial", 30, "normal"))
# Showing bets
def update_bet_display():
    bet_writer.clear()
    bet_writer.write("Bet: $" + str(bet), align='center', font=("Arial", 30, "normal"))
def place_bet(num_increase):
    global bet
    print("bet is being set")
    if money - (bet + num_increase) > 0:
        bet = num_increase + bet
    update_bet_display()
    wn.update()
#Spinning the slots
def spin_slots():

    global money, bet, timer_up

    
    timer_up = False
    while timer_up == False:
        print("Slots are spinning")
        wn.ontimer(end_timer, 1000)# I think 1000 is a second but idk
        Slot1Pen.color(Possible_colors[rand.randint(0,len(Possible_colors)-1)])
        Slot1Pen.shape(Possible_shapes[rand.randint(0,len(Possible_shapes)-1)])
        Slot2Pen.color(Possible_colors[rand.randint(0,len(Possible_colors)-1)])
        Slot2Pen.shape(Possible_shapes[rand.randint(0,len(Possible_shapes)-1)])
        Slot3Pen.color(Possible_colors[rand.randint(0,len(Possible_colors)-1)])
        Slot3Pen.shape(Possible_shapes[rand.randint(0,len(Possible_shapes)-1)])


    check_win()
    update_money_display()
    
def end_timer():
    global timer_up
    timer_up = True

#Check if you win
def check_win():
    global money, bet
    print("checking win")
    if Slot1Pen.shape() == Slot2Pen.shape() == Slot3Pen.shape() and Slot1Pen.color() == Slot2Pen.color() == Slot3Pen.color():
        money = money + (bet * 10)
    elif Slot1Pen.shape() == Slot2Pen.shape() == Slot3Pen.shape() or Slot1Pen.color() == Slot2Pen.color() == Slot3Pen.color():
        money = money + (bet * 5)
    elif Slot1Pen.shape() == Slot2Pen.shape() or Slot2Pen.shape() == Slot3Pen.shape() or Slot1Pen.shape() == Slot3Pen.shape() or Slot1Pen.color() == Slot2Pen.color() or Slot2Pen.color() == Slot3Pen.color() or Slot1Pen.color() == Slot3Pen.color():
        money = money + (bet * 2)
    else:
        money = money - bet
    if money == 0:# Ending the program if you have no money
        wn.bye()
#---------Game Loop---------------


def check_key(key):
    global timer_up
    wn.tracer(True)
    if key == "s":
        print(key+" is pressed")
        spin_slots() 
    if key == "b":
        print(key+" is pressed")
        place_bet()
    if key == "q":
        wn.bye()

for letter in "qsb":
  wn.onkeypress(lambda l=letter: check_key(l), letter)


wn.listen()

wn.tracer(True)

wn.mainloop()