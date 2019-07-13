import random

def QuickSort(A):
    QuickSortMain(A,0,len(A)-1)
    return A

def QuickSortMain(A, l, r):
    if l < r:
        pivot = Partition(A, l, r)
        QuickSortMain(A, l, pivot-1)
        QuickSortMain(A, pivot+1, r)

def Partition (A, l, r):
    x = random.randint(l,r)
    pivot = A[x]
    A[r], A[x] = A[x], A[r]
    i = l
    for j in range(l,r):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i +=1
    A[i], A[r] = A[r], A[i]
    return i

Tablica = [1, 4, 6, 7,-60, 36, 346, 3, 57, 34, -503, 37,1]
print(QuickSort(Tablica))
