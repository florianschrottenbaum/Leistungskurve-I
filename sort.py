def bubble_sort(list):
    """Sorts a list of numbers in descending order using the bubble sort algorithm. We
    used a template from informatik (1. semestre) and modified it to sort in descending order."""
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j] < list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list