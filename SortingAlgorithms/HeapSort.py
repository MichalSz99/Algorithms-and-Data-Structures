def heap_sort(arr):
    build_heap(arr)
    heap_size = len(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        heapify(arr, 0, heap_size)
    return arr


def build_heap(arr):
    heap_size = len(arr)
    for i in range((len(arr)//2), -1, -1):
        heapify(arr, i, heap_size)


def heapify(arr, i, heap_size):
    left = 2*i+1
    right = 2*i+2
    if(left < heap_size) and (arr[left] > arr[i]):
        largest = left
    else:
        largest = i
    if (right < heap_size) and (arr[right] > arr[largest]):
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, largest, heap_size)


arr = [1, 4, 6, 4, 7, 36, 346, 3, 57, 34, -503, 37]
print(heap_sort(arr))
 
