import QueueLinkedList as queue

class BinarySearchTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

BST = BinarySearchTreeNode()

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
        print(f"Node({nodeValue}) sucessfully inserted as rootNode")
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BinarySearchTreeNode(nodeValue)
            print(f"Node({nodeValue}) sucessfully inserted as leftChild of Node({rootNode.data})")
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BinarySearchTreeNode(nodeValue)
            print(f"Node({nodeValue}) sucessfully inserted as rightChild of Node({rootNode.data})")
        else:
            insertNode(rootNode.rightChild, nodeValue)

insertNode(BST, 4)
insertNode(BST, 5)
insertNode(BST, 14)
insertNode(BST, 20)
# insertNode(BST, 60)
# insertNode(BST, 80)
# insertNode(BST, 100)
# insertNode(BST, 20)
# insertNode(BST, 40)

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# print("\n1: PreOrderTraversal method to traverse a Binary Search tree")
# preOrderTraversal(BST)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# print("\n2: InOrderTraversal method to traverse a Binary Search tree")
# inOrderTraversal(BST)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# print("\n3: PostOrderTraversal method to traverse a Binary Search tree")
# postOrderTraversal(BST)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

print("\n4: LevelOrderTraversal method to traverse a Binary Search tree")
levelOrderTraversal(BST)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print(f"Node({nodeValue}) is found as rootNode")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print(f"Node({nodeValue}) is found as leftChild of Node({rootNode.data})")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print(f"Node({nodeValue}) is found as rightChild of Node({rootNode.data})")
        else:
            searchNode(rootNode.rightChild, nodeValue)

searchNode(BST, 60)

def successor(BSTNode):
    currentNode = BSTNode
    while (currentNode.leftChild is not None):
        currentNode = currentNode.leftChild
    return currentNode



def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = successor(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode


deleteNode(BST, 50)
levelOrderTraversal(BST)


def deleteBinarySearchTree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    print("Tree Successfully deleted")

deleteBinarySearchTree(BST)



