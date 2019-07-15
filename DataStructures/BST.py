class Tree:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is None:
            self.val = val
        elif self.val > val:
            if self.left is None:
                self.left = Tree(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = Tree(val)
            else:
                self.right.insert(val)

    def search(self, val):
        if val == self.val:
            return self
        elif val < self.val and not(self.left is None):
            return self.left.search(val)
        elif val > self.val and not(self.left is None):
            return self.right.search(val)
        else:
            return None

    def preorder(self):
        print(self.val)
        if not (self.left is None):
            self.left.preorder()
        if not (self.right is None):
            self.right.preorder()

    def inorder(self):
        if not (self.left is None):
            self.left.inorder()
        print(self.val)
        if not (self.right is None):
            self.right.inorder()

    def postorder(self):
        if not (self.left is None):
            self.left.postorder()
        if not (self.right is None):
            self.right.postorder()
        print(self.val)


    def height(self):
        if self.left is None:
            maxL = 0
        else:
            maxL = self.left.height()
        if self.right is None:
            maxR = 0
        else:
            maxR = self.right.height()
        return max(maxL, maxR)+1

    def search(self, x):
        if x == self.val:
            return self
        elif x > self.val:
            return self.right.search(x)
        else:
            return self.left.search(x)

    def max(self):
        if not (self.right is None):
            return self.right.max()
        return self.val

    def deleteTree(self):
        if not (self.left is None):
            self.left.deleteTree()
        if not (self.right is None):
            self.right.deleteTree()
        del self
        return None

BST = Tree()
with open("data.txt") as input:
    data = input.read().splitlines()
for x in data:
        BST.insert(int(x))
print("Height of BST: " + str(BST.height()))
print("The biggest element: " + str(BST.max()))
print("Preorder: ")
BST.preorder()
print("Inorder: ")
BST.inorder()
print("Postorder: ")
BST.postorder()
print("Right child of 17 is " + str(BST.search(17).right.val))
BST.deleteTree()
