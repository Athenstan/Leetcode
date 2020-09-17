# Question: Educative 2 Pointer 1st question 

# Attempts:2 
# Completed: Y
# Optimal: Kinda

# Time: O(N)
# Space:O(1)

def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
  # in this problem, the inputs are numbers and the output is an array with 2 indexes. 
  # We have a target, and the indexes of the two numbers must give us numbers that add to the specific target. 
  # If i have the target and I am on one of the numbers on the array. 
  for i in arr: 
    neededNum = target_sum - arr[i] 
    if neededNum in arr: 
      return [i, arr.index(neededNum)]; 
  return [-1, -1]

# Problems Encountered: Well did not think of using the hashtable for quicker lookup times 

# Other Solutions:

def pair_with_targetsum(arr, target_sum):
  nums = {}  # to store numbers and their indices
  for i, num in enumerate(arr):
    if target_sum - num in nums:
      return [nums[target_sum - num], i]
    else:
      nums[arr[i]] = i
  return [-1, -1]


# using the hashtable to ensure faster lookups for the items in the list instead of iterating through the list. 


#Notes: Enumerating through an array in python sets a index for each item that can then be referenced later. 