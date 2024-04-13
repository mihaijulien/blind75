'''
Given the root node of a binary tree, transform the tree by swapping each node’s left and right subtrees, thus creating a mirror image of the original tree. Return the root of the transformed tree.
'''

from ds_v1.BinaryTree.BinaryTree import TreeNode

def mirror_binary_tree(root):
  
  if root is None:
    return None

  left = mirror_binary_tree(root.left)
  right = mirror_binary_tree(root.right)

  root.left = right
  root.right = left

  return root