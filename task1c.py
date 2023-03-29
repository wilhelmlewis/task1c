import random

# get random number
comp_num = random.randint(1, 10)

# get user input
print("Welcome to the Guessing Game")
print("The Computer has picked a number from 1 - 10. Try to match it.")
user_guess = eval(input("What number do you choose (1-10): "))
print("You picked " + str(user_guess) + ", and the actual number was " + str(comp_num))

# compare user input to random number
guess_diff = user_guess - comp_num
msg = ""
if user_guess == comp_num:
    msg += "Honored to play with you, Master"
elif guess_diff == 1 or guess_diff == -1:
    msg += "You are a worthy opponent, Knight."
elif guess_diff == 2 or guess_diff == -2:
    msg += "You have much to learn, Padawan."
elif guess_diff == 3 or guess_diff == -3:
    msg += "youngling, your time will come."
else:
    msg += "Keep working hard in the Service Corps."

# print message based on how they compare
print(msg)