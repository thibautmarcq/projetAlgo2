import math
import random

P_MAX = 700

def genere_system() :
    tab_k = [1, 2, 3, 5, 10, 13]
    comp = 1

    for k in tab_k :
        tab = [1]
        last = 1
        filename = "tests/random/sys_rand_" + str(comp) + ".txt"
        with open(filename, "w") as file :
            file.write(str(k) + "\n")
            file.write('1\n')
            for i in range (1, k) :
                cur = random.randint(last, P_MAX)
                last = cur
                file.write(str(cur) + "\n")
        comp +=1
            
genere_system() 