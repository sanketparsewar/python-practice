# -----xxxxxxx-------- Types of sorting techniques -----xxxxxxxxxxx----------
#1. Bubble Sort.
#2. Merge Sort.
#3. Insertion Sort.
#4. Shell Sort.
#5. Selection Sort.


# ------------- Complexities
# --------O notations---------
'''
Algorithm	            Time Complexity	       Space Complexity
 	            Best	    Average 	Worst	   Worst
Bubble Sort	    Ω(n)	    θ(n^2)	    O(n^2)	    O(1)
Merge Sort	    Ω(n log(n))	θ(n log(n))	O(n log(n))	O(n)
Insertion Sort	Ω(n)	    θ(n^2)	    O(n^2)	    O(1)
Shell Sort	    Ω(n log(n))	θ(n log(n))	O(n^2)	    O(1)
Selection Sort	Ω(n^2)	    θ(n^2)	    O(n^2)	    O(1)
Heap Sort	    Ω(n log(n))	θ(n log(n))	O(n log(n))	O(1)
Quick Sort	    Ω(n log(n))	θ(n log(n))	O(n^2)	    O(n)
'''



# ------------Bubble Sort ---------------------------
'''
It is a comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order.
Time Complexity	 
Best	            O(n)
Worst	            O(n^2)
Average	            O(n^2)
Space Complexity	O(1)
'''
# --------Algorithm
'''
bubbleSort(array)
  for i <- 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap leftElement and rightElement
end bubbleSort
'''
# -------Implementation - Bubble Sort
'''
number=[2,98,60,8,0,11,9,10,11,13,51]
print('Original list: ',number)
for j in range(len(number)):   
    for i in range(len(number)-j-1):
        if i!=len(number)-1:
            if number[i]>number[i+1]:
                number[i],number[i+1]=number[i+1],number[i]
            else:
                pass

print('Sorted list:',number)
'''
# ----------Optimization of Bubble sort
'''
In the above algorithm, all the comparisons are made even if the array is already sorted.
This increases the execution time.
To solve this, we can introduce an extra variable swapped. The value of swapped is set true if there occurs swapping of elements. Otherwise, it is set false.
After an iteration, if there is no swapping, the value of swapped will be false. This means elements are already sorted and there is no need to perform further iterations.
This will reduce the execution time and helps to optimize the bubble sort.
'''



# ------------Merge Sort ----------------------
'''
Merge sort first divides the array into equal halves and then combines them in a sorted manner.
Based on the principle of Divide and Conquer Algorithm.
Here, a problem is divided into multiple sub-problems.
Each sub-problem is solved individually.
Finally, sub-problems are combined to form the final solution.
The merge sort algorithm recursively divides the array into halves until we reach the base case of array with 1 element. 
After that, the merge function picks up the sorted sub-arrays and merges them to gradually sort the entire array.
'''
# -----------Algorithm
# A = Unsorted array.
# A subproblem would be to sort a sub-section of this array starting at index p and ending at index r, denoted as A[p..r].
'''
MergeSort(A, p, r):
    if p > r 
        return
    q = (p+r)/2
    mergeSort(A, p, q)
    mergeSort(A, q+1, r)
    merge(A, p, q, r)
'''
# ------Implementation of Merge sort
'''
def merge(li):
    if len(li)>1:
        half=len(li)//2          # // indicates that it will give integer value
        left_half=li[:half]
        right_half=li[half:]

        #we will use recursion to divide and divide the list till we get list with 2 elements each
        merge(left_half)
        merge(right_half)

        #merge
        i=0    #keep track of leftmost element of left half
        j=0    #keep track of leftmost element of right half
        k=0    #index of merge list
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                li[k]=left_half[i]
                i+=1
                
            else:
                li[k]=right_half[j]
                j+=1
            k+=1

        while i<len(left_half):
            li[k]=left_half[i]
            i+=1
            k+=1
        
        while j<len(right_half):
            li[k]=right_half[j]
            j+=1
            k+=1
        return li

number=[10,41,21,1,51,10,20,30,11,14]
print(merge(number))
'''


# ------------Insertion Sort-------------------
'''
Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
So in beginning we compare the first two elements and sort them by comparing them. 
Then we pick the third element and find its proper position among the previous two sorted elements. 
This way we gradually go on adding more elements to the already sorted list by putting them in their proper position.
Time Complexity	 
Best	            O(n)
Worst	            O(n^2)
Average	            O(n^2)
Space Complexity	O(1)
Stability	        Yes
'''
# -----------Algorithm
'''
insertionSort(array)
  mark first element as sorted
  for each unsorted element X
    'extract' the element X
    for j <- lastSortedIndex down to 0
      if current element j > X
        move sorted element to the right by 1
    break loop and insert X here
end insertionSort
'''
# -----------Implementation of Insertion Sort
'''
def Insertion_sort(li):
    for i in range(1,len(li)):
        k=li[i]
        j=i-1
        while j>=0:
            if k<li[j]:
                li[j+1]=li[j]     #shift elements of j to right to j+1
                li[j]=k           #insert k into j th position
            j=j-1

    print(li)
    

num=[4,2,1,6,5]
Insertion_sort(num)
'''


