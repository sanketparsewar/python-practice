# print('Hello world')
# print('Hel"l"o world')

# print("Twinkle, twinkle, little star,\n\t How I wonder what you are! \n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\t How I wonder what you are")

#--------- version of python
# import sys
# print(sys.version,"\n")
# print(sys.version_info)


#-------- version of python
# import datetime
# now=datetime.datetime.now()
# print("currents date and time is:",now)


#--------- accept radius find area
# r=int(input("r:"))
# a=3.142*r*r
# print("a:",a)

# --------- accept radius find area
# from math import pi
# r=float(input("r="))
# print("Area=",pi*r**2)


#------- users first and last name print in reverse
# fn=input("fn=")
# ln=input("ln=")
# print(ln,fn)


#--------- take comma seperated numbers and create list and tuple
# n=input("comma seperated values=")
# list=n.split(",")
# tuple=tuple(list)
# print("list=",list)
# print("tuple=",tuple)


#---------- accept file name and print extension
# name=input("file name=")
# file=name.split(".")
# print("Extension is=",file[1])


#-------- to display 1st and last item
# color_list = ["Red","Green","White" ,"Black"]
# print(f"1st={color_list[0]} and last= {color_list[len(color_list)-1]}")


#-------- get exam time schedule
# exam_st_date = (11, 12, 2014)
# list=list(exam_st_date)
# print(f"{list[0]} / {list[1]} / {list[2]}")


#------- get n and print n+nn+nnn
# n=int(input("enter the number="))
# n1=int("%i" %n)
# n2=int("%i%i" %(n,n))
# n3=int("%i%i%i" %(n,n,n))
# print(n1+n2+n3)


#-------- print a calender
# import calendar
# m=int(input("month="))
# y=int(input("year="))
# print(calendar.month(y,m))


#--------- print the sample string
# print("""a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example""")


#---------- calculate the no of days between the two dates
# from datetime import date
# date1=date(2015, 8, 2)
# date2=date(2015, 9, 3)
# diffs=date2-date1
# print(diffs.days)


#--------- volume of sphere
# from math import pi
# r=int(input("r="))
# v=(4*pi*r**3)/3
# print("volume=",v)


#--------- return diff bet user number and 17
# num=int(input("Enter number="))
# diff=num-17
# if num<17:
#     print(17-num)
# else:
#     print((num-17)*2)


#-------- test whether a number is within 100 of 1000 or 2000.
# def near_thousands(n):
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# print(near_thousands(200))
# print(near_thousands(900))
# print(near_thousands(2100))


#---------- sum of three numbers
# a=int(input())
# b=int(input())
# c=int(input())
# sum=a+b+c
# if a==b==c:
#     print("sum=",sum*3)
# else:
#     print("sum=",sum)


#---------- get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
# str="Is the war between the two countries over?"
# if str.startswith("Is"):
#     print(str)
# else:
#     print("Is "+str)


#----------- create multiple copies
# n=int(input("No of copies you want="))
# str="This is the sample string we have taken here"
# for i in range(n):
#     print(str)
# -----------------------------OR----------------------
# def copies(str,n):
#     for i in range(n):
#         print(str)
# copies("This is the string which is to be copied",4)


#-------- find out even odd
# def even_odd(num):
#     if num%2==0:
#         return "given number is even"
#     return "given number is odd"
# print(even_odd(7))
# print(even_odd(2))
# print(even_odd(4))


#-------- program to count the number 4 in a given list
# l=[2,5,4,44,134,24,4,3,1,5,6,8,4,2,5,6,2,5,7,3,4,7,0]
# count=0
# for i in l:
#     if i==4:
#         count=count+1
# print(count)
# -------------------------------OR------------------
# l=[2,5,4,44,134,24,4,3,1,5,6,244,42,56,4,1,4,4,0]
# print("Total count:",l.count(4))


#--------- program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2
# def copies(str,n):
#     if len(str)<2:
#         return n*str
#     return n*str[:2]
# print(copies("Hello world",5))
# print(copies("is",5))
# print(copies("s",5))
# print(copies("World",5))


#--------- test whether a passed letter is a vowel or not
# def Vowel(char):
#     v=["a","e","i","u","o","A","E","I","O","U"]
#     for i in v:
#         if char==i:
#             return "Vowel"
#     return "Consonant"
# print(Vowel("O"))


#-------- check whether a specified value is contained in a group of values
# def check(value,list):
#     for i in list:
#         if value==int(i):
#             return True
#     return False
# print(check(3,[1,3,5,7,9]))
# print(check(6,[1,3,5,7,9]))
# print(check(80,[1,6,80,2,5,5,9]))


