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





