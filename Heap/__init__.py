class Node:
    def __init__(self, num, key, parent):
        self.num = num
        self.key = key
        self.parent = parent
    def display(self):
         print([self.num, self.key, self.parent])
def minHeapify(arr, i, heap_size):
    l = 2 * i + 1
    r = 2 * i + 2
    smallest = i

    if l < heap_size and (arr[l]).key < arr[smallest].key:
        smallest = l

    if r < heap_size and (arr[r]).key < arr[smallest].key:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minHeapify(arr, smallest, heap_size)

def buildMinHeap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        minHeapify(arr, i, n)

def heaport(arr):
    buildMinHeap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        minHeapify(arr, 0, i)

def delete_min(arr):
    x = arr[len(arr)-1]
    arr.pop()
    return x
def delete (arr, num):
    new = []
    for i in range (len(arr)):
        if arr[i].num != num:
            new.append(arr[i])
    return new
def disall (arr):
    for i in range(len(arr)):
        Node.display(arr[i])
