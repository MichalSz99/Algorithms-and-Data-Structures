import random


def quick_sort(arr):
    quick_sort_main(arr, 0, len(arr)-1)
    return arr


def quick_sort_main(arr, l, r):
    if l < r:
        pivot = partition(arr, l, r)
        quick_sort_main(arr, l, pivot-1)
        quick_sort_main(arr, pivot+1, r)


def partition(arr, l, r):
    x = random.randint(l, r)
    pivot = arr[x]
    arr[r], arr[x] = arr[x], arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


array = [1, 4, 6, 7, -60, 36, 346, 3, 57, 34, -503, 37, 1]
print(quick_sort(array))
