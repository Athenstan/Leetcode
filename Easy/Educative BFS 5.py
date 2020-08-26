class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  result = []
  # TODO: Write your code here
  queue = []
  queue.append(root)

#created while loop for each level 
  while queue: 
    levelsize = len(queue)
    averagecounter = 0.0

# a for loop for iterating within each level and doing what we would like to do 
    for u in range(levelsize):
      currentnode = queue.pop(0)
      averagecounter += currentnode.val 

#Appending children 
      if currentnode.left: 
        queue.append(currentnode.left)
      if currentnode.right: 
        queue.append(currentnode.right)

    result.append(averagecounter/levelsize)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()
