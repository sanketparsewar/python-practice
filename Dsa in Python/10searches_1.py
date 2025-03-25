# -----xxxxxxxxxx------Types of searches ----xxxxxx----
# Sequential Search: linear search
# Interval Search: Binary search


#---------- Sequential Search----------- 
''' 
In this, the list or array is traversed sequentially and every element is checked. 
For example: Linear Search.
Complexity: O(n)
'''

# ---------Linear search
'''
num=[4,10,2,5,8,6,3,1,4,11]
key=int(input("Enter value to search "))
for i in range(len(num)):
    if key==num[i]:
        print(key,'is present at index',i)
        break
    elif i==len(num)-1:
        print('Not Available')
'''



# ----------------Interval Search ---------------
'''
These algorithms are specifically designed for searching in sorted data-structures. 
These type of searching algorithms are much more efficient than Linear Search as they repeatedly target the center of the search structure and divide the search space in half. 
For Example: Binary Search.
Complexity: O(log n)       ....n is number of elements in list 
'''
# ----------------- Binary search 
'''
num=[4,6,9,1,45,26,11,51,345,67,343,12,43]
num.sort()
print(num)
low=0
high=len(num)-1
mid=int((low+high)/2)             # or we can use mid=(low+high)//2
key=int(input("Enter key value to search: "))
while True:
    if key==num[mid]:
        print(key,'is at index',mid,'👍')
        break

    elif low>=high:                     #exit if low is greater than high
        print(key,"not present🙁")
        break

    elif key>num[mid]:                  #for right of mid in list
        print('mid',mid)
        low=mid+1
        mid=int((low+high)/2)
        
    elif key<num[mid]:                  #for left of mid in list
        print('mid',mid)
        high=mid-1
        mid=int((low+high)/2)
        
'''



# --------- search where first becomes mid for right side and high becomes mid for left side
'''
num=[54,90,14,26,4,8,19,45,11,13,87,74,15,49,69]
num.sort()
print(num)
first=0
last=len(num)
mid=(first+last)/2
mid=int(mid)
try:   
    key=int(input("Enter key value to search: "))
    # key=float(input("Enter key value to search: "))     #this is for float value in list 
    while True:            
        if key<num[mid]:
            print('les1 mid is at',mid)      #this statement is to check where the mid pointer is
            last=mid
            mid=int((first+last)/2)
            
            
            if mid==last:
                print(key,'is not available😒')
                break
        
        elif key>num[mid]:
            print('gre1 mid is at',mid)       #this statement is to check where the mid pointer is
            first=mid
            mid=int((first+last)/2)
            
            
            if mid==first:
                print(key,'is not available🥱')
                break
        elif key==num[mid]:
            print(key,'is at index',mid)
            break
except:
    print("Incorrect input!")    
'''


# ------Find the no of rotations of sorted list using Binary search
# using binary search find middle element
# check whether mid_element is less than previous element if yes return mid
# check mid_element is less than last element of range if yes then answer is in left
# else answer is in right
'''
# list=[]
list=[8,9,10,1,2,3,4,5,6,7]  #len(list)=10
if len(list)==1:
    print('List contains single element',list)
    
elif len(list):    
    lo=0
    hi=len(list)-1     #hi=10-1=9
    mid=(lo+hi)//2
    while len(list)>0:
        mid=(lo+hi)//2       #mid=(0+9)//2 = 4
        if list[mid]<list[mid-1]:       #list[4]=2
            print(f'List is rotated {mid} times')
            break      
        elif list[mid]<list[len(list)-1]:  #list[mid]<list[len(list)-1] answer is in left
            hi=mid-1      #hi=4-1=3
        else :
            lo=mid+1

else:
    print('Empty list',list)
'''


# -----searching in a rotated list
# find mid element 
# check mid is less than previous if yes then

# check mid is less than last element of range answer is in left
# else answer is in right

# li = [6,7,1,2,3,4,5]  
# query = 4
# output = (position of 4 is 6)

# li = [6,7,1,2]  
# query = 7
# output = (position of 7 is 2)

# li = [4,5,6,7,1]
# query = 1
# output = (position of 1 is 5)

# list = [6,7,1,2]  
# list = [4,5,6,7,1]
list=[6,7,1,2,3,4,5]
query=6
lo=0
hi=len(list)-1
while True:
    mid=(lo+hi)//2
    # mid_ele=list[mid]
    # prev_ele=list[mid-1]
    if list[mid] < list[mid-1]:   #we found smallest element of list
        lo=0                      # lo=2 
        hi=len(list)-1            # hi=2    
        
        if query==list[mid]:
                print(f'1Query {query} is at position {mid+1}')
                break
        
        else:
            # print('els')
            # count=mid       #count of rotation
            while True:            #[6,7,1,2,3,4,5]   list[mid]=smallest nuber =1
                if query==list[mid]:
                    print(f'Query {query} is at position {mid+1}')
                    break
                if query > list[mid] and query<list[len(list)-1] :     #2>1 2<5 right 
                    lo=mid+1
                    mid=(lo+hi)//2                    
                else:
                    hi=mid-1        #left
                    mid=(lo+hi)//2

        break

    elif list[mid] < list[len(list)-1]:  #answer in left
        hi=mid-1
    else:
        lo=mid+1
    
    







