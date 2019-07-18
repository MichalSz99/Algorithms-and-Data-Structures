def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


array = [1, 4, 6, 4, 7, 36, 346, 3, 57, 34, -50, 37]
print(insert_sort(array))
 
