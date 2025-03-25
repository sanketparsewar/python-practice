#-------- Program to print half Diamond star pattern for given integer N
# xxxxxx 1.Type. program to print a half diamond shape with N rows
# *
# **
# ***
# ***
# **
# *
'''
N=6
for i in range(1,int(N/2)+1):
    print(i*'*')
for i in range(int(N/2),N+1):
    print((N-i)*'*')
'''

# xxxxx 2.Type. program to print a half diamond shape with 2N rows.
# *
# **
# ***
# ****
# ***
# **
# *
'''
N=4
for i in range (1,N+1):
    print(i*'*')
for i in range (1,N):
    print((N-i)*'*')
'''


# ------Programs for printing pyramid patterns in Python
# * 
# * *
# * * *
# * * * *
'''
n=4
for i in range(1,n+1):
    print(i*'* ')
'''
# -----pyramid using recursion
# *
# **
# ***
# ****
# *****
'''
def pyramid(n):
    if n==0:
        return
    else:
        pyramid(n-1)
        print(n*'*')

pyramid(5)
'''
# -----upside down pyramid using recursion
# *****
# ****
# ***
# **
# *
'''
def pyramid(n):
    if n==0:
        return
    else:
        print(n*'*')
        pyramid(n-1)

pyramid(5)
'''


# ------pyramid
#  ****
#   ***
#    **
#     *
'''
n=4
for i in range(n,0,-1):
    print((n-i)*' ',(i*'*'))
'''
# ------pyramid
#      *
#     **
#    ***
#   ****
#  *****
'''
n=5
for i in range(1,n+1):
    print((n-i)*' ',i*'*')
'''


# --------Triangle
#      * 
#     * *
#    * * *
#   * * * *
'''
n=4
for i in range(1,n+1):
    print(n*' ',i*'* ')
    n-=1

'''


# -----Number pattern
# 1
# 12
# 123
# 1234
# 12345
'''
n=5
for i in range(1,n+1):
    for i in range(1,i+1):
        print(i,end='')
    print()
'''
# ------Numbers without reassigning
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15    
'''
n=5
count=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(count,end=' ')
        count+=1
    print()
'''


# -----------Character Pattern
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
'''
from string import ascii_uppercase
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(ascii_uppercase[i-1],end=' ')
    print()

'''
# ------Continuous Character pattern
# A 
# B C 
# D E F 
# G H I J 
# K L M N O
'''
from string import ascii_uppercase
n=5
count=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(ascii_uppercase[count],end=' ')
        count+=1
    print()
'''


# ------Given a number n, write a program to print a diamond shape with 2n rows.
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
'''
num=5
n=num
for i in range(1,n+1):
    num-=1
    print(num*' ',i*'* ')
for i in range(n,0,-1):
    print((n-i)*' ',i*'* ')
'''


# ------Program to print digit pattern
# input: '41325'
# |****
# |*
# |***
# |**
# |*****
'''
n='41325'
for i in n:
    print('|'+ int(i)*'*')
'''
