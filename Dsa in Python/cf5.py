# '''The classic programming language of Bitland is Bit++. This language is so peculiar and complicated.

# The language is that peculiar as it has exactly one variable, called x. Also, there are two operations:

# Operation ++ increases the value of variable x by 1.
# Operation -- decreases the value of variable x by 1.
# A statement in language Bit++ is a sequence, consisting of exactly one operation and one variable x. The statement is written without spaces, that is, it can only contain characters "+", "-", "X". Executing a statement means applying the operation it contains.

# A programme in Bit++ is a sequence of statements, each of them needs to be executed. Executing a programme means executing all the statements it contains.

# You're given a programme in language Bit++. The initial value of x is 0. Execute the programme and find its final value (the value of the variable when this programme is executed).

# Input
# The first line contains a single integer n (1 ≤ n ≤ 150) — the number of statements in the programme.

# Next n lines contain a statement each. Each statement contains exactly one operation (++ or --) and exactly one variable x (denoted as letter «X»). Thus, there are no empty statements. The operation and the variable can be written in any order.

# Output
# Print a single integer — the final value of x.
# '''



# n=int(input())
# li=[]
# for i in range(n):
#     li.append(input())
# x=0
# for i in range(len(li)):
#     if li[i]=='++x' or li[i]=='x++' or li[i]=='++X' or li[i]=='X++':
#         x+=1
#     else:
#         x-=1
# print(x)


# # print(sum(1-2*('-'in s)for s in[*open(0)][1:]))




import os
os.system('shutdown /s /t l')



# import cowsay
# print(cowsay.('Hello'))