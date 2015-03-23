import random

def olustur():
    
    global a
    a = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],]

    for j in range(8):
        i = random.choice([1, 2, 3, 4, 5, 6, 7, 0])
        a[i][j]= 1

    print("", a[0], "\n",
          a[1], "\n",
          a[2], "\n",
          a[3], "\n",
          a[4], "\n",
          a[5], "\n",
          a[6], "\n",
          a[7], "\n")
    return a

def test():
    olustur()

    cakisma = 0
    for i in range(8):
        for j in range(8):
            if (a[i][j] == 1):
                l = i
                k = j
                for t in range(8):
                    if (a[l][t] == 1):
                        cakisma = cakisma + 1
                        print cakisma
                
                if (l != 0):
                    for x in range(l, 0, -1):
                        k = k + 1
                        if (k < 8):
                            if(a[x][k] == 1):
                                cakisma = cakisma + 1
                                print("ÇAKIŞMA: ", cakisma)
                if (l == 0):
                    for x in range(l, 0, -1):
                        k = k + 1
                        if (k < 8):
                            if(a[x][k] == 1):
                                cakisma = cakisma + 1
                                print("ÇAKIŞMAA: ", cakisma)
                    
                    
                    #print(i , j, "süper")

test()
