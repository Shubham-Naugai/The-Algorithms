# Using python list

class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)


CustomTree = TreeNode("Drinks", [])

hot = TreeNode("hot", [])
cold = TreeNode("cold", [])

CustomTree.addChild(cold)
CustomTree.addChild(hot)

tea = TreeNode("tea", [])
coffee = TreeNode("coffee", [])
hot.addChild(tea)
hot.addChild(coffee)

cola = TreeNode("cola", [])
fanta = TreeNode("fanta", [])
soda = TreeNode("soda", [])
cold.addChild(cola)
cold.addChild(fanta)
cold.addChild(soda)

print(CustomTree)



