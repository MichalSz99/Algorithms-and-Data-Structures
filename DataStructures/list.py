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
            new_node = Node(val)
            new_node.next = self
            return newNode
        else:
            new_node = Node(val)
            current_node = self
            next_node = self.next
            while not(next_node is None) and next_node.val < val:
                current_node = next_node
                next_node = next_node.next
            new_node.next = next_node
            current_node.next = new_node
            return self

    def search(self, val):
        current_node = self
        while val > current_node.val and not(current_node.next is None):
            current_node = current_node.next
        if val == current_node.val:
            return current_node
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


list = Node()
with open("data.txt") as input:
    data = input.read().splitlines()
for x in data:
        list = list.insert(int(x))
print("Length of BST: " + str(list.length()))
print("The biggest element: " + str(list.max()))
print("Next value after 21 is " + str(list.search(21).next.val))
list.show()
del list
