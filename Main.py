#!/usr/bin/env python

import random

from rock import Rock
from paper import Paper
from scissors import Scissors
import var_storage

classes = (Rock, Paper, Scissors)
convert_classes = {'rock': Rock(), 'paper': Paper(), 'scissors': Scissors()}

nbr_of_round = input("How many rounds? ")
print "Game started"
nbr_of_round += 1

for i in range(1, nbr_of_round):
    my_choice = raw_input("Make your choice for round " + str(i) + " : ")

    my_choice = convert_classes.get(my_choice)
    opponent_choice = random.choice(classes)()

    if isinstance(opponent_choice, Rock) is True:
        print "opponent choice is Rock"
        my_choice.attack(rock=True)
    elif isinstance(opponent_choice, Paper) is True:
        print "opponent choice is Paper"
        my_choice.attack(paper=True)
    elif isinstance(opponent_choice, Scissors) is True:
        print "opponent choice is Scissors"
        my_choice.attack(scissors=True)

first_part = "Result, you won " + str(var_storage.my_score) + "time(s), your opponent won " + \
             str(var_storage.opponent_score) + "time(s). "
if var_storage.opponent_score == var_storage.my_score:
    print first_part + "It's a tie!"
elif var_storage.opponent_score > var_storage.my_score:
    print first_part + "Your opponent wins!"
else:
    print first_part + "You win!"
