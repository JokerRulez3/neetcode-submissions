# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = [root.val]

        if self._is_leaf(root):
            return result
        
        self._add_left_boundary(root.left,result)
        self._add_leaves(root.left, result)
        self._add_leaves(root.right, result)
        self._add_right_boundary(root.right,result)

        return result
    
    def _is_leaf(self, node):
        return node.left is None and node.right is None
    
    def _add_left_boundary(self, node, result):
        while node and not self._is_leaf(node):
            result.append(node.val)
            node = node.left if node.left else node.right
    
    def _add_right_boundary(self, node, result):
        stack: List[int] = []
        while node and not self._is_leaf(node):
            stack.append(node.val)
            node = node.right if node.right else node.left
        
        result.extend(reversed(stack))

    def _add_leaves(self, node, result):
        if node is None:
            return
        if self._is_leaf(node):
            result.append(node.val)
            return
        self._add_leaves(node.left,result)
        self._add_leaves(node.right, result)
        