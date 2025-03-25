# ----------Python program to interchange first and last elements in a list
# l=[1,2,4,7,3,2]
# l[0],l[len(l)-1] = l[len(l)-1], l[0]
# print(l)



# ------python program to swap two elements in a list
# lis=[23,56,98,15,42,6,23,76,87,98]
# pos1=int(input(f"enter position of 1st value in range 1 to {len(lis)} ")) - 1
# pos2=int(input(f"enter position of 2st value in range 1 to {len(lis)} ")) - 1
# print("previous=",lis)
# lis[pos1],lis[pos2]=lis[pos2],lis[pos1]
# print("swaped = ",lis)


# ---------Python | Ways to find length of list
# lis=[23,56,98,15,42,6,23,76,87,98]
# print(len(lis))
# count=0
# for _ in lis:
#     count+=1
# print(count)


# ---------Minimum of two numbers in Python
# a=2
# b=6
# if a<b:
#     print("a smaller")
# else:
#     print("b smaller")


# ---------Python program to check whether the string is Symmetrical or Palindrome
# s="abcabc"
# half=(len(s)/2)
# if s[:int(half)]==s[int(half):]:
#     print(s,"is symmetrical")
# elif s==s[::-1]:
#     print(s,"is palindrome")
# else:
#     print("no")


# ------Reverse words in a given String in Python
# s='This is a sample string'
# print(s[::-1])


# -------Ways to remove i’th character from string in Python
# s='This is a sample string'
# i=int(input("index to remove:"))-1
# for j in range(len(s)):
#     if j==i:
#         pass
#     else:
#         print(s[j],end='')


# ----------Find length of a string in python
# s='This is a sample string'
# count=0
# for _ in s:
#     count+=1
# print(count)


# -----------Python program to print even length words in a string
# s="this is the sample string in python file"
# st=s.split(' ')
# for word in st:
#     if len(word)%2==0:
#         print(word)


# --------Python – Maximum and Minimum K elements in Tuple
'''tup=(26,31,36,77,90,81,12,56,33,14,45)
print(tup)
li=list(tup)
li.sort()
k=int(input("enter "))
req=[]
req1=[]
for i in range(1,len(li)+1):
    if i<=k:
        req.append(li[i-1])
        req1.append(li[-i])

tup1=tuple(req)
tup2=tuple(req1)
print(tup1+tup2[::-1])
'''


# ----------Python – Sum of tuple elements
# num=(23,65,9,8,9,5,4,8,85)
# s=sum(num)
# print(s)


# ------------ Python – Row-wise element Addition in Tuple Matrix
'''test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
cus_eles = [6, 7, 8]
for indx,val in enumerate(test_list):
    for sub in val:
        sub=sub + (cus_eles[indx],)
        print(sub)
'''
# OR

'''test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
cus_eles = [6, 7, 8]
req=[[sub+(cus_eles[indx],)for sub in val] for indx,val in enumerate(test_list)]
print(str(req))
'''


# -------Create a list of tuples from given list having number and its cube in each tuple
'''num=[2,4,6,16,9,3,27,81,14]
li=[]
for i in num:
    for j in num:
        if i*i==j:
            val=(i,j)
            li.append(val)
print(li)
'''


# --------- Python | Sort Python Dictionaries by Key or Value
'''month = {'jan': 2, 'feb': 3, 'march': 5, 'april': 9, 'may': 6, 'june': 8}
month_key=month.keys()
month_key_li=list(month_key)
month_key_li.sort()
month_d=[]
for i in month_key_li:
    month_dict_item=(i,month[i])
    month_d.append(month_dict_item)
month_dict=dict(month_d)
print(month_dict)
'''


# -------Handling missing keys in Python dictionaries
'''month={'jan':2,'feb':3,'march':5,'april':9,'may':6,'june':8}
try:
    key=input("enetr key to get value ")
    print(key, month[key])
except :
    print("key not found")
'''


# ----Python dictionary with keys having multiple inputs
'''month={'jan':2,'feb':3,'march':5,'april':9,'may':6,'june':8}
num=int(input("number of keys "))
for i in range(num):
    key=input("enter key ")
    print(key,month[key])
'''


