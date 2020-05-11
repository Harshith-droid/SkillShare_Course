def binarysearch(A,key, low, high):
    if low > high :
        return False
    else :
        mid = (low + high) // 2
        if key == A[mid]:
           return True
        elif key < A[mid]:
            return binarysearch(A, key, low, mid-1)
        else :
            return binarysearch(A, key, mid + 1, high)
    return False


List = [25,34,53,72,98,124,125,153,182]
found = binarysearch(List, 124, 0, 8)
print("The number 124 is: ", found)
