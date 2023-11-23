def bubble_sort(lst):
    n = len(lst) - 1
    for i in range(n):
        for j in range(n - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
