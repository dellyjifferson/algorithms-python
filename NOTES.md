# The notes I take from this learning journey
## What is Big O Notation

Big O Notation (Landau Symbol) is a notation that has taken its name from a Theorician named Edmund Landau. It is used to study the performance of an Algorithm. By taking an input "n" the Big O Notation describes how the running time grows as input size increases. Big-O focuses on the upper bound (worst-case) behavi. It classify algorithms as O(1), O(n), O(log n)...

## Binary Search Algorithm

The Binary Search Algorithm is one of the fastest Algorithm, it is used to search an element in a sorted array (If the array is not sorted it will give wrong result). It is fast because At each step, binary search removes half of the remaining search space.
Giving array = 2 | 4 | 6 | 8 | 10 | 12 , Target 8
First it point the middle element in the array which is 6, then it check if the value is equal to the target, if not eliminate a part of the array. As the target is greater it consider the part after 6 now the array becomes 8 | 10 | 12. Now the middle is 10 then repeat the process as the target is less it consider the left part which is 8 and it is equal to the target so found!!

## Linear Search Algorithm

The linear Search logic works on any array, the array does not have to be sorted because the algorithm compares each element of the array to the target one by one. It becomes very slow as the quantity of elements in the array grows. If we consider an array 2 | 4 | 6 | 8 | 10 | 12 and a target 8, the algorithm iterates on the array and compare the first element of the array to the target which is 2 if it is equal it moves to the next. When it is found it returns the position of the element.

### Comparison : Linear Search vs Binary Search

Linear Search: 
1- Works on any array
2- No sorting required
3- Complexity O(n)

Binary Search:
1- Requires sorted array
2- Much faster
3- Complexity O(log n)

POV: According to me the Binary Search is fast as long as the array is sorted if we are facing a case with an unordered array we better use the Linear Search Logic because sorting takes times. But that is as long as we gonna make only one search, if we gonna make many searches we better sort the array then use the Binary Search method.

## Sorting Algorithms
### Bubble Sort
Bubble is one of the simpliest method for sorting arrays. But it is slow O(n^2), it is that complex due to the nested loops for comparisons and swapping. The optimized version of that algorithm saves time by using a flag for when no swap occurs in the last pass of the loop. If no swap happened that means the list is already sorted O(n). Despite of its simplicity the Bubble Sort Algorithm  is rarely used in production systems because its performance degrades rapidly as the input size grows. As an Engineer this algorithm teaches me that some methods may look simple to implement but perfomance is not guaranteed  and choosing a perfect algorithm for a specific case require a deep study of that case in order to know how much data I will be dealing with.

### Insertion Sort
Insertion Sort Algorithm is one of the most used logic in small datasets (Not as standalone sorter for large datasets), because it is stable and efficient. It works like this: It considers the first element as sorted, then check the next elements, every time an element is not sorted i verifies it the sorted part to find where it belongs. The are two correct implementations, swap method and shift method. The swap method is not to efficient it writes to much in the memory, the recommended one is the shift method.
| Version     | Time  | Space | Memory Writes |
| ----------- | ----- | ----- | ------------- |
| Swap-based  | O(n²) | O(1)  | High          |
| Shift-based | O(n²) | O(1)  | Low           |
