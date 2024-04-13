'''
Given a binary tree, you need to compute the length of the tree’s diameter. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

    Note: The length of the path between two nodes is represented by the number of edges between them.

eg.

     1
    / \
   2   3
      / \
     4   5
    /
   6

Output: 4
The number of edges between red node 2 and red node6 is 4, which is the diameter of the tree.

'''

def diameter_of_binaryTree(root):

  if root == None:
    return

  left = height(root.left)
  right = height(root.right)

  return left + right

def height(root):
  if root == None:
    return 0
  left = height(root.left)
  right = height(root.right)

  return max(left, right) + 1