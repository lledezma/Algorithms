import time
import math
##########################################################  Blubble Sort  *O(n^2 )
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
      for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
          arr[j], arr[j+1] = arr[j+1], arr[j]
##########################################################  Quicksort
def quick_sort(A,p,r):
    if p < r:
       q = partition(A, p, r)
       quicksort(A,p,q-1)
       quicksort(A,q+1,r)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if (A[j] <= x):
            i = i+1
            temp = A[i]
            temp2 = A[j]
            A[i] = temp2
            A[j] = temp
    temp = A[i+1]
    temp2 = A[r]
    A[i+1] = temp2
    A[r] = temp
    return i+1


##########################################################  Counting Sort
def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m
    for a in array1:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array1[i] = a
            i += 1

##########################################################  insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

##########################################################  seletion sort
def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]


##########################################################  HeapSort
def heap_sort(arr):
    n = len(arr)
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

##########################################################  MergeSort
def merge_sort(array):
   if len(array)>1:
       middle = len(array)//2
       lefthalf = array[:middle]
       righthalf = array[middle:]
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               array[k]=lefthalf[i]
               i=i+1
           else:
               array[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           array[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           array[k]=righthalf[j]
           j=j+1
           k=k+1

##########################################################  Binary Search
def binary_search (arr,x): 
  first = 0;
  last = len(arr)-1
  while(first <= last):
    middle = (first+last)/2
    if arr[middle] == x:
      return(middle)
    elif arr[middle] > x:
      last = middle -1
    else:
      first = middle +1
  return("Not found!")

def binary_search_recursion(arr,first,last,x):               # Binary Search Recursion
  if first <= last:
    middle = (first+last)/2
    if(arr[middle] == x):
      return(middle)
    elif(arr[middle] > x):
      return binSeaRec(arr,first,middle-1,x)
    else:
      return binSeaRec(arr,middle+1,last, x)
  else:
    return("not found!")



#appending numbers.txt numbers into A[] array to sort them
file = open("numbers.txt", 'r')
lines = file.readlines()
counter = 0
A = []
for line in lines:
    A.append(int(line))

###############################################################################QuickSort Test
# quicksort(A,0, len(A)-1)   //for quick testing
# print(A)                  //for quick testing

# start = time.time()
# quicksort(A,0, len(A)-1)
# end = time.time()
# print(end-start, " seconds to sort")
#
# f = open("QuickSort/quicksort_sorted.txt", "w+")
# for x in A:
#      f.write("%s\n" % str(x))
# f.close()




###############################################################################CountingSort Test
# countingsort(A, max(A))       //for quick testing
# print(A)                      //for quick testing

# start = time.time()
# countingsort(A, max(A))
# end = time.time()
# print(end-start, " seconds to sort")
#
# f = open("CountingSort/countingsort_sorted.txt", "w+")
# for x in A:
#      f.write("%s\n" % str(x))
# f.close()




###############################################################################InsertionSort Test
# insertionSort(A)              //for quick testing
# print(A)                      //for quick testing

# start = time.time()
# insertionSort(A)
# end = time.time()
# print(end-start, " seconds to sort")
#
# f = open("InsertionSort/insertionsort_sorted.txt", "w+")
# for x in A:
#      f.write("%s\n" % str(x))
# f.close()




###############################################################################SelectionSort Test
# selectionsort(A)      //for quick testing
# print(A)              //for quick testing


# start = time.time()
# selectionsort(A)
# end = time.time()
# print(end-start, " seconds to sort")
#
# f = open("selectionSort/selectionsort_sorted.txt", "w+")
# for x in A:
#      f.write("%s\n" % str(x))
# f.close()



###############################################################################heapSort Test
# heapSort(A)           //for quick testing
# print(A)              //for quick testing

# start = time.time()
# heapSort(A)
# end = time.time()
# print(end-start, " seconds to sort")

# f = open("heapSort/heapsort_sorted.txt", "w+")
# for x in A:
#      f.write("%s\n" % str(x))
# f.close()



###############################################################################MergeSort Test
# mergeSort(A, 0, len(A)-1)     //for quick testing
# print(A)                      //for quick testing

# start = time.time()
# mergeSort(A)
# end = time.time()
# print(end-start, " seconds to sort")
#
# f = open("MergeSort/mergesort_sorted.txt", "w+")
# for x in A:
#      f.write("%s\n" % str(x))
# f.close()
