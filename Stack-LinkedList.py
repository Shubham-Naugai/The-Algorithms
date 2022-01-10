class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Stack:
    def __init__(self):
        self.customLinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.customLinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.customLinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.customLinkedList.head
        self.customLinkedList.head = newNode

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty!")
        else:
            nodeValue = self.customLinkedList.head.value
            self.customLinkedList.head = self.customLinkedList.head.next
            print(nodeValue, "is removed from stack")
    
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty!")
        else:
            nodeValue = self.customLinkedList.head.value
            print(nodeValue, "is last node")

    def delete(self):
        self.customLinkedList.head = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.isEmpty())
print(customStack)
print("------")
# customStack.pop()
print("------")
customStack.peek()
print("------")

while not customStack.isEmpty():
    customStack.pop()
    customStack.pop()

customStack.peek()
