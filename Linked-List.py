# Linked List

class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Insert a value in linked list
    def insertionInList(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
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
    
    # Traversing a linked list
    def traversalInList(self):
        if self.head is None:
            print("Linked-List does not exist")
        else:
            tempNode = self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode = tempNode.next

    # Searching in linked list
    def searchingInList(self, nodeValue):
        if self.head is None:
            return "Linked-List does not exist"
        else:
            tempNode = self.head
            while tempNode is not None:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            else:
                return "The value does not exist"

    # Deleting a node in linked list
    def deleteNode(self, location):
        if self.head is None:
            print("Linked-List does not exist!")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
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
    def deleteEntireList(self):
        if self.head is None:
            print("The Linked-List does not exist")
        else:
            self.head = None
            self.tail = None

    # removing dublicates
    def removeDublicates(self):
        tempNode = self.head
        newLinkedList = set()
        newLinkedList.add(self.head.value)
        while tempNode.next:
            if tempNode.next in newLinkedList:
                tempNode.next = tempNode.next.next
            else:
                newLinkedList.add(tempNode.next.value)
                tempNode = tempNode.next
        return list(newLinkedList)


SinglyLinkedList = SLinkedList()
SinglyLinkedList.insertionInList(0, 0)
SinglyLinkedList.insertionInList(1, 1)
SinglyLinkedList.insertionInList(1, 2)
SinglyLinkedList.insertionInList(2, 3)
SinglyLinkedList.insertionInList(3, 4)
SinglyLinkedList.insertionInList(4, 5)
print("Linked-List: ", end = "")
print([node.value for node in SinglyLinkedList])

print("Removing dublicates: ")
print(SinglyLinkedList.removeDublicates())

print("Traversing all elements of linked list: ")
SinglyLinkedList.traversalInList()

print("Searching an element: ", SinglyLinkedList.searchingInList(3))

SinglyLinkedList.deleteNode(4)
print("Deleting a node in Linked list: ", [tempNode.value for tempNode in SinglyLinkedList])

SinglyLinkedList.deleteEntireList()
print("Deleting entire linked list: ", [tempNode.value for tempNode in SinglyLinkedList])
