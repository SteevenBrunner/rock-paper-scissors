#!/usr/bin/env python

import var_storage


class Paper:
    def __init__(self):
        pass

    @staticmethod
    def attack(rock=None, paper=None, scissors=None):
        if rock is not None:
            print "You chose paper, your opponent chose rock. You win!\n"
            var_storage.my_score += 1
        elif paper is not None:
            print "You chose paper, your opponent chose paper. It's a tie\n"
        elif scissors is not None:
            print "You chose paper, your opponent chose scissors. Your opponent wins!\n"
            var_storage.opponent_score += 1