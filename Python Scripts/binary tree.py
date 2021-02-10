class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binary_tree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.dfs_preorder(tree.root, "")
        elif traversal_type == "inorder":
            return self.dfs_inorder(tree.root, "")
        elif traversal_type == "postorder":
            return self.dfs_postorder(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False
    def dfs_preorder(self, start, traversal):
    #root-> left->right
        if start:
            traversal += (str(start) +'-')
            traversal = self.dfs_preorder(start.left, traversal)
            traversal = self.dfs_preorder(start.right, traversal)
        return traversal
    def dfs_inorder(self, start, traversal):
    #left->root->right
        if start:
            traversal = self.dfs_inorder(start.left, traversal)
            traversal += (str(start) + '-')
            traversal = self.dfs_inorder(start.right, traversal)
        return traversal
    def dfs_postorder(self, start, traversal):
    #left->right->root
        if start:
            traversal = self.dfs_inorder(start.left, traversal)
            traversal = self.dfs_inorder(start.right, traversal)
            traversal += (str(start) + '-')
        return traversal
    def bfs(self, start, traversal):
        if start is None:
            return
        queue = []
        queue.append(start)
        while queue:
            traversal += str(start)+'-'
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return traversal
                    

tree = binary_tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("postorder"))
#print(tree.print_tree("preorder"))
#print(tree.print_tree("inorder"))
a  =Node(1)
print(a)


