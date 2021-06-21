from typing import Any, Optional, Iterable, List, Tuple
import random
import unittest

class TreeNode:

    def __init__(self, val: Optional[int] = None):

        self.val = val
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return str(self.val)
    

class BST:

    def __init__(self):
        self.root = None
        self.len = 0
    
    def insert(self, val: Any) -> None:

        def insert_helper(curr: TreeNode) -> Tuple[TreeNode, bool]:
            if not curr:
                return TreeNode(val), True

            if curr.val == val:
                return curr, False
            if curr.val < val:
                curr.right, inserted = insert_helper(curr.right)
            elif curr.val > val:
                curr.left, inserted = insert_helper(curr.left)
            
            return curr, inserted
        
        self.root, inserted = insert_helper(self.root)
        self.len += int(inserted)
    
    def insert_all(self, values: List[Any]) -> None:

        for v in values:
            self.insert(v)
    
    def _get_successor(self, node: TreeNode) -> TreeNode:
        """Assumes that the node has a right child since
        this method is used only in remove.

        :param node: [description]
        :type node: TreeNode
        :return: [description]
        :rtype: TreeNode
        """
        
        succ = None
        def get_left_most(curr: TreeNode) -> TreeNode:
            if curr.left is None:
                nonlocal succ
                succ = curr
                return curr.right
            
            curr.left = get_left_most(curr.left)
            return curr
        
        node.right = get_left_most(node.right)
        return succ

    def remove(self, val: Any) -> None:
        
        def remove_helper(curr: TreeNode) -> TreeNode:
            if not curr:
                return None
            
            if curr.val == val:
                # Current Node has only one child
                if curr.left is None:
                    return curr.right
                if curr.right is None:
                    return curr.left
                
                # Current Node has both children
                if curr.left and curr.right:
                    replace_node = self._get_successor(curr)
                    replace_node.left = curr.left
                    replace_node.right = curr.right

                    return replace_node

            if curr.val > val:
                curr.left = remove_helper(curr.left)
            if curr.val < val:
                curr.right = remove_helper(curr.right)
            
            return curr
        
        self.root = remove_helper(self.root)
    
    def inorder_traversal(self) -> List[Any]:
        traversal_arr = []
        def inorder_helper(curr: TreeNode) -> None:
            if curr is None:
                return
            inorder_helper(curr.left)
            traversal_arr.append(curr.val)
            inorder_helper(curr.right)
        
        inorder_helper(self.root)
        return traversal_arr

    def __len__(self) -> int:
        return self.len
    
    def __repr__(self) -> str:
        return self.inorder_traversal().__repr__()

class TestBST(unittest.TestCase):

    def test_add(self):
        n = 100
        values = [random.randint(0, 100000) for _ in range(n)]
        bst = BST()

        bst.insert_all(values)
        io_traversal = bst.inorder_traversal()
        self.assertEqual(io_traversal, sorted(list(set(values))))
        self.assertEqual(len(io_traversal), len(set(values)))
    
    def test_remove(self):
        n = 1000
        k = 500
        values = [random.randint(0, 5000) for _ in range(n)]
        bst = BST()

        bst.insert_all(values)
        io_traversal = bst.inorder_traversal()

        values_mut = list(set(values[:]))
        values_mut.sort()

        for _ in range(k):
            v = values[random.randint(0, len(bst)-1)]

            bst.remove(v)
            if v in values_mut:
                values_mut.remove(v)

            new_traversal = bst.inorder_traversal()
            
            self.assertEqual(new_traversal, values_mut)

unittest.main()