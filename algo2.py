import numpy as np

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
            if i >= tab[j] : 
                avec_bocal = m[i-tab[j]][j] + 1
            m[i][j] = min(sans_bocal, avec_bocal)
            
    return m


def AlgorithmeII(s, k, V) :
    m = calcul_matrice(s, k, V)
    nb_pots = 0
    tab = [-1]+V
    utilises = np.zeros(k+1)
    i = s
    j = k
    while i>0 and j >= 0 :
        if i>= tab[j] and m[i][j] == m[i-tab[j]][j]+1 :
            utilises[j] += 1
            nb_pots+=1
            i = i-tab[j]
        else :
            j-=1
    return nb_pots
    #return utilises[1:]

def Algorithme2(s, k, V) :
    m = calcul_matrice(s, k, V)

    tab = [-1]+V
    utilises = np.zeros(k+1)
    i = s
    j = k
    while i>0 and j >= 0 :
        if i>= tab[j] and m[i][j] == m[i-tab[j]][j]+1 :
            utilises[j] += 1
            i = i-tab[j]
        else :
            j-=1
    
    sum = 0
    for ind in range(1, len(utilises)) :
        sum += tab[ind] * utilises[ind]
    return sum
