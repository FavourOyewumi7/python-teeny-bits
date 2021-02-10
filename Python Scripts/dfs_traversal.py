def dfs_preorder(start, traversal):
    #root-> left->right
    if start:
        traversal += str(start) +'-'
        traversal = dfs_preorder(start.left, traversal)
        traversal = dfs_preorder(start.right, traversal)
    return traversal

def dfs_inorder(start, traversal):
    #left->root->right
    if start:
        traversal = dfs_inorder(start.left, traversal)
        traversal += str(start) + '-'
        traversal = dfs_inorder(start.right, traversal)
    return traversal

def dfs_postorder(start, traversal):
    #left->right->root
    if start:
        traversal = dfs_inorder(start.left, traversal)
        traversal = dfs_inorder(start.right, traversal)
        traversal += str(start) + '-'
    return traversal
       
                         
