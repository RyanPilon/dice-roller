import random

roll_again = "y"
random.seed(1)
sequence = [i for i in range(1,9)]


while roll_again == "y":
    print("Your dice are ....")
    for dice in range(6):
	    selection = random.choice(sequence)
	    print(selection)
    roll_again = input("Roll the dices again? Y/N - ").lower()
