# Algorithm
This folder includes all sorting algorithms that have been studying throughout  the learning  

SortingAlgorithms.cpp file contains Merge Sort, Quick Sort, Count Sort, and Bucket Sort Algorithms

## Merge Sort 
Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
###Time Complexity: 
θ(nLogn)

## Quick Sort
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

1)Always pick first element as pivot.
2)Always pick last element as pivot (implemented below)
3)Pick a random element as pivot.
4)Pick median as pivot.

###Time Complexity: 
###Worst Case: O(n^2)
but mostly Average case: O(nlogn)
