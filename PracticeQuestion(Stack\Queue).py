# 1- Three in one
class Stacks:
    def __init__(self, stackSize):
        self.numOfStacks = 3
        self.customList = [0] * (stackSize * self.numOfStacks)
        self.sizes = [0] * self.numOfStacks
        self.stackSize = stackSize

    def __str__(self):
        numOfStack = len(self.sizes)
        for stacknum in range(numOfStack):
            localStack = self.customList[stacknum*self.stackSize: (stacknum + 1)*self.stackSize]
            localStack.reverse()
            values = [str(x) for x in localStack]
            print("****** stack", stacknum)
            print('\n'.join(values))
        return ""

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stackSize:
            return True
        else:
            return False

    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False

    def indexOfTop(self, stacknum):     
        offset = stacknum * self.stackSize
        return offset + self.sizes[stacknum] - 1

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            print("The stack is Full")
        else:
            self.sizes[stacknum] += 1
            self.customList[self.indexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            print("Stack is empty")
        else:
            value = self.customList[self.indexOfTop(stacknum)]
            self.customList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            print(value, f"is removed from the {stacknum} stack")

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            print("Stack is empty")
        else:
            value = self.customList[self.indexOfTop(stacknum)]
            print(value, f"is the top element of {stacknum} stack")

customStack = Stacks(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(3, 2)
# customStack.push()
# customStack.push()
customStack.peek(2)
print(customStack)


# 2 - Stack min
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        if self.next:
            string += "," + str(self.next)
        return string

class stack:
    def __init__(self):
        self.top = None
        self.minNode = None

    def min(self):
        if self.minNode == None:
            return None
        return self.minNode.value

    def push(self, item):
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value=self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value=item, next=self.minNode)
        self.top = Node(value=item, next=self.top)

    def pop(self):
        if not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item

customStack = stack()
customStack.push(5)
print(customStack.min())
customStack.push(6)
print(customStack.min())
customStack.push(3)
customStack.push(8)
print(customStack.min())
customStack.pop()
print(customStack.min())


# 3 - Stacks of plates
class plateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return str(self.stacks)

    def push(self, item):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) != 0 and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def popAt(self, stackNum):
        if len(self.stacks[stackNum]) > 0:
            return self.stacks[stackNum].pop()
        else:
            return None

customPlateStack = plateStack(3)
customPlateStack.push(1)
customPlateStack.push(3)
customPlateStack.push(4)
customPlateStack.push(6)
customPlateStack.push(7)
print(customPlateStack)
customPlateStack.pop()
print(customPlateStack)


# 4 - Queue via Stack
class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        return str(self.list)

    def __len__(self):
        return len(self.list)

    def push(self, element):
        self.list.append(element)
    
    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()

class QueueViaStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()
    
    def __str__(self):
        return str(self.inStack)

    def enqueue(self, element):
        self.inStack.push(element)
    
    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result

customQueueViaStack = QueueViaStack()
customQueueViaStack.enqueue(1)
customQueueViaStack.enqueue(2)
customQueueViaStack.enqueue(3)
print(customQueueViaStack)
print(customQueueViaStack.dequeue())
print(customQueueViaStack.dequeue())
print(customQueueViaStack)


# 5 - Animal Shelter
import random
class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == "cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueCat(self):
        if self.cats == []:
            print("There is no cat in Animal Shelter")
        else:
            print(self.cats.pop(0))

    def dequeueDog(self):
        if self.dogs == []:
            print("There is no cat in Animal Shelter")
        else:
            offsetcat = self.dogs.pop(0)
            print(offsetcat)

    def dequeueAny(self):
        if self.cats == [] and self.dogs == []:
            print("No animal in the animal shelter")
        elif self.cats == []:
            result = self.dogs.pop(0)
        elif self.dogs == []:
            result = self.cats.pop(0)
        else:
            d = self.dogs.pop(0)
            c = self.cats.pop(0)
            newLst = [c, d]
            result = random.choice(newLst)
            # if result in self.cats:
            #     self.dogs.insert(0, d)
            # else:
            #     self.cats.insert(0, c)
        print(result)

customQueue = AnimalShelter()
customQueue.enqueue("cat1", "cat")
customQueue.enqueue("cat2", "cat")
customQueue.enqueue("cat3", "cat")
customQueue.enqueue("dog1", "dog")
customQueue.enqueue("dog2", "dog")
customQueue.enqueue("dog3", "dog")
customQueue.enqueue("dog4", "dog")
customQueue.dequeueCat()
customQueue.dequeueCat()
customQueue.dequeueCat()
customQueue.dequeueCat()
