import time
import random

i = 0

k = int(input("Dizinin boyutunu giriniz: "))
dizi = []

while(i < k):
    b = random.randint(1, 10000)
    dizi.append(b)
    i = i + 1

a = 0
b = 0

start = time.time()

for fillslot in range(len(dizi)-1,0,-1):
    positionOfMax=0
    for location in range(1,fillslot+1):
        b = b + 1
        if dizi[location]>dizi[positionOfMax]:
            positionOfMax = location

    a = a + 1 
    temp = dizi[fillslot]
    dizi[fillslot] = dizi[positionOfMax]
    dizi[positionOfMax] = temp
print("Yapılan karşılaştırma sayısı:", b)
print("Yapılan yer değiştirme sayısı:", a)

finish = time.time()
execution_time = finish - start
print(dizi,"Execution time: ", execution_time)
