""" 
Author: J. Jifferson Delly
Date: 1/1/2026
Program: Binary Search Algorithm Implementation
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <=right:
        mid = (left+right) // 2
        mid_value = arr[mid]
        if mid_value == target:
            return mid
        elif mid_value > target:
            right = mid - 1
        else:
            left = mid + 1
    return None

# Let's try the function
sequence = [2, 4, 6, 8, 10, 12]
print(binary_search(sequence, 8))