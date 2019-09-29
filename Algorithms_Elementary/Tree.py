class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Tree traversal
# We use L, N, R to represent Left Child Node, Root Node, and Right Child Node. 
# And visited order is shown by order in the resulted list.
# There are 3 different traversal orders, all of which are distinguished by when Root Node is visited.
# 1.1 pre-order Traversal, N -> L -> R
def preorder_recursion_helper(node, res):
    if node is None:
        return

    res.append(node.val)
    preorder_recursion_helper(node.left, res)
    preorder_recursion_helper(node.right, res)
    
def preorder_recursion(root):
    res = []
    
    preorder_recursion_helper(root, res)
    
    return res

def preorder_iteration(root):
    res = []
    
    q = []
    if root:
        q.append(root)

    while q:
        p = q.pop()
        res.append(p.val)
        
        if p.right:
            q.append(p.right)
        if p.left:
            q.append(p.left)
    
    return res
    
    