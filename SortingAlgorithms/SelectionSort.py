def selection_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        max_index = i
        for j in range(i, -1, -1):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[max_index], arr[i] = arr[i], arr[max_index]
    return arr


array = [1, 4, 6, 4, 7, 36, 346, 3, 57, 34, -501, 37]
print(selection_sort(array))
 
