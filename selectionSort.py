import time

def selectionSort(alist):
   a = 0
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       a = a + 1 
       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
   print(a)

alist = [54,26,93,17,77,31,44,110,55,20]
start = time.time()
selectionSort(alist)
finish = time.time()
execution_time = finish - start
print(alist,"Execution time: ", execution_time)
