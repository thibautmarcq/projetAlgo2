#/bin/bash

# Permet de run les bons tests à chaque fois

rm tests/*.txt
python3 genere_tests.py
python3 main.py