# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
'''
ans=input('What is the Answer to the Great Question of Life, the Universe, and Everything?').lower()
if ans=='42' or ans == 'fourty-two' or ans=='fourty two':
    print('Yes')
else:
    print('No')
'''


# In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
'''
Greeting=input('Greeting: ').strip().lower()
greeting=Greeting.split(' ')
print(greeting)
if greeting[0]=='hello' or greeting[0]=='hello,':
    print('$0')
elif Greeting[0]=='h':
    print('$20')
else:
    print('$100')
'''


# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# Take input
# check input is valid or not use try exception for valueError or ZeroDivisionError
# seperate input as operand operator operand
# output percentage rounded to nearest integer out of 100 
# if more than 99% then output 'F', if less than 1% output 'E' 
'''
while True:
    try:                                     #1st try for value error
        Fraction=input('Fraction: ')          #input from user
        n,d=Fraction.split('/')               #slpit to numerator and denominator
        n,d=int(n),int(d)                     #converting to string
        if n <= d:                             #checking valid numerator and denominator
            try:                               #2nd try for zerodivision error
                percentage=n/d*100            #calculating percentage remaining
                percentage=round(percentage)
                # percentage=int(percentage)     #removing decimal
                if percentage >= 99:            #checking percentage greater than or equal to 99
                    print('F')
                    break                      #exiting loop if yes
                elif percentage <=1:            #checking percentage lesser than or equal to 1
                    print('E')
                    break                      #exiting loop if yes
                else:                           #else print percentage
                    print(f'{percentage}%')
                    break                      #exiting loop if yes
            except ZeroDivisionError:         #exception for zerodivision error
                pass
        else:
            pass
    except ValueError:                        #exception for value error
        pass
'''


# problem set 3
# In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item

# get input as item
# show total
# get item
# add price of each item and show total
# repeat untill user enter (ctrl+d)
'''
menu={                           #menu
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total=0                      #initializing total as 0

while True:
    try:
                                              #if ctrl+c then exit
        item=input('Item: ')
        item=item.title()
        try:                    #other inputs than item in menu
            if item in menu:       #if item is in menu then proceed further
                price=menu[item]
                total=total+price
                ftotal="%.2f" %total
                print(f'Total: ${ftotal}')     #print total after addition of each item 
            else:
                pass
        except :
            pass

    except EOFError:         #when pressed ctrl+c stop
        break
'''

# problem set 3
# In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

# get items until user enter ctrl+d
# print each item with its count on seperate line
'''
grocery=[]             #initial empty list  
grocery_dict={}          #final greocery with count empty list
while True:
    try:                     #input taken as item of grocery list
        item=input()
        grocery.append(item)   #append item in list

    except KeyboardInterrupt:   #when input is ctrl+c the execute exception
        print()                  #single empty line
        for i in range(len(grocery)):      #iterate each item of grocery list
            count = grocery.count(grocery[i])    #count of each item of list
            qnt = count 
            item = grocery[i].upper()        #saving item count and item in capital letts in items
            grocery_dict[item]=qnt
            
        for key in sorted(grocery_dict.keys()):                       #iterating each elemet of grocery_set set
            print(grocery_dict[key], key)                            #printing each element
        break
'''

# problem set4
# In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.
'''
# emojis=['thumbs_up:',':earth_africa:',':earth_asia:',':earth_americas:']  #examples of emojis
import emoji
text=input('Input: ')
print('Output: ',end='')
print(emoji.emojize(text,language='alias'))
'''

# Problem Set 4
# FIGlet has since been ported to Python as a module called pyfiglet.
# In a file called figlet.py, implement a program that:
# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

'''
import pyfiglet
import sys
if len(sys.argv)==3:
    if sys.argv[1]=='-f' or sys.argv[1]=='--font':
        try:
            print(pyfiglet.figlet_format('',font=sys.argv[2]),end='')
            Input=input('Input: ')
            print("Output: ")
            print(pyfiglet.figlet_format(Input,font=sys.argv[2]))
        except:
            print('Invalid usage')
            sys.exit()

    else:
        print('Invalid usage')
        sys.exit()
elif len(sys.argv)==1:
    Input=input('Input: ')
    print("Output: ")
    print(pyfiglet.figlet_format(Input))  
else:
    print('Invalid usage')
    sys.exit()
'''

