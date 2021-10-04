def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start = 0
    end = len(input_list)-1
    while start <= end:
        mid_index = (start+end)//2
        mid_val = input_list[mid_index]
        start_val = input_list[start]
        end_val = input_list[end]
        # print(start)
        # print(end)
        if number == mid_val:
            return mid_index
        if number < mid_val:
            if number < start_val:
                start = mid_index + 1
            else:
                end = mid_index-1
        elif number > mid_val:
            if number <= end_val:
                start = mid_index + 1
            else:
                end = mid_index-1
    if start> 0 and start < len(input_list) and input_list[start] == number:
        return start
    return -1


# THis is for unit testing.
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 100])
test_function([[1,2,3,4], 4])
