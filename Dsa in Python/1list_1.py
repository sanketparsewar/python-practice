'''-----------List in python is dynamic array---------'''
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
l.insert() take index and value as parameter complexity O(n)
l.pop() delete last element
l.remove() delete element complexity O(n)
l.reverse() reverse list
l.sort() sort list '''

# -------------What is the difference between sort and sorted list?
'''
sort() sorts the list and replaces the original list, whereas 
sorted(list) returns a sorted copy of the list, without changing the original list.
'''


# ############## Measuring running time growth: Time complexity ####################
# ---O notation
'''It is the mathematical representation of the time require to run a program'''
'''Time takes to execute a program is directly proportional to number of computation doing'''
'''keep fastest growing term and drop constant'''

# ---Complexity
'''
Indexing = O(n)
Insert element at beginning  = O(n)
Delete element at beginning  = O(n)
Insert/Delete element at end  = O(1) - amortized{is said beacuse if you have dynamic array and you reached capacity you have to copy those elements which require additional cost}  
Insert element at middle  = O(n)
'''

# ------- program to get square of numbers in a list
# def get_squared_numbers(numbers):
#     squared_numbers = []
#     for n in numbers:
#         squared_numbers.append(n*n)
#     print(squared_numbers)
# numbers = [2,5,8,9]
# get_squared_numbers(numbers)
'''keep fastest growing term standard linerar euation is [a*n + b] --> The time complexity of this programm is O(n) because it does n nnumber of iteration in for loop for n number of elements'''


# -------multiplication of 2 items from two list for given index
# def Multiply(a,b,index):
#     Mul = a[index]*b[index]
#     print(f'a*b of index {index} = {Mul}')
# a=[2,4,6,8,10]
# b=[1,3,5,7,9]
# Multiply(a,b,2)
'''keep fastest growing term standard linerar euation is [a] --> The time complexity is O(1) because of accessing directly that particuar element without any further iteration'''


# ------find dupliate of number from list
# numbers = [3,6,2,4,3,6,8,9]
# for i in range (len (numbers)):
#     for j in range(i+1, len (numbers)):
#         if numbers[i] == numbers [j]:
#             print(numbers[i] , " is a duplicate")
#             break
'''keep fastest growing term standard linerar euation is [a*n^2 + b] --> Time complexity is O(n^2) beacuse for two for loops and comparing numbers'''


# ------find dupliate of number from list
# numbers = [3,6,2,4,3,6,8,9]
# duplicate = None
# for i in range (len (numbers)):
#     for j in range(i+1, len (numbers)):
#         if numbers[i] == numbers [j]:
#             duplicate = numbers [i]
#             break
# for i in range (len (numbers)):
#     if numbers [i] == duplicate:
        # print(i)
'''keep fastest growing term standard linear equation is [a*n^2 + b*n + c ] --> Time complexity is O(n^2) beacuse when value of n is very large b⋆n + c becomes irrevalant '''
'''
1. Keep fastest growing term
2. Drop constants
Big O refers to very large value of n. Hence if you have a function like,
time = 5*n² + 3*n + 20
When value of n is very large b⋆n + c become irrevalant
Example: n = 1000
time = 5*1000² + 3*1000 + 20
time = 5000000 + 3020 '''



# ################## Measuring space growth: Space complexity  ################ 


#------ 4 9 15 21 34 57 68 91 Search index for 68
# numbers=[4, 9, 15, 21, 34, 57, 68, 91]
# for i in range (len (numbers)):
#     if numbers [i] == 68:
#         print('index fo 68 is' ,i)
'''The space complexity for this program is O(n) and it iterates every element in the list'''
'''This programm can be optimized using "----Binary search----" because if we have million numbers then we have to do million iterations so sapce and time both are used more, to avoid this binary search can be used ''' 


#------ 4 9 15 21 34 57 68 91 Search for 68
# 4 9 15 21 34 57 68 91 Iteration 1 = n/2
'''get middle element 21'''
# 4 9 15 21 34 57 68 91 Iteration 2 = (n/2)/2 = n/2²
'''left is discared and get middle of right as 57'''
# 4 9 15 21 34 57 68 91 Iteration 3 = (n/2²)/2 = n/2³
'''left is discarded and get middle of right as 68 and we found it'''
#  for K iteration you have to do n/2^k operations
'''
Iteration k = n/2^k
1 = n/2^k
n = 2^k
log₂ n = log₂ 2^k
log₂ n = k * log₂ 2
K = log n → O(log n)   '''
'''--------Complexity of Binary seacrh is O(log n)-------- '''
# For 8 elements we get
# K = O(log n) → log₂8 ⇒ log₂2³ ⇒ 3* log₂2 → 3 iterations


# xxxxxxxxx---------------Examples--------------xxxxxxxxxxxxx

# ------------Create a list
'''
exp=[2200,2350,2600,2130,2190]
print(exp[1]-exp[0])
print(exp[1]+exp[0]+exp[2])
print(2000 in exp)
exp.append(1980)
print(exp)
exp.remove(2130)
exp.insert(3,1930)
print(exp)
'''

# ----------Python program to interchange first and last elements in a list
# l=[1,2,4,7,3,2]
# l[0],l[len(l)-1] = l[len(l)-1], l[0]
# print(l)


# ------python program to swap two elements in a list
'''
lis=[23,56,98,15,42,6,23,76,87,98]
pos1=int(input(f"enter position of 1st value in range 1 to {len(lis)} ")) - 1
pos2=int(input(f"enter position of 2st value in range 1 to {len(lis)} ")) - 1
print("previous=",lis)
lis[pos1],lis[pos2]=lis[pos2],lis[pos1]
print("swaped = ",lis)
'''


# ---------Python | Ways to find length of list
# lis=[23,56,98,15,42,6,23,76,87,98]
# print(len(lis))
# count=0
# for _ in lis:
#     count+=1
# print(count)


#-------- print list or n numbers taken input from user
# nums=[]
# for _ in range(int(input("No. of items: "))):
#     nums.append(int(input("enter number ")))
# print(nums)


# -------List and its methods
'''
heros=["Spider man","Thor","hulk",'iron man','captain america']
print(len(heros))
heros.append('black panther')
print("added item:",heros)
heros.remove('black panther')
heros.insert(3,'black panther')
print("added item at 3rd index:",heros)
heros[1:3]=['doctor strange']
print("changed item from 1-3 item:",heros)
heros.sort()
print('sorted:',heros)
'''

# --------Getting even and odd from entered range
'''
num1=[]
num2=[]
max_val=int(input("Enter max value to get even and odd between it="))
for i in range(1,max_val):
    if i%2==0:
        num1.append(i)
    else:
        num2.append(i)
