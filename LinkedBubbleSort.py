from linkedlist import LinkedList

def bubblesort(A):

    for i in range(len(A)-1, 0, -1):
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

def linkbubblesort(linkList):

    for i in range(len(linkList)-1, 0, -1):
        thead = linkList._head
        for j in range(i):
            if thead._element > thead._next._element:
                thead._element, thead._next._element = thead._next._element, thead._element
            thead = thead._next
        linkList.display()



L = LinkedList()
L.add_last(20)
L.add_last(10)
L.add_last(30)
L.add_last(7)
L.add_last(15)
L.add_last(18)
L.add_last(2)
L.display()
linkbubblesort(L)
L.display()