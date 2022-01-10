# Creating Stack using python list

class Stack:
    def __init__(self):
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
        
    # PUSH method
    def push(self, value):
        self.list.append(value)
        return "Element successfully added."

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


customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.pop())
print("----")
print(customStack)
# print(customStack.peek())
# customStack.delete()
