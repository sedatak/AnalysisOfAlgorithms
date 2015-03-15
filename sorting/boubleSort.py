import time
import random

i = 0

k = int(input("Dizinin boyutunu giriniz: "))
dizi = []

while(i < k):
    b = random.randint(1, 10000)
    dizi.append(b)
    i = i + 1

start = time.time()

a = 0
b = 0
for passnum in range(len(dizi)-1,0,-1):
    for i in range(passnum):
        b = b + 1
        if dizi[i]>dizi[i+1]:
            a = a + 1
            temp = dizi[i]
            dizi[i] = dizi[i+1]
            dizi[i+1] = temp
print("Yapılan karşılaştırma sayısı:", b)
print("Yapılan yer değiştirme sayısı:", a)


finish = time.time()
execution_time = finish - start
print(dizi,"Execution time: ",execution_time)
