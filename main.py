from algo1 import *
from algo2 import *
from algo3 import *

import os
import time

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

results = compare_algorithms()
txt_file = 'results.txt'

# Écrire les résultats dans le fichier texte
with open(txt_file, mode='w') as file:
    file.write('s\talgo1_time\talgo2_time\talgo3_time\n')

    for result in results:
        file.write(f"{result['s']}\t{result['algo1_time']:.6f}\t{result['algo2_time']:.6f}\t{result['algo3_time']:.6f}\n")