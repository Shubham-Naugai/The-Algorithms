class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Queue:
    def __init__(self):
        self.cutomLinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.cutomLinkedList]
        return " ".join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.cutomLinkedList.head == None:
            self.cutomLinkedList.head = newNode
            self.cutomLinkedList.tail = newNode
            # print(newNode.value, "is enqueued in the Queue(using Linked List)")
        else:
            self.cutomLinkedList.tail.next = newNode
            self.cutomLinkedList.tail = newNode
            # print(newNode.value, "is enqueued at the end of the Queue(using Linked List)")

    def isEmpty(self):
        if self.cutomLinkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            tempNode = self.cutomLinkedList.head
            if self.cutomLinkedList.head == self.cutomLinkedList.tail:
                self.cutomLinkedList.head = None
                self.cutomLinkedList.tail = None
            else:
                self.cutomLinkedList.head = tempNode.next
            # print(tempNode.value, "is dequeued from the Queue")
            return tempNode

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.cutomLinkedList.head.value, "is the first element in Queue")
    
    def delete(self):
        self.cutomLinkedList.head = None
        self.cutomLinkedList.tail = None


if __name__ == '__main__':
    customQueue = Queue()
    customQueue.enqueue(1)
    customQueue.enqueue(2)
    customQueue.enqueue(3)
    print(customQueue)
    customQueue.dequeue()
    print(customQueue)
    customQueue.peek()
