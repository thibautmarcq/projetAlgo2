## main pour la génération des temps des algorithmes (tests), en fonction de s, k et V
# > voir plots/genere_plots.sh pour générer le png des graphiques obtenus


from algo1 import *
from algo2 import *
from algo3 import *

import time


def read_test_file(filepath):
    print(filepath)
    with open(filepath, 'r') as file:
        s = int(file.readline().strip())
        k = int(file.readline().strip())
        V = [int(line.strip()) for line in file.readlines()]
        print("s k v", s, k, V)
    return s, k, V


def generate_table(k, d): # génère la table demandée d^(k-1)
    V = [0] * k
    if k > 0:
        V[0] = 1
    if k > 1:
        V[1] = 2
    for i in range(2, k):
        V[i] = d ** (i - 1)
    return V

def compare_algorithms(k, V):
    results = []
    for s in range(1, 1000):
        print("s k v", s, k ,V)
        
        algo1_time=0
        if(s<500):
            start_time = time.time()
            AlgorithmeI(s, k, V)
            algo1_time = time.time() - start_time
                
        print(algo1_time)
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


def make_tests():
    d=4
    k = 10
    print("d ", d)
    V = generate_table(k, d)
    results = compare_algorithms(k,V)
    txt_file = 'thib/results_d'+str(d)+'_k'+str(k)+'.txt'

    # ecrit les résultats dans le fichier texte
    with open(txt_file, mode='w') as file:
        file.write('s\talgo1_time\talgo2_time\talgo3_time\n') #ligne en haut

        for result in results:
            file.write(f"{result['s']}\t{result['algo1_time']:.6f}\t{result['algo2_time']:.6f}\t{result['algo3_time']:.6f}\n")


make_tests()