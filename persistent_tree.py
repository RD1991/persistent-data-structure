"""
Example 3: Persistent vs Non-Persistent Binary Tree
Demonstrates the difference between a traditional binary tree that modifies nodes in place
and a persistent binary tree that creates new nodes for each modification.
"""

# Non-Persistent (Traditional) Binary Tree
class RegularTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class RegularTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = RegularTreeNode(value)
            return self
        
        def _insert(node):
            if value < node.value:
                if node.left is None:
                    node.left = RegularTreeNode(value)
                else:
                    _insert(node.left)
            else:
                if node.right is None:
                    node.right = RegularTreeNode(value)
                else:
                    _insert(node.right)
        
        _insert(self.root)
        return self
    
    def to_list(self):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.value] + inorder(node.right)
        return inorder(self.root)

# Persistent Binary Tree
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class PersistentTree:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, value):
        def _insert(node):
            if node is None:
                return TreeNode(value)
            
            # Create new nodes instead of modifying existing ones
            if value < node.value:
                return TreeNode(node.value, _insert(node.left), node.right)
            else:
                return TreeNode(node.value, node.left, _insert(node.right))
        
        new_root = _insert(self.root)
        return PersistentTree(new_root)
    
    def to_list(self):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.value] + inorder(node.right)
        return inorder(self.root)

if __name__ == "__main__":
    print("\n=== Binary Tree Implementation Comparison ===")
    
    # Demo with Regular Tree
    print("\nRegular Tree Demo:")
    regular_tree = RegularTree()
    tree_v1 = regular_tree.insert(5)
    tree_v2 = tree_v1.insert(3)
    tree_v3 = tree_v2.insert(7)
    
    print("Original tree:", regular_tree.to_list())  # Will show [3, 5, 7]
    print("Version 1:", tree_v1.to_list())          # Will show [3, 5, 7]
    print("Version 2:", tree_v2.to_list())          # Will show [3, 5, 7]
    print("Version 3:", tree_v3.to_list())          # Will show [3, 5, 7]
    print("All versions modify the same tree!")
    
    # Demo with Persistent Tree
    print("\nPersistent Tree Demo:")
    persistent_tree = PersistentTree()
    p_tree_v1 = persistent_tree.insert(5)
    p_tree_v2 = p_tree_v1.insert(3)
    p_tree_v3 = p_tree_v2.insert(7)
    
    print("Original tree:", persistent_tree.to_list())  # Will show []
    print("Version 1:", p_tree_v1.to_list())          # Will show [5]
    print("Version 2:", p_tree_v2.to_list())          # Will show [3, 5]
    print("Version 3:", p_tree_v3.to_list())          # Will show [3, 5, 7]
    print("Each version maintains its own state!") 