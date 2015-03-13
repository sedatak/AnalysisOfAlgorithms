import random
from array import array


i = 0
j = 0
boyut = int(input("Dizinin boyutunu giriniz: "))
k = int(input("Kaçıncı eleman: "))
bigORsmall = input("Büyük eleman mı küçük eleman mı bulunsun? (b/k): ")
dizi = []

while(i < boyut):
    a = random.randint(1, 10000000)
    dizi.append(a)
    i = i + 1

enB = dizi[0]
siraliB = []
enK = dizi[0]
siraliK = []

if(bigORsmall == 'b'):
    while(j < k):
        for i in range(boyut-1):
            if(enB < dizi[i]):
                enB = dizi[i]
        siraliB.append(enB)
        dizi.remove(max(dizi))
        j = j + 1
    print(siraliB[k-1])

if(bigORsmall == 'k'):
    while(j < k):
        for i in range(boyut-1):
            if(enK > dizi[i]):
                enK = dizi[i]
        siraliK.append(enK)
        dizi.remove(min(dizi))
        j = j + 1
    print(siraliK[k-1])

if(bigORsmall != 'b' and bigORsmall != 'k'):
    print("b veya k giriniz!")
