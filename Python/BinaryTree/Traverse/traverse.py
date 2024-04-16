
class nonRecursiveTraverse:
  def __init__(self, root):
    self.root = root

  def preorder(self):
    stack = []
    preorderList = []
    if not self.root:
      return
    stack.append(self.root)
    while len(stack):
      cur = stack.pop()
      preorderList.append(cur.val)
      if cur.right:
        stack.append(cur.right)
      if cur.left:
        stack.append(cur.left)
    return preorderList
  
  def inorder(self):
    stack = []
    inorderList = []
    if not self.root:
      return
    cur = self.root
    while True:
      while cur:
        stack.append(cur)
        cur = cur.left

      if len(stack):
        cur = stack.pop()
        inorderList.append(cur.val)
        cur = cur.right
      else:
        break
    return inorderList

  def postorder(self):
    stack1 = []
    stack2 = []
    postList = []
    if not self.root:
      return
    stack1.append(self.root)
    while len(stack1):
      cur = stack1.pop()
      stack2.append(cur)

      if cur.left:
        stack1.append(cur.left)
      if cur.right:
        stack1.append(cur.right)

    while len(stack2):
      postList.append(stack2.pop().val)
    return postList

