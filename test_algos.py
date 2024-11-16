from algo1 import *
from algo2 import *
from algo3 import *
import os


def temps_algos_compares():
    directory = './tests'
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            filename = filepath[8:-4]
            file_list.append(filename)
            
    return file_list


files = temps_algos_compares()
for f in files :
    print(f)

# temps_algos_compares()