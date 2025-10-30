
def bubble(list_to_sort: list[int]) -> list[int]:
    sorted: bool = False
    list_length: int = len(list_to_sort)
    while not sorted:
        sorted = True
        list_length -= 1
        for i in range(list_length):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                sorted = False
    return list_to_sort