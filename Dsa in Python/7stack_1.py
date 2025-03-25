# ------Stack using list------
'''
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. 
In stack, a new element is added at one end and an element is removed from that end only. 
The insert and delete operations are often called push and pop.
'''

# ---------Use cases----------
'''
1.Function calling in any programming language is managed using stack.
2.Undo (ctrl+Z) functionality in any  editor uses stack to track down last set of operations
'''

# ------------Applications of Stack Data Structure ------------
'''
1.To reverse a word - Put all the letters in a stack and pop them out. Because of the LIFO order of stack, you will get the letters in reverse order.
2.In compilers - Compilers use the stack to calculate the value of expressions like 2 + 4 / 5 * (7 - 9) by converting the expression to prefix or postfix form.
3.In browsers - The back button in a browser saves all the URLs you have visited previously in a stack. 
Each time you visit a new page, it is added on top of the stack. When you press the back button, the current URL is removed from the stack, and the previous URL is accessed.
'''

# ---------The functions associated with stack are-------:
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


# ############## Measuring running time or space growth: complexity ####################
# ---O notation
'''It is the mathematical representation of the time require to run a program'''
'''Time takes to execute a program is directly proportional to number of computation doing'''
'''keep fastest growing term and drop constant'''

# ---Complexity
'''
Push/Pop element: O(1)
Search element by value: O(n)
'''

# -----Stack implementation-----
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
