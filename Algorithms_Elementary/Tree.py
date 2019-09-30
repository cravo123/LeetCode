class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Tree traversal
# We use L, N, R to represent Left Child Node, Root Node, and Right Child Node. 
# And visited order is shown by order in the resulted list.
# There are 3 different traversal orders, all of which are distinguished by when Root Node is visited.
# For recursion methods, it is trivial to see that the traversal order is determined by which order
# each recursion function is called.
# Speaking of relationship between tree traversal and BFS(Breadth-First-Search), DFS(Depth-First-Search)
# Tree is a special case of graph, so 
# Pre-oder, In-order and Post-order are DFS,
# Level-traversal is BFS

# 1.1 Pre-order Traversal, N -> L -> R
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

# 1.2 In-order Traversal, L ->N -> R
def inorder_recursion(root):
    res = []
    inorder_recursion_helper(root, res)

    return res

def inorder_recursion_helper(node, res):
    if node is None:
        return

    inorder_recursion_helper(node.left, res)
    res.append(node.val)
    inorder_recursion_helper(node.right, res)

# 1.3 Post-order Traversal, L ->R ->N
def postorder_recursion(root):
    res = []
    postorder_recursion_helper(root, res)

    return res

def postorder_recursion_helper(node, res):
    if node is None:
        return

    postorder_recursion_helper(node.left, res)
    postorder_recursion_helper(node.right, res)
    res.append(node.val)

# 1.4 Level Traversal, traverse tree level by level
# Like Breadth-First-Search
def level_traversal_iteration(root):
    res = []

    if root is None:
        return res
    
    q = [root]

    while q:
        res.extend([p.val for p in q])
        q = [x for p in q for x in [p.left, p.right] if x]
    
    return res

# Level traversal iteration
# TODO: