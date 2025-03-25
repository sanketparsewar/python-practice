'''function = A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
Example: sorted(iterable[,key,reverse]) , reversed(iterator) '''

'''Method = A method is a function that “belongs to” an object. (In Python, the term method is not unique to class instances: other object types can have methods as well. For example, list objects have methods called append, insert, remove, sort, and so on.
Examples: List.append() Add a single element to the end of the list.
List.clear() Removes all Items from the List.
'''



# Lists
# Dictionary
# Tuple
# Set
# Queues
# Linked List
# Stack



# -----List = values can be added or removed or modified 
# l=[i for i in range(10)]
# print(l)
'''methods in list = 
l.append() Add a single element to the end of the list
l.clear() Removes all Items from the List
l.copy() returns a shallow copy of the list
l.count() returns count of the element in the list
l.extend() adds iterable elements to the end of the list
l.index() returns the index of the element in the list
l.insert() insert element at desired index
l.pop() pop last element
l.remove() remove desired element
l.reverse() reverse list
l.sort() sort in asscending order by default
'''


# ------Dictionary = elements are in form of key value pairs
# d={'mon':2,'tue':3,'wed':4,'thu':6,'fri':9,'sat':10}
# print(d.keys())
# print(d.values())
# print(d)
'''Methods in dictionary: 
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values() Returns a list of all the values in the dictionary
'''



# --------Tuple = immutable (values cannot be modified or removed or changed)
# t=('mon',45,'tue',10,50,66)
# print(t)
'''Methods in tuple:
t.count()	Returns the number of times a specified value occurs in a tuple
t.index()	Searches the tuple for a specified value and returns the position of where it was found'''


# ---------Set = values in set cannot be duplicate -----
# s={'Jan','Jan','Feb','Mar','April','May','June','July','Aug','Sep','Oct','Nov','Dec'}
# num={10,1,2,5,8,3,2,1,4,45,12,1,4,121,211,0}
# print(s) # duplicate values are printed only once 
# print(sorted(s)) #sorted according to alphabetical order
# print(num)
# print(max(num))
'''Methods in set:
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two or more sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with another set, or any other iterable'''


# ------- Queue---------
# Key differences between Priority Queue and Queue:
'''1. In Queue, the oldest element is dequeued first. While, in Priority Queue, an element based on the highest priority is dequeued.
2. When elements are popped out of a priority queue the result obtained is either sorted in Increasing order or in Decreasing Order.
While, when elements are popped from a simple queue, a FIFO order of data is obtained in the result.'''


# --------Queue Implementation -------------
'''
import cowsay
queue=[]
def is_empty(queue):
    if len(queue)==0:
        print("Queue is empty!")
    else:
        print('Queue is not empty!')
    
def push(item):
    queue.append(item)
    
def pop():
    if len(queue)==0:
        print("Queue is empty condition Underflow!!")
    else:
        queue.pop(0)
        print("First element removed successfully!!")

def display(queue):
    if len(queue)==0:
        print('Queue is empty!')
    else:   
        for i in range(len(queue)):
            if i==0:
                print(queue[i] + '<--Top')
            else:
                print(queue[i])

if __name__=='__main__':
    while True:
        print("QUEUE implementation")
        print('1.Check empty')
        print('2.Push')
        print('3.Pop')
        print('4.Display queue')
        print('5.Exit')
        ch=int(input("Enter choice (1-5): "))
        if ch==1:
            is_empty(queue) 
            input("Press enter key to continue.........") 
        elif ch==2:
            item=input("Enter value to push: ")
            push(item)
            print("Added successfully!")
            input("Press enter key to continue.........") 
        elif ch==3:
            pop()
            input("Press enter key to continue.........") 
        elif ch==4:
            display(queue)
            input("Press enter key to continue.........")
        elif ch==5:
            print('Exit successfull !!')
            break
        else:
            cowsay.daemon('Andhe dikhta nai kya!!')
            input("Press enter key to continue.........")
        print('\n')
'''

# ----------Linked list
'''What is Self In __ init __ Python?
The self in keyword in Python is used to all the instances in a class. 
By using the self keyword, one can easily access all the instances defined within a class, including its methods and attributes. init.
__init__ is one of the reserved methods in Python. In object oriented programming, it is known as a constructor.
__init__  called as class constructor also called initialization method.
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.'''


# ----------Linked list Implementation -----------
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



# ------Stack ------
'''
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. 
In stack, a new element is added at one end and an element is removed from that end only. 
The insert and delete operations are often called push and pop.
'''
# ---------The functions associated with stack are:
'''
empty() - Returns whether the stack is empty - Time Complexity: O(1)
size() - Returns the size of the stack - Time Complexity: O(1)
top() / peek() - Returns a reference to the topmost element of the stack - Time Complexity: O(1)
push(a) - Inserts the element 'a' at the top of the stack -Time Complexity: O(1)
pop() - Deletes the topmost element of the stack - Time Complexity: O(1)
IsEmpty(): Check if the stack is empty
IsFull(): Check if the stack is full
Peek(): Get the value of the top element without removing it
'''
# --------Stack implementation using list
'''
st=[]
def push(item):
    st.append(item)
    print(st)
def pop():
    if len(st)==0:
        print("Stack is empty!")
    else:
        i=st.pop()
        print('Item poped!',i)
        print(st)
def display():
    print('Stack:',st)

while True:
    print('\n1.Push')
    print('2.Pop')
    print('3.Display')
    print('4.Exit')
    ch=int(input("Enter choice: "))
    if ch==1:
        value=input("Enter value: ")
        push(value)
        print('Data added successfully!!')
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print("Enter valid input!!!")
'''

