from TreeNode import *
from traverse import nonRecursiveTraverse
from collections import deque

class BinaryTree:
  def createTree(self):
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    # 连接节点
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    return node1

  def preorderTraverse(self, root):
    def process(root): # 内部函数可以访问外部函数中的变量
      if not root:
        return
      preorderTraverseList.append(root.val)
      process(root.left)
      process(root.right)
    preorderTraverseList = []
    process(root)
    return preorderTraverseList
  
  def inorderTraverse(self, root):
    def process(root):
      if not root:
        return
      process(root.left)
      inorderTraverseList.append(root.val)
      process(root.right)
    inorderTraverseList = []
    process(root)
    return inorderTraverseList

  def postorderTraverse(self, root):
    def process(root):
      if not root:
        return
      process(root.left)
      process(root.right)
      postorderTraverseList.append(root.val)
    postorderTraverseList = []
    process(root)
    return postorderTraverseList

  def levelorderTraversal(self, root):
    levelorderList = []
    if not root:
      return levelorderList
    dequeList = deque()
    dequeList.append(root)
    while dequeList:
      cur = dequeList.popleft()
      levelorderList.append(cur.val)
      if cur.left:
        dequeList.append(cur.left)
      if cur.right:
        dequeList.append(cur.right)
    return levelorderList

  def levelorderTraversal2(self, root):
    levelorderList = []
    if not root:
      return levelorderList
    dequeList = deque()
    dequeList.append(root)
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


tree = BinaryTree()
root = tree.createTree()
preorderTraverseList = tree.preorderTraverse(root)
inorderTraverseList = tree.inorderTraverse(root)
postorderTraverseList = tree.postorderTraverse(root)
levelorderList = tree.levelorderTraversal(root)
levelorderListArray = tree.levelorderTraversal2(root)

nonRecursiveTree = nonRecursiveTraverse(root)
preorderList = nonRecursiveTree.preorder()
postorderList = nonRecursiveTree.postorder()
inorderList = nonRecursiveTree.inorder()
print(preorderList)
print(preorderTraverseList)
print(inorderList)
print(inorderTraverseList)
print(postorderTraverseList)
print(postorderList)
print(levelorderList)
print(levelorderListArray)