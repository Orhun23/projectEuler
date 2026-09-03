def lattice_paths_of_n(n):
    list2 = []
    my_list = []
    for i in range(1, n+2):
        list2.append(i)
    for i in range(1, n+2):
        my_list.append(list2)
    for i in range(0,n+1):
        for f in range(0,n+1):
            if f == 0 or i == 0:
                my_list[i][f] = 1
            else:
                my_list[i][f] = my_list[i-1][f]+my_list[i][f-1]
    return my_list[n][n]

print(lattice_paths_of_n(20))
#was torrandseo