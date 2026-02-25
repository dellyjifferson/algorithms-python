# In this program we will the quick sort algorithm to sort a list of numbers.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Testing the quick sort function
if __name__ == "__main__":
    sample_array = [33, 10, 55, 26, 19, 42, 8]
    print("Unsorted array:", sample_array)
    sorted_array = quick_sort(sample_array)
    print("Sorted array:", sorted_array)