import time
import random

i = 0

k = int(input("Dizinin boyutunu giriniz: "))
dizi = []

while(i < k):
    b = random.randint(1, 10000)
    dizi.append(b)
    i = i + 1

def shellSort(dizi):
    print("Sıralanacak Dizi: ", dizi)
    sublistcount = len(dizi)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(dizi,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",dizi)

      sublistcount = sublistcount // 2

def gapInsertionSort(dizi,start,gap):
    global a
    global b
    a = 0
    b = 0
    for i in range(start+gap,len(dizi),gap):
        a = a + 1

        currentvalue = dizi[i]
        position = i

        while position >= gap and dizi[position-gap] > currentvalue:
            dizi[position] = dizi[position-gap]
            position = position-gap
            b = b + 1
        dizi[position]=currentvalue
    return a, b

start = time.time()
shellSort(dizi)
finish = time.time()
execution_time = finish - start
print("Yapılan karşılaştırma sayısı:", a)
print("Yapılan yer değiştirme sayısı:", b)
print(dizi,"Execution time: ",execution_time)


