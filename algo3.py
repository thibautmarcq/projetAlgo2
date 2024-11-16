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