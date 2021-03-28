# Bubble Sort Algorithm

import random
import timeit
import matplotlib.pyplot as plt

def bub_sort(arr):
    n = len(arr) - 1

    for i in range(n, 0, -1):
        #print(arr[i], arr)

        for j in range(i):
            #print(arr[j], arr)

            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


# Selection Sort Algorithm

def sel_sort(arr):
    n = len(arr) - 1

    for i in range(n):
        min = i

        for j in range(i, n + 1):
            if arr[j] < arr[min]:
                min = j

        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    return arr

                    
# Insertion Sort Algorithm                    

def ins_sort(arr):
    n = len(arr) - 1

    for i in range(n + 1):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp
    return arr


# Merge Sort Algorithm                
                
def merge(arr1,arr2):
  arr = []
  
  while len(arr1) > 0 and len(arr2) > 0:
    if arr1[0] < arr2[0]:
      arr.append(arr1.pop(0))
    else: 
      arr.append(arr2.pop(0))
  if len(arr1) > 0:
    arr.extend(arr1)
  if len(arr2) > 0:
    arr.extend(arr2)
  return arr          

def merge_sort(arr): #O(n logn)
  #base case
  if len(arr) <= 1:
    return arr
    #split recursively 
  else:  
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    arr = merge(left,right)
    return arr


def sort(N):
  times = [[],[],[],[]]
  tenth = N//10
  n = [tenth, 2*tenth, 3*tenth , 4*tenth, 5*tenth, 6*tenth, 7*tenth, 8*tenth, 9*tenth, N ]

  for i in n:
    arr1 = list(range(i))
    random.shuffle(arr1)

    execute = "bub_sort(" + str(arr1) + ")" 
    times[0].append(timeit.timeit(globals = globals(), stmt = execute, number=2 )) 

    execute = "sel_sort(" + str(arr1) + ")"
    times[1].append(timeit.timeit(globals = globals(), stmt = execute, number=2 ))

    execute = "ins_sort(" + str(arr1) + ")"
    times[2].append(timeit.timeit(globals = globals(), stmt = execute, number=2 ))

    execute = "merge_sort(" + str(arr1) + ")"
    times[3].append(timeit.timeit(globals = globals(), stmt = execute, number=2 ))

  fig = plt.figure()
  fig,ax = plt.subplots()

  ax.plot(n,times[0], label='bubble sort')
  ax.plot(n,times[1], label='selection sort')
  ax.plot(n,times[2], label='insertion sort')
  ax.plot(n,times[3], label='merge sort')

  ax.set(xlabel='List Size', ylabel='Time in CPU process time', title='Complexities')
  ax.grid()
  ax.legend()

  plt.savefig('algorithms.png')
