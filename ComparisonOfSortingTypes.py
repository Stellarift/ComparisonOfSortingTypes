import random
import time

def bubble_sort(arr):
    arr = arr.copy()
    swaps = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps

def selection_sort(arr):
    arr = arr.copy()
    swaps = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return swaps

def insertion_sort(arr):
    arr = arr.copy()
    swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        arr[j + 1] = key
    return swaps

def quick_sort(arr):
    arr = arr.copy()
    swaps = [0]
    def sort(low, high):
        if low < high:
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps[0] += 1
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            swaps[0] += 1
            sort(low, i)
            sort(i + 2, high)
    sort(0, len(arr) - 1)
    return swaps[0]

def merge_sort(arr):
    arr = arr.copy()
    swaps = [0]
    def sort(low, high):
        if low < high:
            mid = (low + high) // 2
            sort(low, mid)
            sort(mid + 1, high)
            left = arr[low:mid + 1]
            right = arr[mid + 1:high + 1]
            i = j = 0
            k = low
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                swaps[0] += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
                swaps[0] += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
                swaps[0] += 1
    sort(0, len(arr) - 1)
    return swaps[0]

def shaker_sort(arr):
    arr = arr.copy()
    swaps = 0
    left, right = 0, len(arr) - 1
    while left <= right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
        right -= 1
        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swaps += 1
        left += 1
    return swaps

def main():
    sizes = [1000, 10000, 100000]
    algorithms = [
        ("Bubble sort", bubble_sort),
        ("Selection sort", selection_sort), 
        ("Insertion sort", insertion_sort),
        ("Quick sort", quick_sort),
        ("Merge sort", merge_sort),
        ("Shaker sort", shaker_sort)
    ]
    
    print("Сравнение алгоритмов сортировки")
    
    for size in sizes:
        print(f"\nРазмер массива: {size}")
        test_data = [random.randint(1, 100000) for _ in range(size)]
        
        for name, algorithm in algorithms:
            best_time = float('inf')
            
            for _ in range(5):
                start_time = time.time()
                algorithm(test_data)
                time_taken = (time.time() - start_time) * 1000
                
                if time_taken < best_time:
                    best_time = time_taken
            
            print(f"{name}: {best_time:.1f} ms")

if __name__ == "__main__":
    main()