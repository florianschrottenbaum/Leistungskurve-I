def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

print(bubble_sort([34, 5, 7, 9, 3, 2]))
