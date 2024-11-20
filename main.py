from algo1 import *
from algo2 import *
from algo3 import *
from genere_system import *

import os
import time
import random

PMAX = 5500
F = 20
random.seed(47)

def read_test_file(filepath):
    print(filepath)
    with open(filepath, 'r') as file:
        s = int(file.readline().strip())
        k = int(file.readline().strip())
        V = [int(line.strip()) for line in file.readlines()]
        print("s k v", s, k, V)
    return s, k, V

def compare_algorithms():
    directory = './tests'
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            s, k, V = read_test_file(filepath)
            
            algo1_time=0
            if(s<500):
                start_time = time.time()
                AlgorithmeI(s, k, V)
                algo1_time = time.time() - start_time
                
            start_time = time.time()
            AlgorithmeII(s, k, V)
            algo2_time = time.time() - start_time
            
            start_time = time.time()
            AlgorithmeIII(s, k, V)
            algo3_time = time.time() - start_time
            
            results.append({
                's': s,
                'algo1_time': algo1_time,
                'algo2_time': algo2_time,
                'algo3_time': algo3_time
            })
   
    return results

# results = compare_algorithms()
# txt_file = 'results.txt'

# # Écrire les résultats dans le fichier texte
# with open(txt_file, mode='w') as file:
#     file.write('s\talgo1_time\talgo2_time\talgo3_time\n')

#     for result in results:
#         file.write(f"{result['s']}\t{result['algo1_time']:.6f}\t{result['algo2_time']:.6f}\t{result['algo3_time']:.6f}\n")


def proportion_gloutons_compatibles() :

    tot = 0
    comp_glouton = 0

    tab_k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # tab_k = [1] + [random.randint(1, 50000) for _ in range(500)]
    tab_k.sort()

    for k in tab_k :
        tot_partiel = 0
        comp_glouton_partiel = 0
        for i in range(1000) :    
            tot+=1
            tot_partiel+=1
            tab = genere_system(k)
            if TestGloutonCompatible(k-1, tab) :
                comp_glouton+=1
                comp_glouton_partiel+=1
        print("k : ", k)
        print("\t tot : ", tot_partiel)
        print("\t compatibles : ", comp_glouton_partiel)
        print("\t proportion d'instances glouton-compatibles : ", comp_glouton_partiel/tot_partiel)
    
    return comp_glouton/tot

print(proportion_gloutons_compatibles())

def ecarts_glouton_ou_pas() :
    tot = 0
    ecart_tot = 0
    pourc_tot = 0
    ecart_max = -1
    tab_k = [1, 3, 9, 50, 200, 500, 750, 1000, 5000]

    filename = "stats.txt"

    with open(filename, "w") as file:
        file.write("Taille_Systeme\tQuantite\tVal_AlgoII\tVal_AlgoIII\tEcart\tEcart_Pourcentage\n")
    
        for k in tab_k :
            for i in range(5) :
                tab = genere_system(k)
                if not TestGloutonCompatible(k-1, tab) :
                    for s in range(PMAX, PMAX*F + 1, 5) :
                        print("k, s : ", k, s)
                        tot+=1
                        #temps = time.time()
                        val1 = AlgorithmeII(s, k-1, tab)
                        #temps1 = time.time() - temps
                        
                        
                        #temps = time.time()
                        val2 = AlgorithmeIII(s, k-1, tab)
                        #temps2 = time.time() - temps

                        ecart = abs(val1-val2)
                        pourc_ecart = ecart/val1
                        if val1!=0 :
                            pourc_tot += pourc_ecart
                        if ecart > ecart_max :
                            ecart_max = ecart
                        ecart_tot+=ecart

                        file.write(f"{k}\t{s}\t{val1}\t{val2}\t{ecart}\t{pourc_ecart}\n")

    return(ecart_tot/tot, ecart_max, pourc_tot/tot)        
                    
# moy, max, pourc = ecarts_glouton_ou_pas()
# print("moyenne : ", moy, " max : ", max, "pourcentage d'erreur : ", pourc)

