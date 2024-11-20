
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
    #print("ha")
    tab = [-1] + V
    return sub_algo_glouton(s, k, tab)

def TestGloutonCompatible(k, V) :
    #tab = [-1] + V
    #print(tab)
    if k>=3 :
        #print("k : ", k)
        for S in range(V[2]+2 , V[k-2] + V[k-1] - 1) :
            #print("s : ", S)
            for j in range(k) :
                #print("j, V[j]", j, V[j])
                if (V[j] < S) and (AlgorithmeIII(S, k-1, V) > 1 + AlgorithmeIII(S - V[j], k-1, V) ) :
                    return False
    return True


