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

def QuickSort(A):
    stack = Stacks()
    stack.push(0, len(A)-1)
    while not stack.empty():
        l, r = stack.pop()
        while l < r:
           x = random.randint(l,r)
           pivot = A[x]
           A[r], A[x] = A[x], A[r]
           i = l
           for j in range(l,r):
                if A[j] <= pivot:
                     A[i], A[j] = A[j], A[i]
                     i +=1
           A[i], A[r] = A[r], A[i]
           if i<r:
                stack.push(i, r)
           r = j
    return A

Tablica = [1, 4, 6, 7, 36, 346, 3, 57, 34, -503, 37,3,1,4,6]
print(QuickSort(Tablica))
