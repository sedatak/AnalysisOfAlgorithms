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

for index in range(1,len(dizi)):
    a = a + 1

    currentvalue = dizi[index]
    position = index

    while position>0 and dizi[position-1]>currentvalue:
        dizi[position]=dizi[position-1]
        position = position-1
        b = b + 1
        
    dizi[position]=currentvalue

print("Yapılan karşılaştırma sayısı:", b)
print("Yapılan yer değiştirme sayısı:", a)

finish = time.time()
execution_time = finish - start
print(dizi,"Execution time: ",execution_time)
