# ----------Linked list
'''
1. Not need to pre allocate space
2. Insertion is easy
'''

# ############## Measuring running time growth: Time complexity ####################
# ---O notation
'''It is the mathematical representation of the time or space require to run a program'''
'''Time takes to execute a program is directly proportional to number of computation doing'''
'''keep fastest growing term and drop constant'''

# ---Complexity
'''
Insert/Delete element at beginning  = O(1)
Insert element at middle  = O(n)
Insert/Delete element at end  = O(n)
Linked list Traveersal = O(n)
Accesssing element by value = O(n)
'''

# -------Implemetation Linked list-----
'''What is Self In __ init __ Python?
The self in keyword in Python is used to all the instances in a class. By using the self keyword, one can easily access all the instances defined within a class, including its methods and attributes. init. __init__ is one of the reserved methods in Python. In object oriented programming, it is known as a constructor.'''
'''__init__  called as class constructor also called initialization method.
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.'''

# ----code for linked list-------
'''
class Node():
# create a node with fiels as data and next
# when we create a node we pass data as parameter
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList():
# define head for linked list
    def __init__(self):
        self.head=None
# create a node and then add at begining of linked list
# 1.create a node using node class 
# 2.parameter is data
# 3.{new_node=Node(data)} and next field is null
# 4.store next of head in new_node chya next madhe {new_node.next=head}
# 5.store new_node in head that is {head=new_node}
    def add_at_begining(self,data):
        new_node=Node(data)      # we create object from node class
                                 # this creates data field with data and next field with none value
        new_node.next=self.head  # self.head madhle refrence new_node.next madhe store karaiche
        self.head=new_node       # ata self.head point karal new_node la
# create a node and then add at end of linked list
    def add_at_end(self,data):      
        new_node=Node(data)      # created new node by creating object from node class
        if self.head==None:      # check Whether Linked list is empty or not
            self.head=new_node   # if yes then make self.head as new_node            
        else:               
            n=self.head          # else follow iteration to reach to last node
            while n.next!=None:  # iterate till we reach last node      
                n=n.next         # once we reached loop is terminated
            n.next=new_node      # last node chya next madhe new_node takaiche 
                                 # new_node chya next madhe None aste
    def remove_end(self):
        if self.head==None:      # check Whether Linked list is empty or not
            print("Linked list is empty") #if yes print 
        else:
            n=self.head          #else assign self.head to n
            while n.next!=None:  #iterate till n.next is equal to None
                n=n.next         #getting n updated with n.next
                                 #once n.next is equal to none loop get terminated
            p=self.head          # assign self.head to another variable p
            while p.next!=n:     #iterate till p.next equals to n 
                p=p.next         #once p.next equals to n loop get terminated
            p.next=None          #removing n(last item of LL) by assigning p.next to None

# Iterate and print elements of linked list
    def print(self):
        if self.head==None:      #check whether linked list is empty or not
            print('Linked list is empty')
        else:
            n=self.head
            while n!=None:
                print(n.data,'-->',end=' ')    
                n=n.next 
            print('Null')        

ll=LinkedList()
ll.add_at_begining(1)
ll.print()
ll.add_at_begining(3)
ll.add_at_end(5)
ll.print()
ll.add_at_end(6)
ll.add_at_begining(12)
ll.print()
ll.remove_end()
ll.print()
'''


# -------------Doubly Linked List
'''
A doubly linked list is a type of linked list in which each node consists of 3 components:
*prev - address of the previous node
data - data item
*next - address of next node
'''

# -----Doubly Linked List Complexity
'''
Doubly Linked List Complexity	Time Complexity	    Space Complexity
Insertion Operation	                  O(1) or O(n)      	O(1)
Deletion Operation	                    O(1)	            O(1)
'''

# -------Doubly Linked List Applications
'''
1.Redo and undo functionality in software.
2.Forward and backward navigation in browsers.
3.For navigation systems where forward and backward navigation is required.
'''



# --------Circular Linked List
'''
A circular linked list is a type of linked list in which the first and the last nodes are also connected to each other to form a circle.
There are basically two types of circular linked list:
1. Circular Singly Linked List:
Here, the address of the last node consists of the address of the first node.

2. Circular Doubly Linked List:
Here, in addition to the last node storing the address of the first node, the first node will also store the address of the last node.
'''

# ------Circular Linked List Complexity
'''
Circular Linked List Complexity	    Time Complexity	    Space Complexity
Insertion Operation	                   O(1) or O(n) 	    O(1)
Deletion Operation	                        O(1)           	O(1)
'''
#-------- Why Circular Linked List?
'''
1.The NULL assignment is not required because a node always points to another node.
2.The starting point can be set to any node.
3.Traversal from the first node to the last node is quick.
'''
#---------- Circular Linked List Applications
'''
1.It is used in multiplayer games to give a chance to each player to play the game.
2.Multiple running applications can be placed in a circular linked list on an operating system. 
The os keeps on iterating over these applications.
'''




# ----------practice
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Linkedlist():
    def __init__(self):
        self.head=None

    def add_at_begining(self,data):
        new_node = Node(data)
        new_node.next=self.head
        self.head=new_node
        

    def add_at_end(self,data):
        new_node=Node(data)
        n=self.head
        while n.next!=None:
            n=n.next
        n.next=new_node
        new_node.next=None
    
    def is_empty(self):
        if self.head==None:
            return True

    def add_after_given_value(self,value,data):
        
        new_node=Node(data)
        n=self.head
        while n.data!=value:
            n=n.next
        new_node.next=n.next
        n.next=new_node    

    def print_Linkedlist(self):
        print('linkedlist: ',end='')
        n=self.head
        while n!=None:
            print(n.data,end='-->')
            n=n.next
        print(n,'\n')

ll=Linkedlist()
while True:
    print('1.Add at begining\n2.Add after given value\n3.Add at end\n4.Check is empty\n5.Print\n6.Exit')
    ch=int(input('Enter choice: '))
    if ch==1:
        data=int(input('Enter data: '))
        ll.add_at_begining(data)
        print(data,'Added at begining!\n')

    if ch==2:
        data=int(input('Enter data: '))
        value=int(input('Enter value after which you want to add your data: '))
        ll.add_after_given_value(value,data)
        print(data,'Added after',value,'\n')

    if ch==3:
        data=int(input('Enter data: '))
        ll.add_at_end(data)
        print(data,'Added at end!\n')

    if ch==4:
        if ll.is_empty()==True:
            print('Empty!\n')
        else:
            print('Not Empty!\n')

    if ch==5:
        ll.print_Linkedlist()

    if ch==6:
        print('Exit!')
        break

'''