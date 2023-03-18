from HeapSort import HeapSort

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, ]
    app = HeapSort()
    app.heap_sort(arr)
    n = len(arr)
    print('Sorted array is')
    for i in range(n):
        print(arr[i], end=' ')
