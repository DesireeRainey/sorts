

#Python Merge Sort
import time 
import random 

def merge(arr1, arr2):
  results = []
  
  while len(arr1) > 0 and len(arr2) > 0:
    if arr1[0] > arr2[0]:
      results.append(arr2.pop(0))
    else: 
      results.append(arr1.pop(0))
  return results + arr1 + arr2

def merge_sort(arr):
  #base case: array length is less than or equal to one
  #recursive case: any other array length stored in the else
  if len(arr) <= 1:
    return arr #This states that the array is sorted
  else: 
    # Find the middle index of the array. (needs to be an integer)
    middle_index = len(arr) // 2
    #dividing the array in half between the left side and the right side
    left = arr[:middle_index]
    right = arr[middle_index:]
    
    #Recurse on the shorter lists
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    #Now that I have sorted lists, merge them
    return merge(left_sorted, right_sorted)
  
#test data for merge sorted
random_arr = [1, 2, 4, 5, 6, 3, 77, 5]
sorted_arr = merge_sort(random_arr)  
print("Result: ", sorted_arr)

my_arr = []
for i in range(0, 100000)):
  my_arr.append(random.randint(0, 100000))

#time
start_time = time.time()
sorted_arr = merge_sort(my_arr)

print(time.time() - start_time, ' seconds')
  
#Test data for merge function
# my_arr1 = [2, 3, 5]
# my_arr2 = [1, 1, 2, 6]

# print(merge(my_arr1, my_arr2))







