import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


BinaryTree = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
# cola = TreeNode("Cola")
# fanta = TreeNode("Fanta")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")

BinaryTree.leftChild = leftChild
BinaryTree.rightChild = rightChild

leftChild.leftChild = tea
leftChild.rightChild = coffee
# rightChild.leftChild = cola
# rightChild.rightChild = fanta


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

print("1: PreOrderTraversal method to traverse a tree")
preOrderTraversal(BinaryTree)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

print("\n2: InOrderTraversal method to traverse a tree")
inOrderTraversal(BinaryTree)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

print("\n3: PostOrderTraversal method to traverse a tree")
postOrderTraversal(BinaryTree)

# level order traversal by importing QueueLinkedList.py module
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

print("\n4a: LevelOrderTraversal method to traverse a tree")
levelOrderTraversal(BinaryTree)

# level order traversal by using queue functionality
def newlevelOrderTraversal(rootNode):
    if not rootNode:
        return
    Queue = []
    Queue.append(rootNode)
    while len(Queue) > 0:
        # print(Queue[0].data)
        root = Queue.pop(0)
        print(root.data)
        
        # Enqueue left child
        if root.leftChild:
            Queue.append(root.leftChild)
        
        # Enqueue right child
        if root.rightChild:
            Queue.append(root.rightChild)

print("\n4b: LevelOrderTraversal method to traverse a tree(queue functionality)")
newlevelOrderTraversal(BinaryTree)

def searchInBinaryTree(rootNode, nodeValue):
    if not rootNode:
        return "Binary Tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        print("Finding...")
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Node found"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Node not Found"
print("\nSearching in Binary Tree using levelordertraversal method")
print(searchInBinaryTree(BinaryTree, "Cola"))


def newsearchInBinaryTree(rootNode, Nodevalue):
    if not rootNode:
        return "Binary Tree doesn't exist"
    else:
        Queue = []
        Queue.append(rootNode)
        while len(Queue) > 0:
            # print(Queue[0].data)
            root = Queue.pop(0)
            if root.data == Nodevalue:
                return "Node Found"
            # Enqueue left child
            if root.leftChild:
                Queue.append(root.leftChild)
            # Enqueue right child
            if root.rightChild:
                Queue.append(root.rightChild)
        return "Node not found"
print("\nSearching in Binary Tree using levelordertraversal method")
print(newsearchInBinaryTree(BinaryTree, "Cold"))


def insertNodeToTree(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                print(newNode.data, "inserted as a left child of", root.value.data)
                return
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                print(newNode.data, "inserted as a right child of", root.value.data)
                return
# print("\nInserting a node in Binary Tree")
# cola = TreeNode("Cola")
# fanta = TreeNode("Fanta")
# insertNodeToTree(BinaryTree, cola)
# insertNodeToTree(BinaryTree, fanta)

def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        Queue = []
        Queue.append(rootNode)
        while len(Queue) > 0:
            root = Queue.pop(0)
            if root.leftChild is not None:
                Queue.append(root.leftChild)
            else:
                root.leftChild = newNode
                print(newNode.data, "inserted as a left child of", root.data)
                return
            if root.rightChild is not None:
                Queue.append(root.rightChild)
            else:
                root.rightChild = newNode
                print(newNode.data, "inserted as a right child of", root.data)
                return
# print("\nInserting a node in Binary Tree")
# cola = TreeNode("Cola")
# fanta = TreeNode("Fanta")
# insertNode(BinaryTree, cola)
# insertNode(BinaryTree, fanta)



# Deleting a node from tree
print("\nDeleting a node from tree")
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode


# deepestNode = getDeepestNode(BinaryTree)
# print("Step-1: Get Deepest node")
# print(deepestNode.data)

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

# print("Step-2: Delete the deepest Node", deepestNode.data)
# deleteDeepestNode(BinaryTree, deepestNode)
# levelOrderTraversal(BinaryTree)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "Binary Tree Does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node successfully deleted"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete"

print(deleteNodeBT(BinaryTree, "Hot"))
levelOrderTraversal(BinaryTree)

def deleteBinaryTree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    print("Tree Successfully deleted")

deleteBinaryTree(BinaryTree)
levelOrderTraversal(BinaryTree)
