# 10, 20, 30, 40, 50, 60, 70. fibonacci sayılarını döngü yöntemiyle bulan ve
# geçen zamanı ölçen program.

import time # Programın çalışma süresini hesaplamak için time modülü eklendi.

counter = 3
first_var = second_var = 1 # İlk iki fibonacci sayılar tanımlandı.
start = time.time() # Kodun çalışmaya başladığı zaman start değişkenine atandı.
while(counter < 71):
    last = first_var + second_var
    first_var = second_var
    second_var = last;
    finish = time.time() # Kodun bittiği zaman finish değişkenine atandı.
    execution_time = finish - start # Çalışma zamanı bulundu.

    if(counter % 10 == 0):
        print(counter, ". fibonacci number: {}".format(last),
              "Execution Time: {}".format(execution_time))
    counter+=1
