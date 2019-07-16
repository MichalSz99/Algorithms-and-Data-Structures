class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val

    def __del__(self):
        if not (self.next is None):
            del self.next
        print("Delete " + str(self.val));

    def insert(self, val):
        if self.val is None:
            self.val = val
            return self
        elif self.val > val:
            newNode = Node(val)
            newNode.next = self
            return newNode
        else:
            newNode = Node(val)
            currentNode = self
            nextNode = self.next
            while not(nextNode is None) and nextNode.val < val:
                currentNode = nextNode
                nextNode = nextNode.next
            newNode.next = nextNode
            currentNode.next = newNode
            return self

    def search(self, val):
        currentNode = self
        while val > currentNode.val and not(currentNode.next is None):
            currentNode = currentNode.next
        if val == currentNode.val:
            return currentNode
        else:
            return None

    def show(self):
        print(self.val)
        if not (self.next is None):
            self.next.show()

    def length(self):
        if self.next is None:
            return 1
        else:
            return self.next.length() + 1

    def max(self):
        if not (self.next is None):
            return self.next.max()
        return self.val


List = Node()
with open("data.txt") as input:
    data = input.read().splitlines()
for x in data:
        List = List.insert(int(x))
print("Length of BST: " + str(List.length()))
print("The biggest element: " + str(List.max()))
print("Next value after 21 is " + str(List.search(21).next.val))
List.show()
del List
