# -------factorial using recursion
'''
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(5))
'''


# -----fibonacci series enter length get series
# 0 1 1 2 3 5 8 13 21
'''
def fibonacci(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2) 

if __name__=='__main__':
    while True:    
        try:
            n=int(input("Enter fibonacci series length: "))
            for i in range(n):
                print(fibonacci(i),end=' ')
            break
        except:
            print('Invalid input. Enter positive integer!\n')
'''


# --------  lamda
''' 
# This is regular function
def sq(a):
    return  a*a
print(sq(5))
'''

'''
number=[1,5,6,3,2,8,7]
sq=lambda a:a*a        #function che name left of = , argument lemda nantr che ani operation : nantr cha
ll=list(map(sq,number)) #list chya elements ver sq function implement karun ll madhe store kele
print(ll)
'''


#  --------- Map function
'''
number=['12','56','45']     #list of string
# 1st argument of map is the function which we want to apply on each element of list
# humne jo object hai yani jo elements hai jo map ne diye vo llist me type cast kar diye
number=list(map(int,number))   #map jo hai vo object return karta hai
print(number[1]+3)
'''


# ----------up to 2 decimal number
'''
scores=[12,2.5,2.68]
tot_marks=0
for i in range(len(scores)):
    tot_marks+=scores[i]
print("%.2f"%((tot_marks/len(scores))))   #"%.2f"%values is used for 2 number after decimal
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
