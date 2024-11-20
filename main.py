from algo1 import *
from algo2 import *
from algo3 import *
from genere_system import *

import os
import time
import random

PMAX = 700
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


def proportion_gloutons_compatibles() :

    tot = 0
    comp_glouton = 0

    tab_k = [1, 2, 3, 4, 5, 6, 9, 10, 20, 50, 100, 200]

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
            
    return comp_glouton/tot

#print("proportion : ", proportion_gloutons_compatibles())

def ecarts_glouton() :

    tab_k = [1, 2, 3, 9, 50, 200]

    stats_name = "stats_test.txt"

    
    with open(stats_name, "w") as stats : 
        stats.write("Taille_Systeme\tEcart_Moyen\tEcart_Max\tPourcentage_Difference\n")
    
        for k in tab_k :
            tot = 0
            ecart = 0
            ecart_max = 0
            pourc = 0
            for i in range(10) :
                tab = genere_system(k)
                if not TestGloutonCompatible(k, tab) :
                    for s in range(PMAX, PMAX*F + 1, 5) :
                        tot+=1

                        val1 = AlgorithmeII(s, k, tab)
                        
                        val2 = AlgorithmeIII(s, k, tab)

                        ecart_tmp = abs(val1-val2)
                        ecart += ecart_tmp

                        if val1!=0 :
                            pourc_tmp = ecart_tmp/val1  
                            pourc += pourc_tmp

                        else :
                            pourc_tmp = 0
                        
                        if ecart_tmp > ecart_max :
                            ecart_max = ecart_tmp
                        
            
            print("ecart moy : ", ecart)
            print("pourcentage : ", pourc)
            print("total : ", tot)

            if tot !=0 :
                ecart_moy = ecart/tot
                pourc_moyen = pourc/tot

            else : 
                ecart_moy = ecart
                pourc_moyen = pourc

            stats.write(f"{k}\t{ecart_moy}\t{ecart_max}\t{pourc_moyen}\n")

       
#ecarts_glouton()