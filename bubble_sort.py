# In this program we will see two version of bubble sort algorithm

def bubble_sort_v1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Optimized version of bubble sort
def bubble_sort_v2(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Testing the bubble sort functions
array1 = [64, 34, 25, 12, 22, 11, 90]
array2 = [5, 1, 4, 2, 8]
print("Original array1:", array1)
sorted_array1_v1 = bubble_sort_v1(array1.copy())
print("Sorted array1 using bubble_sort_v1:", sorted_array1_v1)
print("Original array2:", array2)
sorted_array2_v2 = bubble_sort_v2(array2.copy())
print("Sorted array2 using bubble_sort_v2:", sorted_array2_v2)