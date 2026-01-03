# The notes I take from this learning journey
## What is Big O Notation

Big O Notation (Landau Symbol) is a notation that has taken is name from a Theorician named Edmund Landau. It is used to study the performance of an Algorithm. By taking an input "n" as this input grows the algorithm can become slower or still remains fast. It ignores constant and focuses on the worst cases. It classify algorithms as O(1), O(n), O(log n)...

## Binary Search Algorithm

The Binary Search Algorithm is one of the fastest Algorithm, it is used to search an element in a sorted array (If the array is not sorted it will give wrong result). It is fast because it works by eliminating part of the array by cutting the array in half of  each time.'
Giving array = 2 | 4 | 6 | 8 | 10 | 12 , Target 8
First it point the middle element in the array which is 6, then it check if the value is equal to the target, if not eliminate a part of the array. As the target is greater it consider the part after 6 now the array becomes 8 | 10 | 12. Now the middle is 10 then repeat the process as the target is less it consider the left part which is 8 and it is equal to the target so found!!