#--------- to create a histogram from a given list of integers
# def histogram(values):
#     for i in values:
#         print(i*"$")
# histogram([1,4,7,2,3,9,8,4,2,5])


#-------- concatenate all elements in a list into a string and return it.
# def concatenation(list):
#     con=""
#     for i in list:
#         con=con+str(i)
#     return con
# print(concatenation(["As","sonn","as","this","will","stop","we","will","be","there"]))
# print(concatenation([3,2,4,6,6,7,9,2,1]))


#--------- print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
# for i in numbers:
#     if i!=237:
#         if i%2==0:
#             print(i)
#     else:
#         print(f"{i} arrived")
#         break


#--------- set containing all the colors from color_list_1 which are not present in color_list_2\
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# result=color_list_1-color_list_2
# print(result)


#-------- accept the base and height of a triangle and compute the area.
# def area(b,h):
#     return (b*h)/2
# print("Area of triangle is",area(5,3))
# print("Area of triangle is",area(1,3.2))
# print("Area of triangle is",area(4.1,7))


#----------- to sum of three given integers. However, if two values are equal sum will be zero
# def sum(a,b,c):
#     if a==b or b==c or c==a:
#         return 0
#     return a+b+c
# print(sum(2,4,6))
# print(sum(2,4,1))
# print(sum(2,4,2))


#-------- to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
# def sum(a,b):
#     sum=a+b
#     if 15<sum<20:
#         return 20
#     return sum
# print(sum(20,-1))


#----------- the two given integer values are equal or their sum or difference is 5
# def value(a,b):
#     if a==b or a+b==5 or a-b==5:
#         return True
#     return False
# print(value(-3,8))


#----------- get the least common multiple (LCM) of two positive integers
# def lcm(a,b):
#     greater=0
#     if a>b:
#         greater=a
#     else:
#         greater=b
#     while(True):
#         if greater%a==0 and greater%b==0:
#             lcm=greater
#             break
#         greater+=1
#     return lcm
# print(lcm(4, 6))
# print(lcm(15, 17))
# print(lcm(10, 13))


#------------ add two objects if both objects are an integer type
# def add(a,b):
#     if type(a)==int and type(b)==int:
#         return a+b
#     else:
#         return "No int found"

# print(add(2,"sank"))
# print(add("par","sank"))
# print(add(5,6))
# print(add("5",6))


#----------- compute the future value of a specified principal amount, rate of interest, and a number of years.
# def amount(amt,int,year):
#     tot=amt*(1+(0.01*int))**year
#     return tot
# print(amount(10000,3.5,7))


#---------- Python program to check whether a file exists
# import os.path
# print(os.path.isfile("main.txt"))

#----------- determine if a Python shell is executing in 32bit or 64bit mode on OS
# import struct
# print(struct.calcsize("P")*8)


# import platform
# import os
# print("\nName of the OS system:",platform.system())
# print("\nVersion of the operating system:",platform.release())


# cars = ['Ford', 'BMW', 'Volvo']
# cars = [9,6,4,2,1,2,3]
# cars.sort()
# print(cars)

# arr = [1, 9, 1, 9, 5, 95, 454, 8, 787]
# arr.sort()
# print(arr)
# arr=set(arr)
# print(arr)
# sortedarr=sorted(arr)
# print(sortedarr)
# l1=list(sortedarr)
# print(l1)
# print(l1[-2])


# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# scores=[37.21,37.21,37.2,41,39]
# sortedscoreset=sorted(set(scores))[1]
# print(sortedscoreset)
# for k,v in sorted(students):
#     # print(k,v)
#     if v==sortedscoreset:
#         print(k)


# -------------expenses of months using dictionary ------------------  
# expense={"January" : 2200,
# "February" : 2350,
# "March":2600,
# "April":2130,
# "May":2190}
# print(expense)
# print(expense["February"]-expense["January"])
# sum=0
# for values in expense:
#     print(expense[values])
# print(sum)


# name=input("what's your name?")
# remove space from left and right
# name=name.strip()
# capitalize first alphabet of string
# name=name.capitalize()
# capitalize first alphabet of every letter in string
# name=name.title()
# split string in two smaller substrings
# first,middle,last=name.split(" ")
# print(f"HEllo, {middle}")

# def pyramid(n):
#     for i in range(n):
#         print("#"*i)
#
# if __name__ == '__main__':
#     height=int(input(("height= ")))
#     pyramid(height)

# print(2/2)
