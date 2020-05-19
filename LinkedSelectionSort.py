
from doublylinkedlist import DoublyLinkedList


def selectionsort(numberlist):
    for i in range(len(numberlist) - 1, 0, -1):
        max_position = 0
        for j in range(1, i + 1):
            if numberlist[j] > numberlist[max_position]:
                max_position = j
        temp = numberlist[i]
        numberlist[i] = numberlist[max_position]
        numberlist[max_position] = temp


def dlinkselectionsort(dlinklist):
    ttail = dlinklist._tail

    for i in range(len(dlinklist)-1, 0, -1):
        max_position = dlinklist._head
        for j in range(1, i+1):
            if max_position._next._element > max_position._element:
                max_position = max_position._next
            
        temp = ttail._element
        ttail._element = max_position._element
        max_position._element = temp

        ttail = ttail._prev
        dlinklist.display()

DL = DoublyLinkedList()
DL.add_last(10)
DL.add_last(20)
DL.add_last(30)
DL.add_last(7)
DL.add_last(40)
DL.add_last(18)
DL.add_last(2)
DL.display()
print("Start")
dlinkselectionsort(DL)
print("End")
DL.display()
