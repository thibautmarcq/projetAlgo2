
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
    tab = [-1] + V
    return sub_algo_glouton(s, k, tab)

def TestGloutonCompatible(k, V) :
    if k>=3 :
        for S in range(V[2]+2 , V[k-2] + V[k-1] - 1) :
            for j in range(k) :
                if (V[j] < S) and (AlgorithmeIII(S, k-1, V) > 1 + AlgorithmeIII(S - V[j], k-1, V) ) :
                    return False
    return True


