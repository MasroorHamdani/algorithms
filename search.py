import math
def linear_search(arr, num, len):
    for i in range(0, len):
        if(arr[i] == num):
            return i
    return -1

def binary_search(arr, l, r, num):
    if r >= l:
        mid = l + (r-l)/2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            return binary_search(arr, mid+1, r, num)
        else:
            return binary_search(arr, l, mid-1, num)
    else:
        return -1

if __name__=='__main__':
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    n = len(arr)
    print("****** Linear Search ******")
    result = linear_search(arr, 23, n)
    if(result == -1):
        print('Element is not Present')
    else:
        print("Element '23' present at location", result)

    result = linear_search(arr, 9, n)
    if(result == -1):
        print('Element 9 is not Present')
    else:
        print("Element '23' present at location", result)

    result = linear_search(arr, 2, n)
    if(result == -1):
        print('Element is not Present')
    else:
        print("Element '2' present at location", result)

    print("****** Binary Search ******")
    arr = [ 2, 3, 4, 10, 40 ] 
    x = 10
    
    # Function call 
    result = binary_search(arr, 0, len(arr)-1, x) 

    if result != -1: 
        print ("Element is present at index % d" % result)
    else: 
        print ("Element is not present in array")