print("list of even numbers",num1)
print("list of odd numbers",num2)
'''

# -----------Python – Check if two lists have atleast one element common
'''
num1=[1,2,9,6,3,4,8,5,2]
num2=[12,15,28,32,96,48,2,5,4]
for n1 in num1:
    for n2 in num2:
        if n1==n2:
            print('common value',n1)
            break
'''

# --------------Python – Assigning Subsequent Rows to Matrix first row elements
'''
matrix=[[2,36,4,1],[7,9,8,5],[5,4,6,8],[3,4,8,6],[9,4,5,7]]
matrix_li=[]
for i in range(len(matrix[0])):
    item=matrix[0][i] , matrix[i+1]
    matrix_li.append(item)
new_matrix=dict(matrix_li)
print(new_matrix)
'''

# -------- Adding and Subtracting Matrices in Python
# [2, 6, 2]   [1, 2, 4]
# [7, 9, 7] + [4, 5, 6]
# [5, 4, 6]   [3, 1, 4]
'''
matrix1 = [[2, 6, 4], [7, 9, 7], [5, 4, 6]]
matrix2 = [[1, 2, 2], [4, 5, 6], [3, 1, 4]]
ADDITION
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        print(matrix1[i][j]+matrix2[i][j],end=' ')
    print()
 SUBTRACT   
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        print(matrix1[i][j]-matrix2[i][j],end=' ')
    print()
'''
