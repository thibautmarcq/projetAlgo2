from algo1 import *
from algo2 import *
from algo3 import *

import os
import time

PMAX = 700
F = 20


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
    tab_k = [1, 2, 3, 5, 6, 7, 8, 10, 13, 15, 17, 22, 25, 36]

    for k in tab_k :
        for i in range(7) :
            tot+=1
            tab = genere_system(k)
            if TestGloutonCompatible(k-1, tab) :
                comp_glouton+=1
    
    return comp_glouton/tot


def ecarts_glouton_ou_pas() :
    tot = 0
    ecart_tot = 0
    pourc_tot = 0
    ecart_max = -1
    tab_k = [1, 2, 3, 5, 6, 7]

    for k in tab_k :
        for i in range(4) :
            tab = genere_system(k)
            if not TestGloutonCompatible(k-1, tab) :
                for s in range(PMAX, PMAX*F + 1) :
                    #print("k : ", k, "tab : ", tab)
                    tot+=1
                    temps = time.time()
                    val1 = AlgorithmeII(s, k-1, tab)
                    temps1 = time.time() - temps
                    
                    
                    temps = time.time()
                    val2 = AlgorithmeIII(s, k-1, tab)
                    temps2 = time.time() - temps
                    #print("val1 : ", val1, "val2", val2)

                    ecart = abs(val1-val2)
                    pourc_tot += ecart/val1
                    if ecart > ecart_max :
                        ecart_max = ecart
                    ecart_tot+=ecart

    return(ecart_tot/tot, ecart_max, pourc_tot/tot)        
                    
moy, max, pourc = ecarts_glouton_ou_pas()
print("moyenne : ", moy, " max : ", max, "pourcentage d'erreur : ", pourc)

