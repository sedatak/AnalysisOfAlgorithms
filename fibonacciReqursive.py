# 10, 20, 30, 40, 50, 60, 70. fibonacci sayılarını özyineleme yöntemiyle bulan
#ve geçen zamanı ölçen program.

import time # Programın çalışma süresini hesaplamak için time modülü eklendi.

def fibonacci_reqursive(fib_number):
    if fib_number == 0: return 0
    elif fib_number == 1: return 1
    else: return fibonacci_reqursive(fib_number-1)+fibonacci_reqursive(fib_number-2)

start = time.time() # Kodun çalışmaya başladığı zaman start değişkenine atandı.

i = 10
while(i < 71):
    print(i, ". fibonacci number", fibonacci_reqursive(i))

    finish = time.time() # Kodun bittiği zaman finish değişkenine atandı.
    execution_time = finish - start # Çalışma zamanı bulundu.

    print("Execution Time: {}".format(execution_time))
    i = i + 10
