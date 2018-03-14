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