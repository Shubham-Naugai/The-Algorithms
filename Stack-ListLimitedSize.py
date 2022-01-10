# Creating Stack using python list (Limited size)

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty method
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False 
    
    # PUSH method
    def push(self, value):
        if self.isFull():
            print("The stack is full")
        else:
            self.list.append(value)
            print("Element successfully added.")

    # POP method
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the Stack"
        else:
            return self.list.pop()

    # Peek method
    def peek(self):
        if self.list == []:
            return "There is not any element in the Stack"
        else:
            return self.list[len(self.list)-1]

    # delete method
    def delete(self):
        self.list = None


customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
customStack.push(5)
# print(customStack.pop())
# print(customStack.peek())
# customStack.delete()

