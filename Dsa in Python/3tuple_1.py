# --------Tuple = immutable (values cannot be modified or removed or changed)
# t=('mon',45,'tue',10,50,66)
# print(t)
'''Methods in tuple:
t.count()	Returns the number of times a specified value occurs in a tuple
t.index()	Searches the tuple for a specified value and returns the position of where it was found'''


# --------Python – Maximum and Minimum K elements in Tuple
'''
tup=(26,31,36,77,90,81,12,56,33,14,45)
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
'''
num=(23,65,9,8,9,5,4,8,85)
s=sum(num)
print(s)
'''

# ------------ Python – Row-wise element Addition in Tuple Matrix
'''
test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
cus_eles = [6, 7, 8]
for indx,val in enumerate(test_list):
    for sub in val:
        sub=sub + (cus_eles[indx],)
        print(sub)

# OR

test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
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
