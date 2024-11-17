import math
import random

P_MAX = 700

def genere_system() :
    tab_k = [1, 2, 3, 5, 10, 12]
    comp = 1

    for k in tab_k :
        tab = [1]
        last = 1
        for i in range (1, k) :
            cur = random.randint(last, P_MAX)
            last = cur
            tab.append(cur)
        



# j'ai fini