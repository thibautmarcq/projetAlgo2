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
                'file': file,
                'algo1_time': algo1_time,
                'algo2_time': algo2_time,
                'algo3_time': algo3_time
            })
    
    return results

results = compare_algorithms()
for result in results:
    print(f"File: {result['file']}, Algo1: {result['algo1_time']:.6f}s, Algo2: {result['algo2_time']:.6f}s, Algo3: {result['algo3_time']:.6f}s")