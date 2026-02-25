# In this program we implement the insertion sort algorithm to sort a list of even numbers.
def insertion_sort_swap(arr):
    to_sort_length = range(1, len(arr))
    for i in to_sort_length:
        value_to_sort = arr[i]

        while i > 0 and arr[i - 1] > value_to_sort:
            arr[i], arr[i-1] = arr[i - 1], arr[i]
            i -= 1

    return arr

# Testing the function to sort a list of even numbers

# Insertion Sort Algorithm Shift method

def insertion_sort_shift(arr):
    for i in range(1, len(arr)):
        value_to_sort = arr[i]
        position = i

        while position > 0 and arr[position - 1] > value_to_sort:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = value_to_sort
    return arr

# Testing the function to sort a list of odd numbers
if __name__ == "__main__":
    # Testing the function to sort a list of even numbers (insertion_sort_swap)
    even_numbers = [28, 4, 2, 6, 8, 10, 14, 16, 12]
    print("Original even numbers:", even_numbers)
    sorted_numbers = insertion_sort_swap(even_numbers)
    print("Sorted even numbers using swap method:", sorted_numbers)
    # Testing the function to sort a list of odd numbers (insertion_sort_shift)
    odd_numbers = [27, 3, 1, 5, 7, 9, 13, 15, 11]
    print("Original odd numbers:", odd_numbers)
    sorted_odd_numbers = insertion_sort_shift(odd_numbers)
    print("Sorted odd numbers using shift method:", sorted_odd_numbers)