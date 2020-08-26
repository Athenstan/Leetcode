class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None
#first try at the problem 
def traverse(root):
  result = []
  if root is None: 
    return result
  # TODO: Write your code here
  queue = deque()
  queue.append(root)
  toggle = True 

  while queue: 
    levelsize = len(queue)
    currentlevel = []

    for _ in range(levelsize):
      currentnode = queue.popleft()
      if toggle: 
        currentlevel.append(currentnode.val)
      else: 
        currentlevel.insert(0,currentnode.val)
      if currentnode.left: 
        queue.append(currentnode.left)
      if currentnode.right:
          queue.append(currentnode.right)
    toggle = not toggle
    result.append(currentlevel)
    
  return result
