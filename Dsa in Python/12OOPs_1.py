# -----------creating class and its objects---------
'''
class Student():
    pass            #written when we didt have any thing here

sanket=Student()    # sanket is the object in class Student
parsewar=Student()  # parsewar is the object in class Student

sanket.rollno=51      #rollno, std, div are the instance variables of object sanket
sanket.std="final year"
sanket.div='A'
print(sanket.div)

parsewar.rollno=52   #rollno, std, subject are the instance variables of object parsewar
parsewar.std='Third year'
parsewar.subjects=['English','Math','Physics']
print(parsewar.std)  #accessing instances using object
'''


# ----------accessing class variable using class name and class objects -----------
'''
class Employee():
    no_of_Employee=10
    pass

rohan=Employee()
human=Employee()

rohan.name="Rohan"
rohan.salary=5454
rohan.role="Teacher"

human.name="Human"
human.salary=999
human.role="Assistant"

print(rohan.role)
print(rohan.no_of_Employee) #using class object we can access class variable
rohan.no_of_Employee=15    #object cannot changes the class variable value but creates a new instance for that object
print(rohan.no_of_Employee)
print(rohan.__dict__)         #rohan.__dict__ prints all the instances created for this particular object
print(Employee.no_of_Employee) #using class name also we can access class variable
Employee.no_of_Employee=98    #only using class name that is Employee class variable value is changed
print(Employee.no_of_Employee)
print(Employee.__dict__)         #this prints all the instances created for this particular object
print(human.no_of_Employee)
'''


# ---------- What is self ---------
'''
class Employee():
    no_of_Employee=10
        
    # creating print detail method for printing details of employee object rohan and human
    def printdetails(self):    #self vo hai jiski bat ki ja rahi  hai
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}.'

rohan=Employee()
human=Employee()
rohan.name="Rohan"
rohan.salary=5454
rohan.role="Teacher"

human.name="Human"
human.salary=999
human.role="Assistant"

print(rohan.printdetails())  #self use kelya mule ithla rohan prindetails la as an argument mhanun assign hoto
print(human.printdetails())  #self use kelya mule ithla human prindetails la as an argument mhanun assign hoto
'''


# --------creating constructor ---------
'''
class Employee():
    no_of_Employee=10
    
    # constructor vo hota hai jo object banate wakt jo kam hota hai vo ye karta hai
    def __init__(self,aname,asalary,arole):
        self.name=aname             #'name' is instance variable name and 'aname' is argument
        self.salary=asalary
        self.role=arole
        
    # creating print detail method for printing details of employee object rohan and human
    def printdetails(self):    #self vo hai jiski bat ki ja rahi  hai yani jis object ki bat ki ja rahi hai
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}.'


rohan=Employee('Rohan',455,'Teacher')       #class chya nava madhe dilele le argument hamesha init la jatat
human=Employee('Human',2121,'Assistant')    #class ke name me diye gaye argument sare init ko jate hai
# rohan.name="Rohan"
# rohan.salary=5454
# rohan.role="Teacher"

# human.name="Human"
# human.salary=999
# human.role="Assistant"

print(rohan.printdetails())  #ithla rohan prindetails la as an argument mhanun assign hoto self use kelya mule 
print(human.printdetails())  #ithla human prindetails la as an argument mhanun assign hoto self use kelya mule 
'''


# ---------Class methods Decorators-------
'''
Decorators: Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. 
Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
'''
'''
class Employee():
    no_of_Employee=10
    
    # constructor vo hota hai jo object banate wakt jo kam hota hai vo ye karta hai
    def __init__(self,aname,asalary,arole):
        self.name=aname             #'name' is instance variable name and 'aname' is argument
        self.salary=asalary
        self.role=arole
        
    # creating print detail method for printing details of employee object rohan and human
    def printdetails(self):    #self vo hai jiski bat ki ja rahi  hai
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}.'

    # ---- Using decorator ------
    """
    Convert a function to be a class method.
    A class method receives the class as implicit first argument, just like an instance method receives the instance. 
    To declare a class method, use this idiom:
    class C:
        @classmethod 
        def f(cls, arg1, arg2, ...):
    """
    
    @classmethod
    def change_employee(cls,new_employes):               #cls vo class hai jiska instance rohan hai yani iss case me Employee hai cls
        cls.no_of_Employee=new_employes
        return

rohan=Employee('Rohan',455,'Teacher')       #class chya nava madhe dilele le argument hamesha init la jatat
human=Employee('Human',2121,'Assistant')    #class ke name me diye gaye argument sare init ko jate hai

print(rohan.no_of_Employee)        
rohan.change_employee(20)           #decorator ki madat se change_employee function create kiya jiski madat se class ka object yani rohan class ke variable yani no_of_Employee ki value change kar sakta hai 
print(rohan.no_of_Employee)

print(rohan.printdetails())  #ithla rohan prindetails la as an argument mhanun assign hoto
print(human.printdetails())  #ithla human prindetails la as an argument mhanun assign hoto

'''

# ----------Encapsulation
'''
Encapsulation is used to restrict access to methods and variables. 
In encapsulation, code and data are wrapped together within a single unit from being modified by accident.
'''


