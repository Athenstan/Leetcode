def smallest_subarray_with_given_sum(s, arr):
  # TODO: Write your code here
  # Steps:
  # insert 2 into windowsum = 2, windowsize =1, windowstart remains 0, maxsize = 10000.  
  # insert 1 into windowsum = 3, window size = 2, windowstart remains 0, maxsize = 10000
  # insert 5 into window sum = 8, window size = 3, windowstart remains 0, max size = 10000 
  # while loop initiated. window sum is 6, window size = 3, window start is 1, max size updated to 3. 
  # insert 2 into window sum = 8, window size is 3, window start remains 1, max size is 3 
  # while loop is initiated. windowsum = 8, window size = 3, window start 2, max size is 3
  # while loop is initiated. windowsum = 7, window size = 2, window start 2, max size is 2
  # 
  #
  windowsum, minsize, windowstart,windowsize = 0,10000,0,0; 
  for windowend in range(len(arr)):
    windowsum += arr[windowend]
    windowsize += 1; 
    while windowsum >= s:
      windowsum -= arr[windowstart]
      windowstart +=1
      minsize = min(minsize, windowsize)
      windowsize -= 1
    
  
  return minsize 
