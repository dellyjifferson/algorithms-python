# This program uses the linear logic to find an element in a list/array

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None

# Testing linear search function
if __name__ == "__main__":
    array = [4, 5, 1, 8, 7, 3, 2, 9]

    result = linear_search(array, 8)
    if result != None:
        print(f"Found at position {result}")
    else:
        print("Not Found!")