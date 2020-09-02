class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  # TODO: Write your code here
  queue = []
  queue.append(root)
  levelcounter = 0

  while queue: 
    levelsize = len(queue)
    levelcounter +=1
    for u in range(levelsize): 
      currentnode = queue.pop(0)
      if not currentnode.left and not currentnode.right: 
        return levelcounter 
      if currentnode.left: 
        queue.append(currentnode.left)
      if currentnode.right: 
        queue.append(currentnode.right)
   

  return -1


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()

