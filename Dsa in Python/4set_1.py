# ---------Set = values in set cannot be duplicate 
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


# ----------- Find the size of a Set in Python
'''
days={'monday','tuesday','wedmnesday','thursday','friday','saturday'}
print(days.__sizeof__(),'bytes')
'''

# ------Iterate over a set in Python
'''
days={'monday','tuesday','wedmnesday','thursday','friday','saturday'}
for day in days:
    print(day)
'''

# -----------Python – Maximum and Minimum in a Set
'''
nums={12,22,36,45,14,10,25,18,98,78,11,26}
nums_sorted=sorted(nums)
print(nums_sorted)
print("min=",nums_sorted[0],', max=',nums_sorted[len(nums_sorted)-1])
'''

# ------- Python – Remove items from Set
'''
nums={12,22,36,45,14,10,25,18,98,78,11,26}
print(nums)
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