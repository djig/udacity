import math
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number<=1:
        return number
    start = 2
    end = number//2
    while start <= end:
        center = start + (end-start)//2
        new_num = center*center
        if new_num == number:
            return center
        elif new_num > number:
            end = center -1
        else:
            start = center + 1
    # this is for finding near square value for number and return
    if abs(number-start* start) < abs(number-end* end):
        return start
    else:
        return end
    pass

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (-1 == sqrt(-1)) else "Fail")
print ("Pass" if  (100000 == sqrt(10000000000)) else "Fail")
