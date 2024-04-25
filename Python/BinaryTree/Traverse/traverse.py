
from collections import deque
from baseClass import BinaryTree
class Traverse(BinaryTree):
  def __init__(self):
    super().__init__()
  
  def preorderTraverse(self):
    def process(root):
      if not root:
        return
      preorderTraverseList.append(root.val)
      process(root.left)
      process(root.right)
    preorderTraverseList = []
    process(self.root)
    return preorderTraverseList
  
  def inorderTraverse(self):
    def process(root):
      if not root:
        return
      process(root.left)
      inorderTraverseList.append(root.val)
      process(root.right)
    inorderTraverseList = []
    process(self.root)
    return inorderTraverseList

  def postorderTraverse(self):
    def process(root):
      if not root:
        return
      process(root.left)
      process(root.right)
      postorderTraverseList.append(root.val)
    postorderTraverseList = []
    process(self.root)
    return postorderTraverseList

  def levelorderTraversal(self):
    levelorderList = []
    if not self.root:
      return levelorderList
    dequeList = deque()
    dequeList.append(self.root)
    while dequeList:
      cur = dequeList.popleft()
      levelorderList.append(cur.val)
      if cur.left:
        dequeList.append(cur.left)
      if cur.right:
        dequeList.append(cur.right)
    return levelorderList

  def levelorderTraversal2(self):
    levelorderList = []
    if not self.root:
      return levelorderList
    dequeList = deque()
    dequeList.append(self.root)
    while dequeList:
      size = len(dequeList)
      levelNode = []
      for i in range(size):
        cur = dequeList.popleft()
        levelNode.append(cur.val)
        if cur.left:
          dequeList.append(cur.left)
        if cur.right:
          dequeList.append(cur.right)
      levelorderList.append(levelNode)
    return levelorderList

  def getWidthTree(self):
    if not self.root:
      return 0
    q = deque()
    nodeMap = {}
    q.append(self.root)
    nodeMap[self.root] = 1
    res = 0
    curNodeLevel = 1
    LevelNodesNum = 0
    while q:
      cur = q.popleft()
      if curNodeLevel != nodeMap[cur]:
        res = max(res, LevelNodesNum)
        LevelNodesNum = 1
        curNodeLevel += 1
      else:
        LevelNodesNum += 1
      if cur.left:
        q.append(cur.left)
        nodeMap[cur.left] = curNodeLevel+1
      if cur.right:
        q.append(cur.right)
        nodeMap[cur.right] = curNodeLevel+1
    return res


  def getNodesNum(self, root):
    if not root:
      return 0
    return self.getNodesNum(root.left) + self.getNodesNum(root.right) + 1

  def getAllLeafs(self):
    pass

  def getDepthTree(self, root):
    if not root:
      return 0
    return max(self.getDepthTree(root.left), self.getDepthTree(root.right)) + 1

  def nonRecursivePreorder(self):
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
  
  def nonRecursiveInorder(self):
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

  def nonRecursivePostorder(self):
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

