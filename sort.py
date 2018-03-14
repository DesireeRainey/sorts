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


# Heap Sort

def heap_sort(list):
  # For ease, let's make a variable for the size of the array
  size = len(list)
  
  # Build inital heap structure
  build_heap(list, size)
  
  # Loop from length down to 2 to heapify
  for i in range(size - 1, 0, -1):
    #swap first and "last"
    list[0], list[i] = list[i], list[0]
    
    # Call heapify on reduced list size
    heapify(list, i, 0)
    
  return list
    
# Convert array/list to a heap  
def build_heap(list, size):
  for i in range(size // 2, -1, -1):
    heapify(list, size, i)

# Make our tree into a max heap
def heapify(sublist, size, root_index):
  largest = root_index
  left = 2*root_index + 1
  right = 2*root_index + 2
  
  if(left < size and sublist[left] > sublist[largest]):
    largest = left
  if(right < size and sublist[right] > sublist[largest]):
    largest = right
  
  if(root_index != largest):
    sublist[largest], sublist[root_index] = sublist[root_index], sublist[largest]
    heapify(sublist, size, largest)


# Test Data
print(heap_sort([8, 2, 1, 4, 6, 5, 7, 3]))


#Bucket Sort / Radix Sort
def radix_sort(arr, max_digits):
    # create buckets
  buckets = create_buckets()
    # set current digit
  current_digit = 1
    # loop thru max_digit number of times 0-max_digit
  for i in range(0,max_digits):
# loop thru 0..max_digits
  for j in range(0,len(arr)):
        # do math to determine bucket, HINT: remember modulus and division
        ## (chop off end) 313 // 10 = 31, (get last number) 31 % 10 == 1
 sig_digit = arr[j] // current_digit
        # assign to bucket // buckets[calculated_num].append(arr[i])
  buckets[sig_digit % 10].append(arr[j])
# switch digit (multiply by 10)
      # flatten array 
  arr = flatten(buckets)  
  # reset buckets to empty
  buckets = create_buckets()
      # set current digit up one place
  current_digit *= 10
    #return arr which will now be sorted
  return arr
    
def create_buckets():
  buckets = []
  for i in range(0,10):
    buckets.append([])
  return buckets
  
def flatten(list_of_lists):
  flattened = []
  for sub_list in list_of_lists:
    flattened.extend(sub_list)
    
  return flattened
  
print(radix_sort([252,1235,332,1237,7523,4432,135,3,6,32], 4))














