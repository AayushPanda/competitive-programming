#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Title: ROULETTE GAME
Author: Aayush Panda
Date: Mar 29, 2022
Course: ICS3UO-C
Objective: Simulate a roulette game.
"""

import random


def getBet():
    bet = input("Place your bet: [R]ed, [G]reen or [B]lack- ").upper()
    if bet == "RED":
        bet = 'R'
    elif bet == "BLACK":
        bet = 'B'
    elif bet == "GREEN":
        bet = 'G'
    elif bet not in "RGB":
        print("\nEnter a valid value for your bet\n")
        getBet()
    return bet


def game():
    money = 10
    while 20 > money > 0:
        print(f"Current amount of money: {money}")
        colour =(('G'*2) + ('R'*18) + ('B'*18))[random.randint(0, 38)]
        if colour == getBet():
            money += 1
        else:
            money -= 1

    if money == 0:
        print("\nGame over: You lost all your money!")
    else:
        print("\nGame over: You doubled your money and leave with $20")


def main():
    try:
        game()
    except:
        print("Enter a valid value in input.")
        main()


main()