# -------Python program to find the sum of all items in a dictionary
# month={'jan':2,'feb':3,'march':5,'april':9,'may':6,'june':8}
# month_value=month.values()
# month_value_li=list(month_value)
# print('sum',sum(month_value_li))


# ------python program to find the size of a Dictionary
# month={'jan':2,'feb':3,'march':5,'april':9,'may':6,'june':8,'july':17,'august':13}
# print(month.__sizeof__(),'bytes')


# ----------- Find the size of a Set in Python
# days={'monday','tuesday','wedmnesday','thursday','friday','saturday'}
# print(days.__sizeof__(),'bytes')


# ------Iterate over a set in Python
# days={'monday','tuesday','wedmnesday','thursday','friday','saturday'}
# for day in days:
#     print(day)


# -----------Python – Maximum and Minimum in a Set
# nums={12,22,36,45,14,10,25,18,98,78,11,26}
# nums_sorted=sorted(nums)
# print(nums_sorted)
# print("min=",nums_sorted[0],', max=',nums_sorted[len(nums_sorted)-1])


# ------- Python – Remove items from Set
'''nums={12,22,36,45,14,10,25,18,98,78,11,26}
items=input("Enter item to remove: ")
item=items.split(' ')
print(nums)
for i in item:
    for num in nums:
        if num==int(i):
            nums.remove(num)
            break
print(nums)
'''


# -----------Python – Check if two lists have atleast one element common
'''num1=[1,2,9,6,3,4,8,5,2]
num2=[12,15,28,32,96,48,2,5,4]
for n1 in num1:
    for n2 in num2:
        if n1==n2:
            print('common value',n1)
            break
'''

# --------------Python – Assigning Subsequent Rows to Matrix first row elements
'''matrix=[[2,36,4,1],[7,9,8,5],[5,4,6,8],[3,4,8,6],[9,4,5,7]]
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

'''matrix1 = [[2, 6, 4], [7, 9, 7], [5, 4, 6]]
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

# -------Python – Row-wise element Addition in Tuple Matrix
'''matrix = [[2, 6, 4], [7, 9, 7], [5, 4, 6]]
for i in range(len(matrix)):
    s=sum(matrix[i])
    print(s)
'''

# -------Create an n x n square matrix, where all the sub-matrix have the sum of opposite corner elements as even
# matrix[n]==matrix[n][]


#-------- How to get list of parameters name from a function in Python?
"""signature = Get a signature object for the passed callable."""
"""inspect = Get useful information from live Python objects."""
"""getargspec = Get the names and default values of a function's parameters."""
# import inspect
# def add(a,b):
#     return a+b
# print(inspect.signature(add))
# print(inspect.signature(len))
# print(inspect.getargspec(add))


# -------How to Print Multiple Arguments in Python?
# An argument is a value that is passed within a function when it is called.They are independent items, or variables, that contain data or codes. During the time of call each argument is always assigned to the parameter in the function definition.
'''
def add(a,b):
    print('sum is', a+b)
if __name__ =='__main__':
    add(5,6)
'''

#----------- Python program to find the power of a number using recursion
# Recursion = Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. 
# It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.
# Get number and power
# multiply number itself to the count of power
# return result

'''
def power(num,p):
    if p==0:
        return 1
    else:
        return num*power(num,p-1)
print(power(2,3))
'''


# -----------Sorting objects of user defined class in Python
# The following article discusses how objects of a user-defined class can be arranged based on any of the variables of the class, which obviously will hold some value for every object.
# So far, we are aware of how we can sort elements of a list, the concept here is more or less the same as, except it is a step forward or we can say it is an advanced version of sorting elements but instead of a list we are dealing with objects of a class.
'''
class list():
    def __init__(self):
        self.list=[]
    def add(self,item):
        self.list.append(item)
    def sort(self):
        self.list.sort()
        print(self.list)
li=list()
li.add(56)
li.add(1)
li.add(12)
li.add(45)
li.sort()
'''
