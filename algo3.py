
from genere_system import *


def sub_algo_glouton(s, k, V):
    res=0
    for i in range(k, 0, -1):
        while s >= V[i]:
            s -= V[i]
            res += 1
    return res

# => complexité temporelle : O(k)

def AlgorithmeIII(s, k, V) :
    tab = [0] + V
    return sub_algo_glouton(s, k, tab)

def TestGloutonCompatible(k, V) :
    if k>=3 :
        for S in range(V[3]+2, V[k-1] + V[k]) :
            for j in range(1, k) :
                if (V[j] < S) and (AlgorithmeIII(S, len(V), V) > AlgorithmeIII(S - V[j], len(V), V) ) :
                    return False
    return True


