def selection_sort(list):
    for i in range(len(list)-1, -1, -1):
        i_max = i
        for j in range(0, i):
            if list[j] > list[i_max]:
                i_max = j
        list[i], list[i_max] = list[i_max], list[i]
    return list

print(selection_sort([3, 2, 1, 5, 4])) # [1, 2, 3, 4, 5]
