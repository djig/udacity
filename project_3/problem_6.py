def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    def helper(arr, start, end):
        if start == end:
            return (arr[start], arr[start])
        if start + 1 == end:
            if arr[start] > arr[end]:
                return (arr[end], arr[start])
            else:
                return (arr[start], arr[end])
        else:
            mid = (start+end)//2
            left_min, left_max = helper(arr, start, mid)
            right_min, right_max = helper(arr, mid+1, end)
            min_res = left_min
            max_res = left_max
            if min_res > right_min:
                min_res = right_min
            if max_res < right_max:
                max_res = right_max
            return (min_res, max_res) 
    if len(ints) == 0:
        return (None, None)
    return helper(ints, 0, len(ints)-1)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 1000000)]
random.shuffle(l)
print(get_min_max(l))
print(get_min_max([1]))
print(get_min_max([]))

