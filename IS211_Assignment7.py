#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assingment7: A simple game of dice."""


import random


class Dice(object):
    """A class for the dice; random numbers between 1 to 6.
    """
    random.seed(0)

    def __init__(self):
        """A dice class constructor."""
        self.rolled = 0

    def roll(self):
        """A roll function for the dice call.

        Attributes:
            Dice (class): INvokes the dice class.

        Returns:
            Integar (int): Returns an integar from 1 to 6.
        """
        self.rolled = random.randint(1, 6)
        return self.rolled


class Player(object):
    """A plyer class for the game. """
    def __init__(self, name):
        """A constructor for the player class.

        Args:
            name (string): The player name.

        Attributes:
            Player (class): Invokes the playr class.
            name (string): The player name.
        """
        self.name = name
        self.score_total = 0
        self.score_turn = 0
        self.turn_num = 0
        print 'Welcom! {}'.format(self.name)


class Game(object):
    """A game class.

    Class the rice class and the player class to be used in the game.

    Example:
        >>> Game('Homer', 'Ned')
        Welcom! Homer
        Welcom! Ned
        Player turn: Homer
        Homer rolled a 6
        Homer has a current score of 6, and total score of 6
        Homer, Would you like to Roll (R/r) the dice or Hold (H/h) this turn? r
        Player turn: Homer
        Homer rolled a 1, lose a turn.
        ...
        Player turn: Ned
        Ned rolled a 1, lose a turn.
        Ned, your current score is 93
        ...
        Player turn: Homer
        Homer rolled a 5
        Homer has a current score of 5, and total score of 101
        Homer, Would you like to Roll (R/r) the dice or Hold (H/h) this turn? r
        Player turn: Homer
        WInner! Homer has won the game! With a total score of 101!
    """
    def __init__(self, player_1, player_2):
        """A constructor for the game class.

        Args:
            player_1 (string) : the name of player 1.
            player_2 (string): the name of player 2.

        Attributes:
            Game (class): invokes the game class.
            Player (class): Invokes the player class.
            player_1 (string) : the name of player 1.
            player_2 (string): the name of player 2.
        """
        self.player_1 = Player(player_1)
        self.player_2 = Player(player_2)
        self.dice = Dice()
        self.turn(self.player_1)

    def turn(self, player):
        """A player turn function."""
        player.turn_num = 1
        print 'Player turn: {}'.format(player.name)
        if player.turn_num == 1 and player.score_total < 100:
            roll = self.dice.roll()
            if roll == 1:
                print '{} rolled a 1, lose a turn.'.format(player.name)
                print '{}, your current score is {}'.format(player.name,
                                                            player.score_total)
                player.score_turn = 0
                self.next_player()
            else:
                print '{} rolled a {}'.format(player.name, roll)
                player.score_turn = roll
                player.score_total += player.score_turn
                print ('{} has a current score of {},'
                       ' and total score of {}').format(player.name,
                                                  player.score_turn,
                                                  player.score_total)
                self.turn_select(player)
        else:
            player.score_total >= 100
            print ('WInner! '
                    '{} has won the game!'
                    ' With a total score of {}!').format(player.name,
                                                         player.score_total)
        
    
    def turn_select(self, player):
        """A funtion for player's turn.

        Args:
            player (string) The name of the player.

        Returns:
            String (string): A meesage to display the player's name,
            current score, and total score.
        """
        select = raw_input('{}, Would you like to Roll (R/r) the dice'
                           ' or Hold (H/h) this turn? '.format(player.name))
        select = (select[0])
        if select.lower() == 'h':
            player.score_total += player.score_turn
            print ('{} holds with a total score of {}').format(player.name,
                                                               player.score_total)
            if player.score_total >= 100:
                print ('WInner!'
                       '{} has won the game!'
                       'With a total score of {}!'
                       'Thanks for playing!').format(player.name,
                                                     player.score_total)
                raise SystemExit
            else:
                player.score_turn = 0
                print ('{}, your current score is {}.'
                       ' Next player please.').format(player.name,
                                                     player.score_total)
                self.next_player()
        elif select.lower() == 'r':
            self.turn(player)
        else:
            print 'Please enter R/r to roll the dice or H/h to hold.'
            self.turn_select(player)

    def next_player(self):
        """A function to select the next player"""

        if self.player_1.turn_num == 1:
            self.player_1.turn_num = 0
            self.turn(self.player_2)
        else:
            self.player_2.turn_status = 0
            self.turn(self.player_1)
