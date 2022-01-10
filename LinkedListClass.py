class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class Linked_List():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return " --> ".join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

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


LinkedList = Linked_List()
LinkedList.insertionInList(0, 0)
LinkedList.insertionInList(1, 1)
LinkedList.insertionInList(1, 2)
LinkedList.insertionInList(2, 3)
LinkedList.insertionInList(3, 4)
LinkedList.insertionInList(4, 5)


print(LinkedList)
print(len(LinkedList))
for i in LinkedList:
    print(i)