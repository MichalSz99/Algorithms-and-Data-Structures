import random


class Stacks:
    def __init__(self):
        self.tab = []

    def push(self, a, b):
        self.tab.append((a, b))

    def pop(self):
        pom = self.tab.pop(-1)
        return pom

    def empty(self):
        if len(self.tab) > 0:
            return False
        else:
            return True


def quick_sort(arr):
    stack = Stacks()
    stack.push(0, len(arr)-1)
    while not stack.empty():
        l, r = stack.pop()
        if l < r:
            x = random.randint(l, r)
            pivot = arr[x]
            arr[r], arr[x] = arr[x], arr[r]
            i = l
            for j in range(l, r):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i], arr[r] = arr[r], arr[i]
            stack.push(l, i-1)
            stack.push(i+1, r)
    return arr


array = [1, 4, 6, 7, 36, 346, 3, 57, 34, -503, 37, 3, 1, 4, 6]
print(quick_sort(array))
