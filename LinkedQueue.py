from exceptions import Empty

class LinkedQueue:

    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        newNode = self._Node(e, None)
        if self.is_empty():
            self._head = newNode
        else:
            self._tail._next = newNode
        self._tail = newNode
        self._size+= 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('LinkedQueue is Empty')
        value = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return value

    def first(self):
        if self.is_empty():
            raise Empty("LinkedQueue is Empty")
        return self._head._element

    def display(self):
        thead = self._head
        while thead:
            print(thead._element, end="-->")
            thead = thead._next
        print()


lq = LinkedQueue()
# lq.enqueue(20)
# lq.enqueue(30)
# lq.enqueue(40)
# lq.enqueue(50)
# lq.enqueue(60)
# lq.display()
# lq.dequeue()
# lq.display()
# print("Is empty: ", lq.is_empty())
# lq.display()
# print("First: ", lq.first())
# lq.display()
# lq.enqueue(69)
# lq.display()
