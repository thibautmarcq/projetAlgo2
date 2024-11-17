#!/bin/bash

# Parcourir tous les fichiers .txt dans le dossier 'results'
for file in results/*.txt; do
    # Extraire le nom de base du fichier sans l'extension
    base_name=$(basename "$file" .txt)
    
    # Générer le graphique avec toutes les valeurs de s
    gnuplot -e "
        set terminal png;
        set output 'graphs/${base_name}_plot.png';
        set title 'Algorithm Times';
        set xlabel 's';
        set ylabel 'Time (seconds)';
        set key inside;
        set xtics rotate by -45;
        set format x '%.0f';
        plot '$file' using 1:2 with points title 'Algo1 Time', \
             '$file' using 1:3 with points title 'Algo2 Time', \
             '$file' using 1:4 with points title 'Algo3 Time';
    "
    
    # Générer le graphique avec les valeurs de s comprises entre 0 et 5000
    gnuplot -e "
        set terminal png;
        set output 'graphs/${base_name}_plot_0_1000.png';
        set title 'Algorithm Times (s between 0 and 1000)';
        set xlabel 's';
        set ylabel 'Time (seconds)';
        set key inside;
        set xtics rotate by -45;
        set xrange [0:1000];
        set format x '%.0f';
        plot '$file' using 1:2 with points title 'Algo1 Time', \
             '$file' using 1:3 with points title 'Algo2 Time', \
             '$file' using 1:4 with points title 'Algo3 Time';
    "
done