def selectionsort(numberlist):
    for i in range(len(numberlist) -1, 0, -1):
        max_position = 0
        for j in range(1, i+1):
            if numberlist[j] > numberlist[max_position]:
                max_position = j
        temp = numberlist[i]
        numberlist[i] = numberlist[max_position]
        numberlist[max_position] = temp

List = [21, 15, 47, 96, 84,33,21,77]
print("Original Array: ", List)
selectionsort(List)
print("Sorted Array: ", List)