from node import linkedListNode


class linkedlist:
    def __init__(self, number):
        self.head = linkedListNode(number)
        self.tail = self.head
        # this doesn't create a new node that is a duplicate node because
        # without the class linkedListNode it can't create a new instance.
        # linkedListNode is like a blueprint which is used to create multiple instances that can actually be accessed.
        # in the insert we will update the None values accordingly to the tail or head.

    def insert(self, number):
        Node = linkedListNode(number, None, self.tail)
        self.tail.next = Node
        self.tail = Node

    def __str__(self):
        return


LL1 = linkedlist(5)
LL1.insert(7)
print(LL1.head.next)
LL1.insert(9)
print(LL1.tail.previous)
print(LL1.tail)
# when we call print on the head it calls to the print function in the node class in node.py,
# but if we called print on Ll1 our linked list it would call on the linkedList class in this file
