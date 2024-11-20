#!/bin/bash

# Parcourir tous les fichiers .txt dans le dossier 'results'
for file in stats/stats_proportion_compatibles/*.txt; do
    # Extraire le nom de base du fichier sans l'extension
    base_name=$(basename "$file" .txt)
    
    # Générer le graphique avec toutes les valeurs de s
    gnuplot -e "
        set terminal png;
        set output 'stats/plots/stats_proportion_compatibles${base_name}_plot.png';
        set title '${base_name}';
        set xlabel 'Valeur de k';
        set ylabel 'Difference de lalgo glouton avec dalgo dynamique';
        set key inside;
        set xtics rotate by -45;
        set format x '%.0f';
        plot '$file' using 1:2 with points title 'Proportion compatibles';
    "

    # gnuplot -e "
    #     set terminal png;
    #     set output 'thib/${base_name}_plot_log.png';
    #     set title '${base_name}';
    #     set xlabel 'Valeur de s';
    #     set ylabel 'Temps (secondes)';
    #     set key inside;
    #     set xtics rotate by -45;
    #     set format x '%.0f';
    #     set logscale x 2;
        
    #     plot '$file' using 1:2 with points title 'Temps AlgoI', \
    #          '$file' using 1:3 with points title 'Temps AlgoII', \
    #          '$file' using 1:4 with points title 'Temps AlgoIII';
    # "
    
    # Générer le graphique avec les valeurs de s comprises entre 0 et 5000
    # gnuplot -e "
    #     set terminal png;
    #     set output 'graphs/${base_name}_plot_0_1000.png';
    #     set title '${base_name} (entre 0 et 1000)';
    #     set xlabel 'Valeur de s';
    #     set ylabel 'Temps (secondes)';
    #     set key inside;
    #     set xtics rotate by -45;
    #     set xrange [0:1000];
    #     set format x '%.0f';
    #     plot '$file' using 1:2 with points title 'Temps AlgoI', \
    #          '$file' using 1:3 with points title 'Temps AlgoII', \
    #          '$file' using 1:4 with points title 'Temps AlgoIII';
    # "

    #     gnuplot -e "
    #     set terminal png;
    #     set output 'thib/${base_name}_plot_sans1.png';
    #     set title '${base_name}';
    #     set xlabel 'Valeur de s';
    #     set ylabel 'Temps (secondes)';
    #     set key inside;
    #     set xtics rotate by -45;
    #     set format x '%.0f';
    #     plot 
    #          '$file' using 1:3 with points title 'Temps AlgoII', \
    #          '$file' using 1:4 with points title 'Temps AlgoIII';
    # "

    #         gnuplot -e "
    #     set terminal png;
    #     set output 'thib/${base_name}_plot_sans1_log.png';
    #     set title '${base_name}';
    #     set xlabel 'Valeur de s';
    #     set ylabel 'Temps (secondes)';
    #     set key inside;
    #     set xtics rotate by -45;
    #     set logscale x 2;
    #     set format x '%.0f';
    #     plot 
    #          '$file' using 1:3 with points title 'Temps AlgoII', \
    #          '$file' using 1:4 with points title 'Temps AlgoIII';
    # "
    

done