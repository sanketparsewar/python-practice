# ------- Queue
# Key differences between Priority Queue and Queue:
'''
1. A queue is a useful data structure in programming. It is similar to the ticket queue outside a cinema hall, where the first person entering the queue is the first person who gets the ticket.
2. In Queue, the oldest element is dequeued first. While, in Priority Queue, an element based on the highest priority is dequeued.
3. When elements are popped out of a priority queue the result obtained is either sorted in Increasing order or in Decreasing Order. While, when elements are popped from a simple queue, a FIFO order of data is obtained in the result.'''


#----------- Operations associated with queue ------ 
'''
A queue is an object (an abstract data structure - ADT) that allows the following operations:
Enqueue: Add an element to the end of the queue
Dequeue: Remove an element from the front of the queue
IsEmpty: Check if the queue is empty
IsFull: Check if the queue is full
Peek: Get the value of the front of the queue without removing it
'''

# ------------ Applications of Queue  ------------
'''
1.CPU scheduling, Disk Scheduling
2.When data is transferred asynchronously between two processes.The queue is used for synchronization. For example: IO Buffers, pipes, file IO, etc
3.Handling of interrupts in real-time systems.
4.Call Center phone systems use Queues to hold people calling them in order.
'''

# ---------Implementation using collections.deque-----------
'''However, lists are quite slow for this purpose because inserting or deleting an element at the beginning requires shifting all of the other elements by one, requiring O(n) time.
Queue in Python can be implemented using deque class from the collections module.
Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. 
Instead of enqueue and deque, append() and popleft() functions are used.
'''

# ############## Measuring running time or space growth: complexity ####################
# ---O notation
'''It is the mathematical representation of the time require to run a program'''
'''Time takes to execute a program is directly proportional to number of computation doing'''
'''keep fastest growing term and drop constant'''

# ---Complexity if implemented using List
'''
Access item - Time complexity : O(n)
Search item - Time complexity : O(n)
Enqueue (append()): Adds an item to the queue - Time Complexity : O(n)
Dequeue (pop()): Removes an item from the queue - Time Complexity : O(n)
'''

# ---Complexity if Implemented using collections.dequeue
'''
Enqueue (append()) : Adds an item to the queue - Time Complexity : O(1)
Dequeue (popleft()): Removes an item from the queue - Time Complexity : O(1)
'''



# ------------Queue implemenatation using List------
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


# -----------Queue implementation using class Queue
'''
class Queue():
    def __init__(self):     #initializing queue
        self.queue=[]
    # Adding item in queue
    def enqueue(self,item):
        self.queue.append(item)
        # print(item,'added at rare!')
    # Remove item from queue
    def dequeue(self):
        if len(self.queue)==0:
            print("Queue is empty")
        else:
            self.queue.pop(0)
        print('Item removed from top!')
    # Display Queue
    def display(self):
        print('Queue:')
        for i in range(len(self.queue)):
            if i==0:
                print(self.queue[i],'<--Top')
            elif i==(len(self.queue)-1):
                print(self.queue[i],'<--rare')
            else:
                print(self.queue[i])
   
q=Queue()
q.enqueue(20)
q.enqueue(56)
q.enqueue(87)
q.enqueue(98)
q.display()
q.dequeue()
q.display()
q.enqueue(80)
q.display()
'''


# ---------Implementation of queue using collections.dequeue
'''
from collections import deque
class Queue():
    def __init__(self):
        self.queue=deque()
    def enqueue(self,item):
        self.queue.appendleft(item)
    def dequeue(self):
        if len(self.queue)==0:
            print('Empty Queue!')
        else:
            self.queue.pop()
    def display(self):
        if len(self.queue)==0:
            print('Empty Queue!')
        else:
            print(self.queue)

q=Queue()
q.display()
q.enqueue(26)
q.enqueue(246)
q.enqueue(16)
q.enqueue(945)
q.enqueue(246)
q.enqueue(265)
q.display()
q.dequeue()
q.display()
'''



# ------------Circular queue ------------
'''
A circular queue is the extended version of a regular queue where the last element is connected to the first element. Thus forming a circle-like structure.
'''
# ---------Circular Queue Works
'''Circular Queue works by the process of circular increment i.e. 
when we try to increment the pointer and we reach the end of the queue, we start from the beginning of the queue.
Here, the circular increment is performed by modulo division with the queue size.
'''
# --------Circular Queue Operations
'''The circular queue work as follows:
two pointers FRONT and REAR
FRONT track the first element of the queue
REAR track the last elements of the queue
initially, set value of FRONT and REAR to -1
'''
# ------Circular Queue Complexity Analysis
'''The complexity of the enqueue and dequeue operations is O(1) for (array implementations).'''
# --------Applications of Circular Queue
'''
1.CPU scheduling
2.Memory management
3.Traffic Management
'''



# ---------Priority Queue ------------------
'''
A priority queue is a special type of queue in which each element is associated with a priority value. 
And, elements are served on the basis of their priority. 
That is, higher priority elements are served first.
However, if elements with the same priority occur, they are served according to their order in the queue.
'''
#-------- Assigning Priority Value
'''
Generally, the value of the element itself is considered for assigning the priority. 
For example,
The element with the highest value is considered the highest priority element.
However, in other cases, we can assume the element with the lowest value as the highest priority element.
We can also set priorities according to our needs.
'''
# -------Priority Queue Applications
'''Some of the applications of a priority queue are:
1.Dijkstra's algorithm
2.for implementing stack
3.for load balancing and interrupt handling in an operating system
4.for data compression in Huffman code
'''