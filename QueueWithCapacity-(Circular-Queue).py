class circularQueue:
    def __init__(self, maxSize):
        self.list = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.list]
        return " ".join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            print("The Queue is Full")
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.list[self.top] = value
            print(value, "is enqueued at the end of the Queue")

    def dequeue(self):
        if self.isEmpty():
            print("The Queue is empty")
        else:
            firstElement = self.list[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.list[start] = None
            print(firstElement, "is dequeued from the Queue")
    
    def peek(self):
        if self.isEmpty():
            print("The Queue is empty")
        else:
            print(self.list[self.start], "is the first element in Queue")

    def delete(self):
        self.list = self.maxSize * [None]
        self.start = -1
        self.top = -1


customCircularQueue = circularQueue(5)
customCircularQueue.enqueue(1)
customCircularQueue.enqueue(2)
customCircularQueue.enqueue(3)
customCircularQueue.enqueue(4)
customCircularQueue.enqueue(5)
print(customCircularQueue)
customCircularQueue.dequeue()
print(customCircularQueue)
customCircularQueue.dequeue()
print(customCircularQueue)
customCircularQueue.peek()
customCircularQueue.enqueue(6)
print(customCircularQueue)
customCircularQueue.peek()
customCircularQueue.delete()
print(customCircularQueue)
