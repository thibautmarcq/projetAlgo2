## Fichier contenant toutes le fonctions (algorithmes) écrits durant le projet
# Pour les algorithmes isolés : voir algo1.py, algo2.py, algo3.py,

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


def calcul_matrice(s, k, V) :
    lig = s+1
    col = k+1
    tab = [-1] + V
    m = np.full((s+1, k+1), np.inf)

    for i in range(col) :
        m[0][i] = 0

    for i in range (1, lig) :
        for j in range (1, col) :
            sans_bocal = m[i][j-1]
            avec_bocal = np.inf
            if s >= tab[j] : 
                avec_bocal = m[i-tab[j]][j] + 1
            m[i][j] = min(sans_bocal, avec_bocal)

    return m

def algo_optimise(s, k, V) :
    m = calcul_matrice(s, k, V)
    return m[s][k]
    

# Fonction opti par mémoïsation + retour du nb de bocaux pris par volume
# (6.a)

def algo_optimise2(s, k, tab):
    col = len(tab)
    m = [[(np.inf, [np.zeros(col)]) for _ in range(k + 1)] for _ in range(s + 1)]

    m[0] = [(0, [np.zeros(col)]) for _ in range(k + 1)]

    for i in range(1, s + 1):
        for j in range(1, k + 1):
            sb_nb, sb_tab = m[i][j-1]

            ab_nb, ab_tab = (np.inf, [np.zeros(col)])

            if i >= tab[j-1]:
                tmp, ab_tab = m[i-tab[j-1]][j]
                ab_tab = ab_tab.copy()
                ab_tab[j-1] += 1
                ab_nb = tmp + 1

            if sb_nb <= ab_nb:
                m[i][j] = (sb_nb, sb_tab)
            else:
                m[i][j] = (ab_nb, ab_tab)

    # print(m)
    return m[s][k]



def AlgorithmeII(s, k, V) :
    m = calcul_matrice(s, k, V)

    tab = [-1]+V
    utilises = np.zeros(k+1)
    i = s
    j = k
    while i>0 and j >= 0 :
        if m[i][j] == m[i-tab[j]][j]+1 :
            utilises[j] += 1
            i = i-tab[j]
        else :
            j-=1
    return utilises[1:]


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


def extract_data(filename) :
    with open(filename + ".txt", 'r') as file :
        s = int(file.readline().strip())
        nb_bocaux = int(file.readline().strip())
        tab = []
        for i in range (nb_bocaux) :
            tab.append(int(file.readline().strip()))
        return (s, tab)
    

S, V = extract_data("test")
print(AlgorithmeIII(S, 2, V))