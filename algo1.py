import numpy as np

def AlgorithmeI(s, i, V) :
    tab = [-1] + V
    if s == 0 :
        return 0
    elif s < 0 or i==0 :
        return np.inf
    else :
        m1 = AlgorithmeI(s, i-1, V)
        m2 = AlgorithmeI(s-tab[i], i, V) +1
        return min(m1, m2)

tab = [0, 1, 2, 5, 10, 20, 50, 100, 200]
#AlgorithmeI(729, 2, tab)
#print(compteur)

