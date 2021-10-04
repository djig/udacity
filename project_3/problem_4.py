def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    start = 0
    l = len(input_list)
    end = l-1
    i= 0
    while i<= end:
        if input_list[i] == 0:
            input_list[i], input_list[start] = input_list[start], input_list[i]
            start+=1
            i+=1
        elif input_list[i] == 2:
            input_list[i], input_list[end] = input_list[end], input_list[i]
            end-=1
        else:
            i+=1
    # print(end)
    return input_list
    pass

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
test_function([0,2,0, 1, 0,2,2,2])
test_function([0])
test_function([])
test_function([1,1,1])
test_function([2,2])
test_function([0,0,1,2,1,2])