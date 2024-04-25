from baseClass import TreeNode
# 根据先序遍历以及中序遍历,构造一棵树
# 先序[1, 2, 4, 5, 3]
# 中序[4, 2, 5, 1, 3]
# 先序中的第一个数字就是根节点
# 根据先序中的根节点,查找它在中序中的位置,确定左子树以及右子树
# 递归实现这个过程
def run(preorder, inorder):
  if len(preorder) != len(inorder):
    return None
  if len(preorder) == 0 or len(inorder) == 0:
    return None
  node = TreeNode(preorder[0])
  in_index = inorder.index(preorder[0])
  node.left = run(preorder[1:in_index+1], inorder[:in_index])
  node.right = run(preorder[in_index+1:], inorder[in_index+1:])
  return node

# 根据中序与后序,构造一棵树
# 中序[4, 2, 5, 1, 3]
# 后序[4, 5, 2, 3, 1]
# 根节点在后续遍历中一定是最后一个,再根据中序确定左右子树
# 递归实现这个过程
def buildTree(inorder, postorder):
  if len(inorder) != len(postorder):
    return None
  if len(inorder) == 0 or len(postorder) == 0:
    return None
  root = TreeNode(postorder[-1])
  in_index = inorder.index(postorder[-1])
  root.left = buildTree(inorder[:in_index], postorder[:in_index])
  root.right = buildTree(inorder[in_index+1:], postorder[in_index:-1])
  return root

  

  






