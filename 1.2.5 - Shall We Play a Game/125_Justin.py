import turtle as trtl
import random as rand

bet_writer = trtl.Turtle(visible=False)
bet_writer.penup()
bet_writer.goto(0, 200)
money_writer = trtl.Turtle(visible=False)
money_writer.penup()
money_writer.goto(0, 250)
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
timer = 3
timer_up = False
#---------Function Setup---------------
def update_bet_display():
    bet_writer.clear()
    bet_writer.write("Bet: $" + str(bet), align='center', font=("Arial", 30, "normal"))
def update_money_display():
    money_writer.clear()
    money_writer.write("Money: $" + str(money), align='center', font=("Arial", 30, "normal"))
def place_bet():
    global bet
    bet = wn.numinput("Place your bet", "You have $" + str(money) + ". How much would you like to bet?", minval=1, maxval=money)
    update_bet_display()

def spin_slots():
    global money, bet, timer, timer_up
    timer = 3
    print("Slots are spinning")
    while timer_up == False:
        Slot1Pen.color(Possible_colors[rand.randint(0,len(Possible_colors)-1)])
        Slot1Pen.shape(Possible_shapes[rand.randint(0,len(Possible_shapes)-1)])
        Slot2Pen.color(Possible_colors[rand.randint(0,len(Possible_colors)-1)])
        Slot2Pen.shape(Possible_shapes[rand.randint(0,len(Possible_shapes)-1)])
        Slot3Pen.color(Possible_colors[rand.randint(0,len(Possible_colors)-1)])
        Slot3Pen.shape(Possible_shapes[rand.randint(0,len(Possible_shapes)-1)])
    check_win()
    update_money_display()
def check_win():
    global money, bet
    if Slot1Pen.shape() == Slot2Pen.shape() == Slot3Pen.shape() and Slot1Pen.color() == Slot2Pen.color() == Slot3Pen.color():
        money = money + (bet * 10)
        trtl.textinput("You Win!", "Congratulations! You won $" + str(bet * 10) + "! You now have $" + str(money) + ". Press Enter to continue.")
    elif Slot1Pen.shape() == Slot2Pen.shape() == Slot3Pen.shape() or Slot1Pen.color() == Slot2Pen.color() == Slot3Pen.color():
        money = money + (bet * 5)
        trtl.textinput("You Win!", "Congratulations! You won $" + str(bet * 5) + "! You now have $" + str(money) + ". Press Enter to continue.")
    elif Slot1Pen.shape() == Slot2Pen.shape() or Slot2Pen.shape() == Slot3Pen.shape() or Slot1Pen.shape() == Slot3Pen.shape() or Slot1Pen.color() == Slot2Pen.color() or Slot2Pen.color() == Slot3Pen.color() or Slot1Pen.color() == Slot3Pen.color():
        money = money + (bet * 2)
        trtl.textinput("You Win!", "Congratulations! You won $" + str(bet * 2) + "! You now have $" + str(money) + ". Press Enter to continue.")
    else:
        money = money - bet
        trtl.textinput("You Lose!", "Sorry, you lost your bet of $" + str(bet) + ". You now have $" + str(money) + ". Press Enter to continue.")
    if money == 0:
        trtl.textinput("Game Over", "You have run out of money! Game Over! Press Enter to exit.")
        wn.bye()
def countdown():# making it look like a slot machine roling down
    global timer, timer_up
    if timer <= 0:
        timer_up = True
    else:
        timer -= 1
#---------Game Loop---------------
spin_slots()


wn.onkeypress(place_bet, "b")
wn.onkeypress(spin_slots, "r")
wn.ontimer(countdown, 1000)# I think 1000 is a second but idk
wn.listen()
wn.mainloop()