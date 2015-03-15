import time

def bubbleSort(alist):
    a = 0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                a = a + 1
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp 
    print(a)
alist = [54,26,93,17,77,31,44,110,55,20]
start = time.time()
bubbleSort(alist)
finish = time.time()
execution_time = finish - start
print(alist,"Execution time: ",execution_time)
