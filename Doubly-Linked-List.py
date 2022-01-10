class Node():
    def __init__(self, value=None):
        self.prev = None
        self.value = value
        self.next = None

class DLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertionInDLinkedList(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                nextNode = self.head
                newNode.prev = None
                newNode.next = nextNode
                nextNode.prev = newNode
                self.head = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                if tempNode == self.tail:
                    newNode.prev = tempNode
                    tempNode.next = newNode
                    newNode.next = None
                    self.tail = newNode
                else:
                    nextNode = tempNode.next
                    newNode.next = nextNode
                    newNode.prev = tempNode
                    tempNode.next = newNode
                    nextNode.prev = newNode
    
    # Traversal in Double linked list
    def traversalInCLinkedList(self):
        if self.head is None:
            print("Doubly Linked List does not exist!")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    # Reverse Traversal in Doubly Linked List
    def reverseTraversingInLinkedList(self):
        if self.head is None:
            print("Doubly Linked List does not exist!")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # Searching in Doubly Linked List
    def searchingInDLinkedList(self, nodeValue):
        if self.head is None:
            return "Doubly Linked List does not exist"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "Element not found..."

    # Deleting a node in Doubly Linked List
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
                    nextNode = self.head
                    self.head = nextNode.next
                    self.head.prev = None
                    nextNode.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                removableNode = tempNode.next
                if removableNode == self.tail:
                    tempNode.next = None
                    removableNode.prev = None
                    self.tail = tempNode
                else:
                    tempNode.next = removableNode.next
                    removableNode.next.prev = tempNode

    # Delete entire Doubly Linked List
    def deleteEntireDLinkedList(self):
        if self.head is None:
            print("The Linked-List does not exist")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None


DoublyLinkedList = DLinkedList()
DoublyLinkedList.insertionInDLinkedList(2, 0)
DoublyLinkedList.insertionInDLinkedList(5, 1)
DoublyLinkedList.insertionInDLinkedList(78, 2)
DoublyLinkedList.insertionInDLinkedList(1, 3)
print([node.value for node in DoublyLinkedList])
DoublyLinkedList.deleteNode(3)
print([node.value for node in DoublyLinkedList])
print("Traversal Doubly Linked List")
DoublyLinkedList.traversalInCLinkedList()
print("Reverse Traversal in Doubly Linked List")
DoublyLinkedList.reverseTraversingInLinkedList()
print("Searching in Doubly Linked List")
print(DoublyLinkedList.searchingInDLinkedList(78))
DoublyLinkedList.deleteEntireDLinkedList()
print([node.value for node in DoublyLinkedList])
