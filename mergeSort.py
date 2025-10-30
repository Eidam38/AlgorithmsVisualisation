def mergeSort(list_to_sort):
    # Base case: if the list is of length 1 or empty, it's already sorted
    if len(list_to_sort) > 1:
        left_half = list_to_sort[:len(list_to_sort) // 2]
        right_half = list_to_sort[len(list_to_sort) // 2:]

        mergeSort(left_half)
        mergeSort(right_half)

        i: int = 0 # index for left_half
        j: int = 0 # index for right_half
        k: int = 0 # index for merged_list

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list_to_sort[k] = left_half[i]
                i += 1
            else:
                list_to_sort[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements of left_half
        while i < len(left_half):
            list_to_sort[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements of right_half 
        while j < len(right_half):
            list_to_sort[k] = right_half[j]
            j += 1
            k += 1

    return list_to_sort