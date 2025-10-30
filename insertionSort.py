def insertion(list_to_sort: list[int]) -> list[int]:
    for i in range(len(list_to_sort)):
        for j in range(i, len(list_to_sort)):
            if list_to_sort[j] < list_to_sort[i]:
                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
    return list_to_sort

