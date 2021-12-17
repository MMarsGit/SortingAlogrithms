from random import randint
import timeit
import matplotlib.pyplot as plt
import numpy as np
import math

#GLOBALS
ARRAY_LENGTH = 1000
array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

# VISUALISATIONS
def plot_graph():
    #%%
    plt.rcParams['figure.figsize'] = [10, 6]

    ns = np.linspace(10, 10_000, 50, dtype=int)
    ts = [timeit.timeit('sum(range({}))'.format(n), number=100)for n in ns]

    plt.plot(ns, ts, 'or')
    plt.show()

#RUNTIME CALCULATOR
def run_sorting_algorithm(algorithm, array):

    # Code supplied by: https://realpython.com/sorting-algorithms-python/ 

    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

# SORTING ALGORITHMS
# Compare value with neighbor, if your value is bigger swap positions
def bubble_sort(array):


    loops = len(array)

    for array_index in range(loops):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        for j in range(loops - array_index - 1):
            #Compare value with neighbor
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                #sorting occured, so not sorted
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array

# Works backwards in the array to find the items correct position
def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for item in range(1, len(array)):
        key_item = array[item]
        reverseCount = item - 1

        while reverseCount >= 0 and array[reverseCount] > key_item:
            # moves the key item position by one
            array[reverseCount + 1] = array[reverseCount]
            reverseCount -= 1

        # When loop is satisfied set the final key item position
        array[reverseCount + 1] = key_item

    return array

def _merge_sort(left, right):
    # return if left is empty
    if len(left) == 0:
        return right

    # return if right is empty
    if len(right) == 0:
        return left

    result = []
    # Set the left and right index to origin
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # When the left number is smaller than the right number
        # add to result array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            # When the right number is bigger add to result array
            result.append(right[index_right])
            index_right += 1

        # When the end of either array is reached, add the other arrays items to the result array
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    #If there is one or less items then exit.
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return _merge_sort(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

if __name__ == "__main__":
    #run_sorting_algorithm(algorithm="merge_sort", array=array)
    plot_graph()