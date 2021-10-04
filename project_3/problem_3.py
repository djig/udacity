
# this is using merge sort to sort array asc
def rearrange_digits_merge_sort(input_list):
    """
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return [0, 0]
    def merge(a1, a2):
        ans = []
        i =0
        j =0
        while i < len(a1) and j < len(a2):
            if i < len(a1) and j < len(a2):
                if a1[i] > a2[j]:
                    ans.append(a1[i])
                    i +=1
                else:
                    ans.append(a2[j])
                    j+=1
        while i< len(a1):
            ans.append(a1[i])
            i +=1
        while j< len(a2):
            ans.append(a2[j])
            j +=1
        
        return ans
    def helper(arr, start,end):
        if start == end:
            return [arr[start]]
        if start + 1 ==  end:
            if arr[start]> arr[end]:
                return [arr[start], arr[end]]
            else:
                return [arr[end], arr[start]]
        mid = (start+end)//2
        left = helper(arr, start, mid)
        right = helper(arr, mid+1, end)
        
        return merge(left, right)
    sorted_arr = helper(input_list, 0 , len(input_list)-1)
    res_1 =[]
    res_2 = []
    for i in range(0, len(sorted_arr)):
        if i % 2 == 0:
            res_1.append(sorted_arr[i])
        else:
            res_2.append(sorted_arr[i])
    ans_1=0
    ans_2 =0
    for i in range(0, len(res_1)):
        ans_1 += res_1[i]* pow(10,(len(res_1)-i-1))
    for i in range(0, len(res_2)):
        ans_2 += res_2[i]* pow(10,(len(res_2)-i-1))
    return [ans_1,ans_2]

    pass

#  this is using pivot index
def rearrange_digits_quick_sort(input_list):
    """
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return [0, 0]
    def partition(arr, start, end):
        p_i = end
        pivot = arr[p_i]
        j = start
        for i in range(start, end):
            if arr[i] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
                j +=1
        tmp = arr[j]
        arr[j] = pivot
        arr[p_i] = tmp
        return j
  
    def helper(arr, start,end):
        if start < end:
            pi = partition(arr, start, end)
            helper(arr, start, pi-1)
            helper(arr, pi+1, end)
       
    helper(input_list, 0 , len(input_list)-1)
    
    res_1 =[]
    res_2 = []
    for i in range(0, len(input_list)):
        if i % 2 == 0:
            res_1.append(input_list[i])
        else:
            res_2.append(input_list[i])
    ans_1=0
    ans_2 =0
    for i in range(0, len(res_1)):
        ans_1 += res_1[i]* pow(10,(len(res_1)-i-1))
    for i in range(0, len(res_2)):
        ans_2 += res_2[i]* pow(10,(len(res_2)-i-1))
    return [ans_1,ans_2]

    pass

def test_function(test_case):
    # output = rearrange_digits_merge_sort(test_case[0])
    output_1 = rearrange_digits_merge_sort(test_case[0])
    output_2 = rearrange_digits_quick_sort(test_case[0])
    solution = test_case[1]
    if sum(output_1) == sum(solution) and sum(output_2) == sum(solution):
        print("Pass")
    else:
        print("Fail")
# 5 testcases
test_cases = [
    [[1, 2, 3, 4, 5], [542, 31]],
    [[4, 6, 2, 5, 9, 8], [964, 852]],
    [[1,2], [3, 0]],
    [[4,5,6], [64, 5]],
    [[],[0,0]]
]
for test_case in test_cases:
    test_function(test_case)
