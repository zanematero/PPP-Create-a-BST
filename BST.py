# Part 1: Create a BSTNode class
class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

# Part 2: Create a BST class
class BST:
    def __init__(self, root=None):
        self.root = root
        self.contents = set()

    def __str__(self):
        if self.root == None:
            return "This Binary-Tree is empty."
        
        self.output = ""
        self.print_tree(node=self.root)
        return self.output

    def print_tree(self, node, level=0):
        if node != None:
            self.print_tree(node.right, level + 1)
            self.output += " " * 4 + level + " => " + str(node.data) + " " * 4
        self.print_tree(node.left, level + 1)

    def add(self, data):
        if type(data) not in [int, BSTNode]:
            raise ValueError("Incorrect data type.")

        node = None
        if type(data) == int:
            node = BSTNode(data=10)
        else:
            node = data

        if node.data in self.contents:
            return
        if self.root == None:
            self.root = node

    def add_node(self, current, new):
        if new.data < current.data:
            if current.right == None:
                current.right = new
                self.contents.add(new.data)
                return
            self.add_node(current.right, new)
        else:
            if current.left == None:
                current.left = new
                self.contents.add(new.data)
            self.add_node(current.left, new)
            
    # def __repr__(self):
# Part 3: Add functionality to your BST class





# n1 = BSTNode(3)
# print(n1)

# n2 = BSTNode(4, left=n1)
# print(n2)

# n3 = BSTNode()
# print(n3) #None
# n3.data = 5
# print(n3) #5

#bst = BST()
# print(bst)

# bst.root = n2
# print(bst)

# n2.right = n3
# print(bst)

#bst.add(10)
#bst.add("10")


#create tree from image
node8 = BSTNode(8)
node3 = BSTNode(3)
node10 = BSTNode(10)
node1 = BSTNode(1)
node6 = BSTNode(6)
node14 = BSTNode(14)
node4 = BSTNode(4)
node7 = BSTNode(7)
node13 = BSTNode(13)

bst = BST()
bst.add(node8)
bst.add(node3)
bst.add(node10)
bst.add(node1)
bst.add(node6)
bst.add(node14)
bst.add(node4)
bst.add(node7)
bst.add(node13)

bst.print_tree(node1)