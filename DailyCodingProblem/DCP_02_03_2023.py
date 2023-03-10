"""
You are given an array of integers, where each element represents the maximum number of steps that can be jumped going forward from that element. Write a function to return the minimum number of jumps you must take in order to get from the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal solution involves jumping from 6 to 5, and then from 5 to 9."""


from typing import List


def min_number_of_jumps(Arr: List, n: int) -> int:
    """
    Return the minimum number of jumps
    Given a list [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2

    :param List: list of integers
    :param n List: size of the list
    :return int: the minimum number of jumps
    """
    if n <= 1:
        return 0

    curr_max_reach = Arr[0]
    steps_count = Arr[0]
    jump = 0

    for start in range(1, n - 1):
        curr_max_reach = max(curr_max_reach, start + Arr[start])
        steps_count = steps_count - 1

        if steps_count == 0:
            jump = jump + 1
            steps_count = curr_max_reach - start
    return jump + 1


# Driver Program to test above function
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)
print(size)
print("Minimum number of jumps to reach", "end is", min_number_of_jumps(arr, size))


# We are initially at the start of the array
# Arr[i] = x, this mean that from index i, we can jump to the following i+1, i+2 ...,i+x
# Aim is to return the minimum numbef of jumps