# ---------Data Abstraction
'''
Data abstraction and encapsulation are synonymous as data abstraction is achieved through encapsulation.
Abstraction is used to hide internal details and show only functionalities. Abstracting something means to give names to things, so that the name captures the basic idea of what a function or a whole program does.'''

# --------Inheritance
'''What is inheritance in Python?
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class. 
Child class is the class that inherits from another class, also called derived class.
'''

# ---------There are five types of inheritances:
'''
1.Single Inheritance
2.Multiple Inheritance
3.Multilevel Inheritance
4.Hierarchical Inheritance
5.Hybrid Inheritance
'''


# --------1.Single Inheritance
'''This type of inheritance enables a subclass or derived class to inherit properties and characteristics of the parent class'''
'''
class Employee():
    def __init__(self,name,std):
        self.name=name
        self.std=std

    def print_details(self):
        return f'Name is {self.name}, Class is {self.std}.'


class Programmer(Employee):       #Sinhle inheritance using this we can access all the functions of Employee class
    def print_prog_details(self):
        return f'Programmer\'s name is {self.name}.'


rohan=Employee('Rohan',2)         #object of Employee class
rohan=Programmer('Rohan',4545)     #object of programmer class

print(rohan.print_prog_details())      #this function is of programer class
print(rohan.print_details())           #this function is of Employee class accessed by object of programmer class
'''


#------------------ Multiple Inheritance
'''This inheritance enables a child class to inherit from more than one parent class.
This type of inheritance is not supported by java classes, but python does support this kind of inheritance. 
It has a massive advantage if we have a requirement of gathering multiple characteristics from different classes.
'''
# --------Example-1
'''
#parent class 1
class A:
    demo1=0
    def fun1(self):
        print(self.demo1)

#parent class 2
class B:
    demo2=0
    def fun2(self):
        print(self.demo2)

#child class
class C(A, B):              #class c is inheriting the properties of class A and class B
    def fun3(self):
        print(“Hey there, you are in the child class”)

# Main code
c = C()
c.demo1 = 10
c.demo2 = 5
c.fun3()
print(“first number is : “,c.demo1)
print(“second number is : “,c.demo2)
'''


# ------Example-2
'''
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))  
'''


# ----------Multilevel Inheritance
'''In multilevel inheritance, the transfer of the properties of characteristics is done to more than one class hierarchically. '''
'''
class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#The child class Dog inherits the base class Animal  
class Dog(Animal):           # class Dog is inheriting class Animal
    def bark(self):  
        print("dog barking")  
#The child class Dogchild inherits another child class Dog  
class DogChild(Dog):        # class DogChid is inheriting class Dog
    def eat(self):  
        print("Eating bread...")  
d = DogChild()  
d.bark()  
d.speak()  
d.eat()  
'''


# ------------Hierarchical Inheritance


# --------------Public, Protected and Private
'''
Example:
Public - agar koi cheese apko sabhi logo ko dikhani hai to ghar ke bahar chipkaenge 
Protected - agar ghar ke logon ko dikhani hai to ghar ke ander chipkange
Private - sirf khud ko dekhni hai toh room me chipkaenge
'''
'''
class Employee():
    no_of_Employee=10                   #ye public variable hai
    _var=3                              #_var ye protected variabl hai. 
    __num=20                            #__num ye private variable hai
    
    # constructor vo hota hai jo object banate wakt jo kam hota hai vo ye karta hai
    def __init__(self,aname,asalary,arole):
        self.name=aname             #'name' is instance variable name and 'aname' is argument
        self.salary=asalary
        self.role=arole
        
    # creating print detail method for printing details of employee object rohan and human
    def printdetails(self):    #self vo hai jiski bat ki ja rahi  hai yani jis object ki bat ki ja rahi hai
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}.'


rohan=Employee('Rohan',455,'Teacher')       #class chya nava madhe dilele le argument hamesha init la jatat

print(rohan.no_of_Employee)              #public variable direct access kar sakte hai
print(rohan._var)                        #protected variable ko direct access kar sakte hai
print(rohan._Employee__num)             #privat evariable ke liye (_'name of class'__num) ve naming follow karna padta hai
'''


# ----------Super() and overriding of methods in classes---------------
'''agar hume super class ke variables ko access karna hai toh hum super() ko istemal kar sakte hai'''
'''
class A:
    classvar1='I am a class variable in class A'
    def __init__(self):
        self.var1='I am inside class A constructor'
        self.classvar1='Instance vr in class A'
        self.special='Special'

class B(A):
    classvar1="I am a class variablel in class B"
    def __init__(self):
        self.var1='I am inside class B constructor'
        self.classvar1='Instance vr in class B'
        super().__init__()           #class a cha instance variabl eaccess karte ani value dete

a=A()
b=B()
print(b.classvar1) 
# print(b.classvar2)
'''


# -------Diamond problem in programming
'''Diamond problem occurs due to using multiple inheritance while solving a problem.
            A
           / \
          /   \
         B     C   
          \   /
           \ /
            D
This are the four class B & C inherits class A , class D inhereits class B & C 
'''

# ------Dunder methods
'''
The methods which start and ends with ' __ '.
In Python, dunder methods are methods that allow instances of a class to interact with the built-in functions and operators of the language. 
The word “dunder” comes from “double underscore”, because the names of dunder methods start and end with two underscores, for example __str__ or __add__ .
'''