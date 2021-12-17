# SortingAlogrithms
A Variety of sorting alogrithms.

## Technical Details

### Time complexity

#### In the code
To time the code I will be using a function 'run_sorting_algorithm' to run another function from the 'timeit' module. The function then prints the data.

## Types of algorithms shown

### Python's inbuilt sorting algorithm
Python has its own inbuilt algorithm you can use using:
sorted(array)
Time: 0.0012252000014996156

### Bubble sort
This algorithm swaps with its neighbor if the neighbors value is bigger.
Time: 0.9154005000018515
Time complexity: O(n2)

## Insertion sort
Sorts the list one item at a time by placing it in its correct position.
Time: 0.37257320000207983
Time complexity: O(n2)

## Merge sort
Splits the array into two parts and use recursion to solve each half.
Combines to give a final solution.
Time: 0.04413840000052005
Time complexity: O(n log2n)