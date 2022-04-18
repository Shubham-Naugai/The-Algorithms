class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value, index=1):
        try:
            if self.customList[index] == None:
                self.customList[index] = value
                print(f"Value({value}) sucessfully inserted as root value")
            elif value <= self.customList[index]:
                if self.customList[index*2] is None:
                    self.customList[index*2] = value
                    print(f"Value({value}) sucessfully inserted as left value of Value({self.customList[index]})")
                else:
                    self.insertNode(value, index*2)
            else:
                if self.customList[index*2 + 1] is None:
                    self.customList[index*2 + 1] = value
                    print(f"Value({value}) sucessfully inserted as right value of Value({self.customList[index]})")
                else:
                    self.insertNode(value, index*2 + 1)
        except Exception as e:
            print(f"{e}: please put the value in proper order(root-left-right) or decrease the number of element(if order already maintained)")
            exit()

    def levelOrderTraversal(self, index=1):
        for i in range(index, self.maxSize-1):
            print(self.customList[i])

newBT = BinaryTree(11)
newBT.insertNode(70)
newBT.insertNode(50)
newBT.insertNode(90)
newBT.insertNode(30)
newBT.insertNode(60)
newBT.insertNode(80)
newBT.insertNode(100)
newBT.insertNode(20)
newBT.insertNode(40)
# newBT.insertNode(40)

newBT.levelOrderTraversal()




