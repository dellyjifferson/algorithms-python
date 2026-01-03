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