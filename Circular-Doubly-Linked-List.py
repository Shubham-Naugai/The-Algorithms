class Node():
    def __init__(self, value=None):
        self.prev = None
        self.value = value
        self.next = None

class CDLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # Insertion in circular doubly linked list
    def insertionInCDLinkedList(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            newNode.prev = newNode
            newNode.next = newNode
            self.tail = newNode
        else:
            if location == 0:
                self.head.prev = newNode
                newNode.next = self.head
                newNode.prev = self.tail
                self.head = newNode
                self.tail.next = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                if tempNode == self.tail:
                    tempNode.next = newNode
                    newNode.prev = self.tail
                    newNode.next = self.head
                    self.head.prev = newNode
                    self.tail = newNode
                else:
                    nextNode = tempNode.next
                    tempNode.next = newNode
                    newNode.prev = tempNode
                    newNode.next = nextNode
                    nextNode.prev = newNode
                
    # Traversing in Circular Doubly Linked List
    def traversalInCDLinkedList(self):
        if self.head is None:
            print("Circular Linked List does not exist!")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
    
    # reverse traversal in Circular Doubly Linked List
    def reverseTraversalInCDLinkedList(self):
        if self.head is None:
            print("Circular Linked List does not exist!")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    # Searching in Circular Doubly Linked List
    def searchingInCDLinkedList(self, nodeValue):
        if self.head is None:
            return "Doubly Linked List does not exist"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return "Element not found"
                tempNode = tempNode.next
    
    # Deleting a node in Circular Doubly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print('Doubly Linked List does not exist')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.head.next = None
                    self.head.prev = None
                    self.tail = None
                else:
                    removableNode = self.head
                    self.head = removableNode.next
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                removableNode = tempNode.next
                if removableNode == self.tail:
                    tempNode.next = self.head
                    self.head.prev = tempNode
                    self.tail = tempNode
                else:
                    tempNode.next = removableNode.next
                    removableNode.next.prev = tempNode

    # Delete entire Circular Doubly Linked List
    def deleteEntireCDLinkedList(self):
        if self.head is None:
            print("The Linked-List does not exist")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None


CircularDoublyLinkedList = CDLinkedList()
CircularDoublyLinkedList.insertionInCDLinkedList(50, 0)
CircularDoublyLinkedList.insertionInCDLinkedList(23, 1)
CircularDoublyLinkedList.insertionInCDLinkedList(12, 2)
CircularDoublyLinkedList.insertionInCDLinkedList(72, 3)
CircularDoublyLinkedList.insertionInCDLinkedList(21, 4)
print([node.value for node in CircularDoublyLinkedList])
print("Traversing a Circular Doubly Linked List")
CircularDoublyLinkedList.traversalInCDLinkedList()
print("Reverse traversing a Circular Doubly Linked List")
CircularDoublyLinkedList.reverseTraversalInCDLinkedList()
print("Searching an element in Circular Doubly Linked List")
print(CircularDoublyLinkedList.searchingInCDLinkedList(21))
print("Deleting a node in Circular Linked List")
CircularDoublyLinkedList.deleteNode(0)
print([node.value for node in CircularDoublyLinkedList])
print("Deleting entire Circular Doubly Linked List")
CircularDoublyLinkedList.deleteEntireCDLinkedList()
print([node.value for node in CircularDoublyLinkedList])

