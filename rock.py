#!/usr/bin/env python

import var_storage


class Rock:
    def __init__(self):
        pass

    @staticmethod
    def attack(rock=None, paper=None, scissors=None):
        if rock is not None:
            print "You chose rock, your opponent chose rock. It's a tie!\n"
        elif paper is not None:
            print "You chose rock, your opponent chose paper. Your opponent wins\n"
            var_storage.opponent_score += 1
        elif scissors is not None:
            print "You chose rock, your opponent chose scissors. You win!\n"
            var_storage.my_score += 1