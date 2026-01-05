def insertion_sort(arr):
    to_sort_length = range(1, len(arr))
    for i in to_sort_length:
        value_to_sort = arr[i]

        while i > 0 and arr[i - 1] > value_to_sort:
            arr[i], arr[i-1] = arr[i - 1], arr[i]
            i -= 1

    return arr