# ------------Shell Sort ---------------------
'''
Shell Sort involves sorting elements which are away from each other. 
We sort a large sublist of a given list and go on reducing the size of the list until all elements are sorted. 
The below program finds the gap by equating it to half of the length of the list size and then starts sorting all elements in it. 
Then we keep resetting the gap until the entire list is sorted.
Time Complexity	 
Best	            O(n log n)
Worst	            O(n^2)
Average	            O(n log n)
Space Complexity	O(1)
Stability	        No
The space complexity for shell sort is O(1).
'''
# -------- Shell Sort Applications
'''
Shell sort is used when:
1.Calling a stack is overhead. uClibc library uses this sort.
2.Recursion exceeds a limit. bzip2 compressor uses it.
3.Insertion sort does not perform well when the close elements are far apart. 
4.Shell sort helps in reducing the distance between the close elements. Thus, there will be less number of swappings to be performed.
'''
# --------Shell Sort Algorithm
'''
shellSort(array, size)
  for interval i <- size/2n down to 1
    for each interval "i" in array
        sort all the elements at interval "i"
end shellSort
'''
# ---------Implementation of shell sort
'''
def Shell_sort(alist):
    gap=len(alist)//2
    while gap>0: 
        for index in range(gap,len(num)):
            current_element=alist[index]   #this is 4th index ielement as current element
            pos=index     #position will tell how many elements are present in sorted part when we need to stop compating values
            while pos>=gap and current_element<alist[pos-gap]:      #it is for ascending order if you want descending order then use this while pos>=gap and current_element<alist[pos-gap]
                alist[pos]=alist[pos-gap]
                pos=pos-gap
            alist[pos]=current_element
        gap=gap//2
    print(alist)

num=[6,5,3,4,8,1,2,10,9,7]
Shell_sort(num)
'''



# ----------------Selection Sort ----------------------
'''
In selection sort we start by finding the minimum value in a given list and move it to a sorted list. 
Then we repeat the process for each of the remaining elements in the unsorted list. 
The next element entering the sorted list is compared with the existing elements and placed at its correct position.
So, at the end all the elements from the unsorted list are sorted.
Selection Sort Complexity
Time Complexity	 
Best	            O(n^2)
Worst	            O(n^2)
Average	            O(n^2)
Space Complexity	O(1)
Stability	        No
'''
# ---------------Selection Sort Applications
'''
The selection sort is used when:
1.a small list is to be sorted
2.cost of swapping does not matter
3.checking of all the elements is compulsory
4.cost of writing to a memory matters like in flash memory (number of writes/swaps is O(n) as compared to O(n2) of bubble sort)
'''
# ---------------Selection Sort Algorithm
'''
selectionSort(array, size)
  repeat (size - 1) times
  set the first unsorted element as the minimum
  for each of the unsorted elements
    if element < currentMinimum
      set element as new minimum
  swap minimum with first unsorted position
end selectionSort
'''
# -------------Implementation of Selection sort
# --- 1.Using min function **Not duplicate values** (ascending order) 
'''
list1=[6,5,2,1,4,3]
for i in range(len(list1)):
    min_val=min(list1[i:])
    min_index=list1.index(min_val)
    list1[i],list1[min_index]=list1[min_index],list1[i]
print(list1)
'''
# --- 2.Using min function ** duplicate values** (ascending order) 
'''
list1=[6,6,5,2,1,1,4,3,6]
for i in range(len(list1)):
    min_val=min(list1[i:])
    min_index=list1.index(min_val,i)    #the i indicates from where to start to get the index
    list1[i],list1[min_index]=list1[min_index],list1[i]
print(list1)
'''
# --- 3.Using max function **Not duplicate values** (descending order)
'''
list1=[6,5,2,1,4,3]
for i in range(len(list1)):
    max_val=max(list1[i:])
    max_index=list1.index(max_val)
    list1[i],list1[max_index]=list1[max_index],list1[i]
print(list1)
'''
# --- 4.Using max function **duplicate values** (descending order)
'''
list1=[6,6,5,2,1,1,4,3,6]
for i in range(len(list1)):
    max_val=max(list1[i:])
    max_index=list1.index(max_val,i)   #the i indicates from where to start to get the index
    list1[i],list1[max_index]=list1[max_index],list1[i]
print(list1)
'''
# --- 5.Ascending order 
'''
list1=[6,6,5,2,1,1,4,3,6]
for i in range(len(list1)):
    min_val=list1[i]
    for j in range(i+1,len(list1)):
        if list1[j]<min_val:
            min_val=list1[j]
    
    min_index=list1.index(min_val,i)    #the i indicates from where to start to get the index
    list1[i],list1[min_index]=list1[min_index],list1[i]
print(list1)
'''