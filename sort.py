def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

def selection_sort(list):
    for i in range(len(list)-1, -1, -1):
        i_max = i
        for j in range(0, i):
            if list[j] > list[i_max]:
                i_max = j
        list[i], list[i_max] = list[i_max], list[i]
    return list