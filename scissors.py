#!/usr/bin/env python

import var_storage


class Scissors:
    def __init__(self):
        pass

    @staticmethod
    def attack(rock=None, paper=None, scissors=None):
        if rock is not None:
            print "You chose scissors, your opponent chose rock. Your opponent wins!\n"
            var_storage.opponent_score += 1
        elif paper is not None:
            print "You chose scissors, your opponent chose paper. You win!\n"
            var_storage.my_score += 1
        elif scissors is not None:
            print "You chose scissors, your opponent chose scissors. It's a tie!\n"