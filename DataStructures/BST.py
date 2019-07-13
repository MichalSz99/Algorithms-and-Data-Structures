class Node:

    def __init__(self, val = 0):

        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def search(self, val):
        if val < self.val:
            if self.left is None:
                return 0
            return self.left.search(val)
        elif val > self.val:
            if self.right is None:
                return 0
            return self.right.search(val)
        else:
            return 1
