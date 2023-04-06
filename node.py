class linkedListNode:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous
    def __str__(self):
        return str(self.value)
