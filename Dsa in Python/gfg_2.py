#------------- Python program to get Current Time
'''
import datetime
Time=datetime.datetime.now()
date=datetime.datetime(2023,2,2)
print(Time)
print('Date',date)
print('Hour',Time.hour)
print('Minutes',Time.minute)
print('Seconds',Time.second)
print('Year',Time.year)
print('Month',Time.month)
print('day',Time.day)
'''


# ------Shuffle a deck of card with OOPS in Python
'''
from random import shuffle    #import required modules
class Cards():
    global suits,values     #Declare a class named Cards which will have variables suites and values, now instead of using self.suites and self.values, we are going to declare them as global variables.
    suits=['Spade','Club','Diamond','Heart'] 
    values=['1','2','3','4','5','6','7','8','9','10','11','12','13']
    

class Deck(Cards):       #Declare a class Deck which will have an empty list named as mycardset, and the suites and values will be appended to mycardset  list.
    # Constructor
    def __init__(self):
        Cards.__init__(self)
        self.mycardset=[]
        for s in suits:
            for v in values:
                self.mycardset.append(v+' of '+s)
    # Method to print cards from the deck
    def print_cards(self):
        print(self.mycardset)
        

class ShuffleCards(Deck):      #Declare a class ShuffleCards along with a method named shuffle() that would check the number of cards and then shuffles them.
    # Constructor
    def __init__(self):
        Deck.__init__(self)

    #  Method to shuffle cards
    def shuffle_card(self):
        shuffle(self.mycardset)

    def popCard(self):         #To remove some cards we will create a popCard() method in ShuffleCards class.
        get_card=input("Do you want to get a card? (Y/N): ")
        if get_card=='Y' or get_card=='y':    
            popedcard=self.mycardset.pop()
            print('Your poped card is: ',popedcard)
        else:
            print('OK!')
        
# Creating object
objCards=Cards()
objDeck=Deck()
objShuffle=ShuffleCards()

print('Unshuffeled Deck of Cards -->')
objDeck.print_cards()
objShuffle.shuffle_card()
print('Shuffeled Deck of Cards -->')
objShuffle.print_cards()
objShuffle.popCard()
'''

'''
import random
cards=['Queen','Jack', 'King']
random.shuffle(cards)
print(cards)
'''
























