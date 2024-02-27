import time
import random
import matplotlib.pyplot as plt


def partition(arr, l, h):
    i = l - 1
    x = arr[h]
    for j in range(l, h):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quick_sort(arr, l, h):
    size = h - l + 1
    stack = [0] * size
    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        p = partition(arr, l, h)
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
    return arr


def merge(arr: list, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr: list, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def heapify(arr: list, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)


def heap_sort(arr: list):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)


def insertion_sort(arr: list):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


number_array = [_ for _ in range(1000, 10001, 1000)]
merge_time = []
quick_time = []
heap_time = []
insertion_time = []
for i in number_array:
    array = [random.randint(100, 100000) for _ in range(i)]

    start_time = time.time()*1000
    merge_sort(array.copy(), 0, len(array.copy())-1)
    ellapsed_time = time.time()*1000-start_time
    merge_time.append(ellapsed_time)

    start_time = time.time()*1000
    quick_sort(array.copy(), 0, len(array.copy())-1)
    ellapsed_time = time.time()*1000 - start_time
    quick_time.append(ellapsed_time)

    start_time = time.time()*1000
    heap_sort(array.copy())
    ellapsed_time = time.time()*1000 - start_time
    heap_time.append(ellapsed_time)

    start_time = time.time()*1000
    insertion_sort(array.copy())
    ellapsed_time = time.time()*1000 - start_time
    insertion_time.append(ellapsed_time)

plt.plot(number_array, merge_time, label='Merge Sort', color='orange', marker='o')
plt.plot(number_array, quick_time, label='Quick Sort', color='yellow', marker='o')
plt.plot(number_array, heap_time, label='Heap Sort', color='green', marker='o')
plt.plot(number_array, insertion_time, label='Insertion Sort', color='blue', marker='o')
plt.title("Sorting algorithms comparison")
plt.xlabel("Input size")
plt.ylabel("Time (ms)")
plt.legend()
plt.show()

