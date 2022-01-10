class Queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        return " ".join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.list.append(value)
        print(value, "is enqueued at the end of the Queue")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.list.pop(0), "is dequeued from the Queue")

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.list[0], "is the first element in Queue")
    
    def delete(self):
        self.list = None


customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
customQueue.enqueue(5)
print(customQueue.isEmpty())
print(customQueue)
customQueue.dequeue()
print(customQueue)
customQueue.peek()
customQueue.delete()
try:
    print(customQueue)
except:
    print("There is not any Queue or had been deleted!")
