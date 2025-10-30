import turtle as trtl
import random as rand
import math


win_writer = trtl.Turtle(visible=False)
win_writer.teleport(0, -250)
win_writer.write("Press S to spin slots and press Q to quit.\n Press the upper turtles to place bets.", align='center', font=("Arial", 40, "normal"))
bet_turtle_reset = trtl.Turtle(shape="turtle")
bet_turtle_reset.color("black")
bet_turtle_reset.teleport(-325, 250)
bet_turtle_reset.write("reset", font=("Arial", 20, "normal"))
bet_turtle1 = trtl.Turtle(shape="turtle")
bet_turtle1.color("red")
bet_turtle1.teleport(-225, 250)
bet_turtle1.write("$1", font=("Arial", 20, "normal"))
bet_turtle5 = trtl.Turtle(shape="turtle")
bet_turtle5.color("blue")
bet_turtle5.teleport(-125, 250)
bet_turtle5.write("$5", font=("Arial", 20, "normal"))
bet_turtle10 = trtl.Turtle(shape="turtle")
bet_turtle10.color("yellow")
bet_turtle10.teleport(-25, 250)
bet_turtle10.write("$10", font=("Arial", 20, "normal"))
bet_turtle50 = trtl.Turtle(shape="turtle")
bet_turtle50.color("green")
bet_turtle50.teleport(75, 250)
bet_turtle50.write("$50", font=("Arial", 20, "normal"))
bet_turtle250 = trtl.Turtle(shape="turtle")
bet_turtle250.color("purple")
bet_turtle250.teleport(175, 250)
bet_turtle250.write("$250", font=("Arial", 20, "normal"))
bet_turtle_all_in = trtl.Turtle(shape="turtle")
bet_turtle_all_in.teleport(275, 250)
bet_turtle_all_in.write("ALL IN", font=("Arial", 20, "normal"))
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
timer_up = True
i = 1
fav_color = trtl.textinput("What is your favorite color?", "Type your favorite color here:")
# Keep asking until turtle accepts the color; fallback to 'orange' if user cancels
while True:
    if fav_color is None:
        fav_color = "orange"
        Possible_colors.append(fav_color)
        bet_turtle_all_in.color(fav_color)
        break
    try:
        bet_turtle_all_in.color(fav_color)
        Possible_colors.append(fav_color)
        break
    except trtl.TurtleGraphicsError:
        fav_color = trtl.textinput("Invalid color, please enter a valid color:", "Type your favorite color here:")

#---------Function Setup---------------
# Display money
def update_money_display():
    money_writer.clear()
    money_writer.write("Money: $" + str(money), align='center', font=("Arial", 30, "normal"))
# Showing bets
def reset_bet():
    global bet
    print("bet is being reset")
    bet = 0
    update_bet_display()
def update_bet_display():
    bet_writer.clear()
    bet_writer.write("Bet: $" + str(bet), align='center', font=("Arial", 30, "normal"))
def place_bet(num_increase):
    global bet
    print("bet is being set")
    if money - (bet + num_increase) >= 0:
        bet = num_increase + bet
    update_bet_display()
    wn.update()
#Spinning the slots
def spin_slots():

    global money, bet, timer_up

    
    timer_up = False
    wn.ontimer(end_timer, 1000)# I think 1000 is a second but idk
    while timer_up == False:
        print("Slots are spinning")
        Slot1Pen.color(Possible_colors[rand.randint(0,len(Possible_colors)-1)])
        Slot1Pen.shape(Possible_shapes[rand.randint(0,len(Possible_shapes)-1)])
        Slot2Pen.color(Possible_colors[rand.randint(0,len(Possible_colors)-1)])
        Slot2Pen.shape(Possible_shapes[rand.randint(0,len(Possible_shapes)-1)])
        Slot3Pen.color(Possible_colors[rand.randint(0,len(Possible_colors)-1)])
        Slot3Pen.shape(Possible_shapes[rand.randint(0,len(Possible_shapes)-1)])


    check_win()
    update_money_display()
    reset_bet()
# Ending the timer
    
def end_timer():
    global timer_up
    timer_up = True

#Check if you win
def check_win():
    global money, bet, timer_up
    print("checking win")
    if Slot1Pen.shape() == Slot2Pen.shape() == Slot3Pen.shape() and Slot1Pen.color() == Slot2Pen.color() == Slot3Pen.color():
        money = money + math.ceil(bet * 2)
        win_writer.clear()
        win_writer.write("JACKPOT!", align='center', font=("Arial", 40, "normal"))
    elif Slot1Pen.shape() == Slot2Pen.shape() == Slot3Pen.shape() or Slot1Pen.color() == Slot2Pen.color() == Slot3Pen.color():
        money = money + math.ceil(bet * 1)
        win_writer.clear()
        win_writer.write("BIG WIN!", align='center', font=("Arial", 40, "normal"))
    elif Slot1Pen.shape() == Slot2Pen.shape() or Slot2Pen.shape() == Slot3Pen.shape() or Slot1Pen.shape() == Slot3Pen.shape() or Slot1Pen.color() == Slot2Pen.color() or Slot2Pen.color() == Slot3Pen.color() or Slot1Pen.color() == Slot3Pen.color():
        money = money + math.ceil(bet * 0.2)
        win_writer.clear()
        win_writer.write("WIN!", align='center', font=("Arial", 40, "normal"))
    else:
        money = money - bet
        win_writer.clear()
        win_writer.write("LOSE!", align='center', font=("Arial", 40, "normal"))
    if money == 0:# Ending the program if you have no money
        timer_up = False
        win_writer.clear()
        win_writer.write("Tried to be a big shot.\nYou lost it all.\nThats what you get for being a gambler.", align='center', font=("Arial", 40, "normal"))
        wn.ontimer(wn.bye, 3000)

def check_key(key):
    global timer_up
    wn.tracer(True)
    if key == "s":
        if timer_up == True:
            print(key+" is pressed")
            spin_slots() 
    if key == "q":
        wn.bye()

#---------Game Loop---------------

update_bet_display()
update_money_display()

for letter in "qsb":
  wn.onkeypress(lambda l=letter: check_key(l), letter)
bet_turtle_reset.onclick(lambda x, y: reset_bet())
bet_turtle1.onclick(lambda x, y: place_bet(1))
bet_turtle5.onclick(lambda x, y: place_bet(5))
bet_turtle10.onclick(lambda x, y: place_bet(10))
bet_turtle50.onclick(lambda x, y: place_bet(50))
bet_turtle250.onclick(lambda x, y: place_bet(250))
bet_turtle_all_in.onclick(lambda x, y: place_bet(money - bet))
wn.listen()

wn.tracer(True)

wn.mainloop()