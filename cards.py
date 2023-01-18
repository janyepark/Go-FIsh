import random
from random import shuffle

"""
this module creates a deck of shuffled cards, excluding Jokers
"""

class Card:
    """
    assigns cards a value and a suit

    attributes:
    value(str): an integer between 2-14 used to assign cards to a name
    suit(str): a pattern - clubs, diamonds, hearts, spades - used to assign cards to a name
    """
    def __init__(self, value, suit):
        """
        assigns a suit and value to cards
        """
        self.suit = suit
        self.value = value

        values = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 
        9: "9", 10: "10", 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
        
        self.name = values[int(value)]
      
    def __str__(self):
        """
        creates a string representation of an object
        returns string in the form: "<name> of <suit>"
        """
        return f'{self.suit} of {self.value}'


class Deck:
    """
    creates a deck of 52 cards with each combination of suit and value

    attributes:
    value(str): an integer between 2-14 used to assign cards to a name
    suit(str): a pattern - clubs, diamonds, hearts, spades - used to assign cards to a name
    cards(list): a list of cards, each card has a value and suit
    """
    def __init__(self):
        """
        creates a deck of 52 cards with each combination of suit and value
        """
        self.value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
        self.suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.cards = []
        for i in range(4):
            for j in range(13):
                self.cards.append(Card(self.value[j], self.suit[i]))

    def shuffle(self):
        """
        randomizes the order of the cards
        """
        random.shuffle(self.cards)

    def draw(self):
        """
        removes and returns a card if there are cards left in the deck
        runs RuntimeError if the deck is empty
        """
        if len(self.cards) != 0:
           return self.cards.pop()
        else:
            raise RuntimeError