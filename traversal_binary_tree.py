import queue

class ListNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

tree.left = node1
tree.right = node2
node2.left = node3
node2.right = node4
node3.left = node5
node3.right = node6

def mid_traverse(root):
    if not root:
        return
    print(root.val)
    mid_traverse(root.left)
    mid_traverse(root.right)

def prev_traverse(root):
    if not root:
        return
    prev_traverse(root.left)
    print(root.val)
    prev_traverse(root.right)

def post_traverse(root):
    if not root:
        return
    post_traverse(root.left)
    post_traverse(root.right)
    print(root.val)

def level_order_traverse(root):
    if not root:
        return []
    ans = []
    que = [root]
    while que:
        level_size = len(que)
        level_node = []
        for i in range(level_size):
            node = que.pop(0)
            level_node.append(node.val)

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        ans.append(level_node)
    return ans

# mid_traverse(tree)
# prev_traverse(tree)
# post_traverse(tree)
ans = level_order_traverse(tree)
print(ans)

