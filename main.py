from algo1 import *
from algo2 import *
from algo3 import *
from genere_system import *

import os
import time
import random

PMAX = 400
F = 5
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

    tab_k = [1, 2, 3, 4, 5, 6, 9, 10, 20, 50, 100, 200]
    tab_k.sort()

    with open("proportion_glouton_compatibles.txt", "w") as g_comp :
        g_comp.write("Taille_Systeme\tPourcentage_compatibles\n")
        for k in tab_k :
            tot_partiel = 0
            comp_glouton_partiel = 0
            for i in range(10000) :    
                tot+=1
                tot_partiel+=1
                tab = genere_system(k)
                if TestGloutonCompatible(k, tab) :
                    comp_glouton+=1
                    comp_glouton_partiel+=1
            proportion = comp_glouton_partiel/tot_partiel
            g_comp.write(f"{k}\t{proportion}\n")
            print("k : ", k)
            print("\t tot : ", tot_partiel)
            print("\t compatibles : ", comp_glouton_partiel)
            print("\t proportion d'instances glouton-compatibles : ", comp_glouton_partiel/tot_partiel)
        
    return comp_glouton/tot

#print("proportion : ", proportion_gloutons_compatibles())

def ecarts_glouton() :
    tab_k = [1, 2, 3, 9, 50]

    logs_name = "logs2.txt"
    stats_name = "stats_ecarts_petites_valeurs.txt"

    with open(logs_name, "w") as logs:
        with open(stats_name, "w") as stats : 
            stats.write("Taille_Systeme\tEcart_Moyen\tEcart_Max\tPourcentage_Difference\n")
        
            for k in tab_k :
                tot = 0
                ecart = 0
                ecart_max = 0
                pourc = 0
                for i in range(5) :
                    tab = genere_system(k)
                    if not TestGloutonCompatible(k, tab) :
                        for s in range(PMAX, PMAX*F + 1, 5) :
                            text = "k, s : "+ str(k) + ", " + str(s) + "\n"
                            logs.write(text)
                            tot+=1

                            
                            val1 = AlgorithmeII(s, k, tab)
                            text = "\tval1 : " + str(val1) + "\n"
                            logs.write(text)
                            
                            
                            val2 = AlgorithmeIII(s, k, tab)
                            text = "\tval2 : " + str(val2) + "\n"
                            logs.write(text)

                            ecart_tmp = abs(val1-val2)
                            ecart += ecart_tmp

                            if val1!=0 :
                                pourc+= ecart_tmp/val1  
                            
                            if ecart_tmp > ecart_max :
                                ecart_max = ecart
                
                if tot !=0 :
                    ecart_moy = ecart/tot
                    pourc_moyen = pourc/tot

                else : 
                    ecart_moy = ecart
                    pourc_moyen = pourc

                # logs.write("\n")
                # logs.write(f"{k}\t{s}\t{ecart_moy}\t{ecart_max}\t{pourc_moyen}\n")
                # logs.write("\n\n")

                stats.write(f"{k}\t{ecart_moy}\t{ecart_max}\t{pourc_moyen}\n")

       
ecarts_glouton()                    
# moy, max, pourc = ecarts_glouton_ou_pas()
# print("moyenne : ", moy, " max : ", max, "pourcentage d'erreur : ", pourc)

