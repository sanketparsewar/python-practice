# ------------ 1 -------------
# take input as interger for number of inputs
# create a dictionary key and list of values 
# add key and values in dictionary
# input to find average with respect to key
# print average correct to 2 decimal places
# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh
# 26.50
'''

n=int(input())
students_list=[]
for i in range(n):
    data=input()          #input is in data
    data_list=data.split(' ')   #data is split to space and stored in data_list
    # name=data_list[0]         #1st elemet of list is stored as name
    # marks=data_list[1:]       #remaining is stored in value
    element=data_list[0],data_list[1:]      #name is key and marks is value
    students_list.append(element)    #adding in list

students=dict(students_list)         #converting list to dictionary
stu_name=input()                   #taking name of student to find his average of marks
stu_marks=students[stu_name]       #using key assigning students marks to stu_marks
total_marks=0                      #initial total marks as 0
for i in range(len(stu_marks)):     #converting string values into float to find average
    stu_marks[i]=float(stu_marks[i])
    total_marks+=stu_marks[i]      #adding each marks

# avg_marks=total_marks/len(stu_marks) #finding average to total marks
# avg_marks=round(avg_marks,2)
# print(avg_marks)
#------- or ----------- 
print("%.2f"%((total_marks/len(stu_marks))))   #rounding up to 2 dedcimals
'''


# ---------- 2 ------------
# The first line of input contains an integer N , the number of mobile phone numbers.
# N lines follow each containing a mobile number.
# Output Format

# Print N mobile numbers on separate lines in the required format.

# Sample Input
# 3
# 07895462130
# 919875641230
# 9195969878

# Sample Output
# +91 78954 62130
# +91 91959 69878
# +91 98756 41230

# number of mobile number
# iterate n number of times to get input
# input mobile numbers one after another
# remove 0 or 91 from the numbers
# print in +91 XXXXX XXXXX this format
'''
n=int(input('Number of mobile numbers'))
m_numbers=[]
for _ in range(n):
    m_numbers.append(input())
sorted(m_numbers)
for i in range(len(m_numbers)):
    num=m_numbers[i]
    if len(num) == 11:
        num=num[1:]
        print(f'+91 {num[:5]} {num[5:]}')
    elif len(num) == 12:
        num=num[2:]
        print(f'+91 {num[:5]} {num[5:]}')
        # m_numbers[i]
    else:
        print(f'+91 {num[:5]} {num[5:]}')
        
'''
 
'''
def wrapper(f):
    def fun(l):
        l=sorted(l)
        # complete the function
        l1=[]
        for i in range(len(l)):
            num=l[i]
            if len(num) == 11:
                num=num[1:]
                l1.append(f'+91 {num[:5]} {num[5:]}')
            elif len(num) == 12:
                num=num[2:]
                l1.append(f'+91 {num[:5]} {num[5:]}')          
            elif len(num) == 10:
                l1.append(f'+91 {num[:5]} {num[5:]}')
            else:
                l1.append(f'{num[:3]} {num[3:8]} {num[8:]}')
        l1=sorted(l1)
        for i in range(len(l1)):
            print(l1[i])
    return fun
   
        

@wrapper
def sort_phone(l):
    print(*sorted(), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    l=sorted(l)
    print(l)
    sort_phone(l) 

'''

def __hash__(self):
    return hash(self)

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split(' '))
    for i in tuple(integer_list):
        hash_value=hash(i)
        print(hash_value,end='')


class Person:
    def __init__(self):
        pass

    # def __eq__(self, other):
    #     return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))

if __name__ == '__main__':
    n = int(input())
    person = Person(23, 'Adam')
    print(hash(person))