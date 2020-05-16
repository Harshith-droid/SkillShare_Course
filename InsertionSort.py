def insertionsort(A):
    for i in range(1, len(A)):
        value = A[i]
        position = i

        while position > 0 and A[position -1] > value:
            A[position] = A[position-1]
            position = position - 1

        A[position] = value

A = [21, 15, 47, 96, 84]
print("Original Array: ", A)
insertionsort(A)
print("Sorted Array: ", A)