'''
print(pyfiglet.print_figlet('World!'))  
print(pyfiglet.figlet_format('World!',font = "slant"))  
print(pyfiglet.figlet_format('World!',font = "5lineoblique"))  
print(pyfiglet.figlet_format('W o r l d !',font = "alphabet"))  
print(pyfiglet.figlet_format('W o r l d !',font = "3-d"))  
print(pyfiglet.figlet_format('W o r l d !',font = "banner3-D"))  
print(pyfiglet.figlet_format('W o r l d !',font = "doh"))  
print(pyfiglet.figlet_format('W o r l d !',font = "isometric1"))  
print(pyfiglet.figlet_format('W o r l d !',font = "letters"))  
print(pyfiglet.figlet_format('W o r l d !',font = "alligator"))  
print(pyfiglet.figlet_format('W o r l d !',font = "dotmatrix"))  
print(pyfiglet.figlet_format('W o r l d !',font = "bubble"))  
print(pyfiglet.figlet_format('W o r l d !',font = "bulbhead"))  
print(pyfiglet.figlet_format('W o r l d !',font = "digital"))  
print(pyfiglet.figlet_format('W o r l d !',font = "rectangles"))  
'''

# Problem Set 4
# In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and n names with n-1 commas and one and, as in the below:

# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa
# Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

# get names continiously 
# append names in certain list
# till loop breaks
'''
prefix='Adieu, adieu, to'       #given prefix
names=[]                        #empty list to store all name
while True:
    try:
        n=input('Name: ')           #take input
        names.append(n)             #append in names list

    except KeyboardInterrupt:                   #when pressed ctrl+c then execute this
        if len(names)==1:                       #if len(names) is equal to 1 
            print('\n'+ prefix + ' ' + names[0])      #print prefix and direct first name
            break
        
        elif len(names)==2:
            print('\n'+ prefix + ' ' + names[0] + ' and ' + names[1])
            break
        else:
            first = ', '.join(names[:len(names)-1])         #join 1 to last but 1 elements of names list with ',
            last=names[len(names)-1]                        #last element
            print('\n'+ prefix + ' ' + first + ', and ' + last)    #print prefix first to last with ',' and last element   
            break
'''

# problem set 4
# Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and n, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.
'''
import random
while True:
    try:
        n=int(input('level: '))
        num=random.randrange(1,n+1)
        while True:
            try:
                guess=int(input('Guess: '))
                if guess>num:
                    print('Too large!')
                elif guess<num:
                    print('Too small!')
                else:
                    print('Just right!')
                    break

            except:
                pass
        break
    except:
        pass
'''

# problem set 4
# In a file called professor.py, implement a program that:

# Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
#  digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score, a number out of 10.
# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
'''
import random
def main():
    get_level()
    

def get_level():
    while True:
        try:
            level=int(input('Level: '))
            if 1<=level<=3:
                level=level
                break
            else:
                pass
        except:
            pass
    generate_integer(level)


def generate_integer(level):
    if level==1:
        low=0
        high=9
    elif level==2:
        low=10
        high=99
    elif level==3:
        low=100
        high=999
    score=0
    for i in range(10):
        x=random.randint(low,high)
        y=random.randint(low,high)
        result=x+y
        x,y=str(x),str(y)
        for _ in range(3):
            try:
                answer=int(input(f'{x} + {y} = '))
                if answer==result:
                    score+=1
                    break
                elif _ == 2:
                    print('EEE')
                    print(f'{x} + {y} =',result)
                    break

                else:
                    print('EEE')

            except:
                print('EEE')
                pass

            if _ == 2:
                print(f'{x} + {y} =',result)
                break
    
    print('Final score:',score)
    

if __name__ == "__main__":
    main()
'''


# problem set 4
# implement a program that:
# Expects the user to specify as a command-line argument the number of Bitcoins,n 
# , that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
'''
import requests
import sys
import json

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

# print( json.dumps(response.json(), indent=2))    #print in the good format
obj=response.json()                              #print url to json format

# print(obj['bpi']['USD']['rate_float'])     #print usa rate float
price=obj['bpi']['USD']['rate_float']      #access only usa rate float 


if len(sys.argv) > 1:
    try:
        n=float(sys.argv[1])             #value at command-line
        value=n*price                        
        # print("%.4f" % value)           #make upto 4 number right to  decimal
        print('${:,}'.format(value))        #print in xxx,xxx,xxx format
        
    except:
        print('Command-line argument is not a number')
        sys.exit

else:
    print('Missing command-line argument')

'''
