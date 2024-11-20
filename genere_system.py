import math
import random

P_MAX = 5500
random.seed(47)


def genere_system(k) :
    tab = [1] 
    for i in range(k-1) :
        rand = int(random.uniform(2, P_MAX))
        while(rand in tab) :
            rand = int(random.uniform(2, P_MAX))
        tab.append(rand)
    tab.sort()
    return tab

genere_system(699)