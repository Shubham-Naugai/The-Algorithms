class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    
    def insertionInCLinkedList(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            newNode.next = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
    
    # Traversing a Circular linked list
    def traversalInCLinkedList(self):
        if self.head is None:
            print("Circular Linked List does not Exist!")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
    
    # Searching in Circular linked list
    def searchingInCLinkedList(self, nodeValue):
        if self.head is None:
            return "Circular Linked List does not exist!"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "Element not found..."
    
    # Deleting a node in linked list
    def deleteNode(self, location):
        if self.head is None:
            print("Circular Linked List does not exist!")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                removableNode = tempNode.next
                tempNode.next = removableNode.next
                if removableNode == self.tail:
                    self.tail = tempNode
            
    # Delting entire linked list 
    def deleteEntireCLinkedList(self):
        if self.head is None:
            print("The Linked-List does not exist")
        else:
            self.head = None
            self.tail.next = None
            self.tail = None


CircularLinkedList = CLinkedList()
CircularLinkedList.insertionInCLinkedList(3, 0)
CircularLinkedList.insertionInCLinkedList(6, 1)
CircularLinkedList.insertionInCLinkedList(2, 2)
CircularLinkedList.insertionInCLinkedList(4, 3)
print([node.value for node in CircularLinkedList])
CircularLinkedList.traversalInCLinkedList()
print(CircularLinkedList.searchingInCLinkedList(4))
CircularLinkedList.deleteNode(3)
print([node.value for node in CircularLinkedList])
CircularLinkedList.deleteEntireCLinkedList()
print([node.value for node in CircularLinkedList])
