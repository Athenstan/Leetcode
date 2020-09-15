def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  # need a variable to store the maximum sum 
  maxsum = 0
  #need a for loop to iterate through the array until the end of the window hits the end of the array
  for i in range (len(arr) -k + 1):
  #need a variable to store the window sum 
    windowsum = 0
  #need a for loop to keep track of the window 
    for j in range (i, i+k):
  #add the numbers in the window 
      windowsum += arr[j]
  #need to compare the max sum with window sum 
    maxsum = max(maxsum, windowsum)
  return maxsum 
