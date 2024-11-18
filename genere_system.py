import math
import random

P_MAX = 700

def genere_system(k) :
    tab = [1] + [random.randint(2, P_MAX) for _ in range(k-1)]
    tab.sort()
    return tab


"""
def genere_system() :
    tab_k = [1, 2, 3, 5, 6, 8, 10, 13]
    comp = 1

    for k in tab_k :
        for i in range(3) :
            filename = "random/sys_rand_" + str(comp) + ".txt"
            with open(filename, "w") as file :
                file.write(str(k) + "\n")
                file.write('1\n')
                rand_int = [random.randint(2, P_MAX) for _ in range(k)]
                rand_int.sort()
                for val in rand_int :
                    file.write(str(val) + "\n")

            comp +=1
            
def read_system(filename) :
    with open(filename, 'r') as file :
        k = int(file.readline().strip())
        tab = [int(val.strip()) for val in file.readlines()]
        return (k, tab)

"""