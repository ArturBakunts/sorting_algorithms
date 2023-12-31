def merge_two_sorted_list(lst1, lst2):
    i = j = 0
    merge_lst = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merge_lst.append(lst1[i])
            i += 1
        else:
            merge_lst.append(lst2[j])
            j += 1

    return merge_lst + lst1[i:] + lst2[j:]


def recursive_sort_by_merge(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = recursive_sort_by_merge(lst[:mid])
    right = recursive_sort_by_merge(lst[mid:])
    return merge_two_sorted_list(left, right)

