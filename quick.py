#Quick Sort

def quicksort(arr):
  if len(arr) < 1:
    return arr
  else: 
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quicksort(less) +[pivot] + quicksort(greater)

print(quicksort([10, 1, 23, 5, 7,  12, 17, 19]))




