class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        current = self.head
        if current is None:
            self.head = node
            return
        while current.next is not None:
            current = current.next
        current.next = node

    def remove(self, data):
        current = self.head
        prev = None
        if current is None:
            return
        while current.data != data:
            if current.next is None:
                return
            prev = current
            current = current.next
        if prev is None:
            if current is None:
                return
            self.head = current.next
            return
        prev.next = current.next

    def is_loop(self):
        s = set()
        current = self.head
        if current is None:
            return
        while current.next is not None:
            if current in s:
                return True
            s.add(current)
            current = current.next
        return False

    def count(self):
        length = 0
        current = self.head
        s = set()
        while current is not None:
            length += 1
            if current in s:
                break
            s.add(current)
            current = current.next
        return length

    def print(self):
        current = self.head
        length = self.count()
        for i in range(length):
            print(current.data)
            current = current.next

l = LinkedList()
loopnode = Node("x")
l.head = loopnode
l.add("a")
l.add("b")
l.add("c")
l.print()
print("")
n = l.head
while n.next is not None:
    n = n.next
n.next = loopnode

print(l.is_loop())

l.print()
print(l.count())