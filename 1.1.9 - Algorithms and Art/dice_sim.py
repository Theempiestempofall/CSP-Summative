import turtle as trtl
import random
dice_num_faces = trtl.textinput("Dice Faces", "How many faces should the dice have? (between 2 and 20)")
num_of_dice = trtl.textinput("Number of Dice", "How many dice should be rolled? (between 1 and 10)")
current_number = 0
results = []
total = 0
total_totals = 0
total_average = 0
num_of_itterations = 0
x_pos = -300
y_pos = 300


# roll dice 
def roll_dice():
    global current_number, results, total, x_pos, y_pos, total_average, num_of_itterations, total_totals
    results = []
    total = 0
    for roll in range(int(num_of_dice)):
        current_number = random.randint(1, int(dice_num_faces))
        results.append(current_number)
        total = total + current_number
    total_totals = total_totals + total
    num_of_itterations = num_of_itterations + 1
    total_average = total_totals / num_of_itterations
    y_pos = y_pos - 20
    trtl.teleport(x_pos, y_pos)
    trtl.write("You rolled: " + str(results), font=("Arial", 8, "normal"))
    y_pos = y_pos - 20
    trtl.teleport(x_pos, y_pos)
    trtl.write("You totaled: " + str(total), font=("Arial", 8, "normal"))
    y_pos = y_pos - 20
    trtl.teleport(x_pos, y_pos)
    trtl.write("Your total average is: " + str(total_average), font=("Arial", 8, "normal"))


roll_dice()

answer = trtl.textinput("Again?", "y or n")
while answer == "y":
    total = 0
    roll_dice()
    answer = trtl.textinput("Again?", "yes or no")

wn = trtl.Screen()
wn.mainloop()