def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    print ("Sorted array"),
    print_array(arr)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    

def print_array(arr):
    for i in range(len(arr)):
        print("%d" %arr[i]),

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j= i-1
        key = arr[i]
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i=j=k=0
    
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while i< len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j< len(R):
            arr[k] = R[j]
            j+=1
            k+=1

def quick_sort(arr, low, high):
    if(low < high):
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    i= (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i + 1)

if __name__=='__main__':
    arr = [64, 25, 12, 22, 11]
    print ("****** Selection Sort *******")
    print ("UnSorted array"),
    print_array(arr)
    selection_sort(arr)
    print ("Sorted array"),
    print_array(arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    print ("****** Bubble Sort *******")
    print ("UnSorted array"),
    print_array(arr)
    bubble_sort(arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    print ("****** Insertion Sort *******")
    print ("UnSorted array"),
    print_array(arr)
    insertion_sort(arr)
    print ("Sorted array"),
    print_array(arr)

    arr = [12, 11, 13, 5, 6, 7]
    print ("****** Merge Sort *******")
    print ("UnSorted array"),
    print_array(arr)
    merge_sort(arr)
    print ("Sorted array"),
    print_array(arr)

    arr = [10, 7, 8, 9, 1, 5]#[10, 80, 30, 90, 40, 50, 70]
    print ("****** Quick Sort *******")
    print ("UnSorted array"),
    print_array(arr)
    quick_sort(arr, 0, (len(arr) -1))
    print ("Sorted array"),
    print_array(arr)
