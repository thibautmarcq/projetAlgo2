def genere_tests() : 

    tab_d = [4]
    # tab_d = [2, 3, 4] 
    tab_s = [7, 12, 68, 120, 200, 300, 1009, 1999, 14852, 45279]
    # tab_s = [7, 12, 68, 120, 200, 300]
    tab_k = [10]
    # tab_k = [1, 2, 3, 7, 11]

    for s in tab_s :
        for d in tab_d :
            for k in tab_k :
                filename = "tests/test_d" + str(s) + "_d" + str(d) + "_k" + str(k) + ".txt"
                with open(filename, "w") as file :
                    file.write(str(s) + "\n")
                    file.write(str(k) + "\n")
                    for i in range(k) :
                        capacite = d**i
                        file.write(str(capacite) + "\n")

genere_tests()