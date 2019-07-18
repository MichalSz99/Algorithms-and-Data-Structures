def merge_sort(arr):
    temp = [0] * len(arr)
    arr = merge_sort_in(arr, temp, 0, len(arr) - 1)
    return arr


def merge(arr, temp, first, med, last):
    i = first
    j = med + 1
    for k in range(first, last + 1):
        if ((i <= med) and (j > last)) or (((i <= med) and (j <= last)) and (arr[i] <= arr[j])):
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
    for k in range(first, last + 1):
        arr[k] = temp[k]
    return arr


def merge_sort_in(arr, temp, first, last):
    med = (first + last) // 2
    if (med - first) > 0:
        merge_sort_in(arr, temp, first, med)
    if (last - med) > 0:
        merge_sort_in(arr, temp, med + 1, last)
    merge(arr, temp, first, med, last)
    return arr


array = [1, 4, 6, 4, 7, 36, 346, 3, 57, 34, -50, 37]
print(merge_sort(array))
