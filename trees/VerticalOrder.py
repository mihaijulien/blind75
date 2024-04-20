'''
Find the vertical order traversal of a binary tree when the root of the binary tree is given. In other words, return the values of the nodes from top to bottom in each column, column by column from left to right. If there is more than one node in the same column and row, return the values from left to right.

Input Tree:
	     _ 3 _ 
	    |     |
	    2 _   3 _ 
	       |     |
	       3     1 

	Vertical order traversal: [[2], [3, 3], [3], [1]]

Input Tree:
	       ___ -10 _ 
	      |         |
	   __ -23 _     45 
	  |        |
	  25       46 

	Vertical order traversal: [[25], [-23], [-10, 46], [45]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
            if root is None:
                return []

            node_list = defaultdict(list)
            min_column = 0
            max_index = 0

            # push root into the queue
            queue = deque([(root, 0)])

            # traverse over the nodes in the queue
            while queue:
                node, column = queue.pop()

                if node is not None:
                    # add the value of the node to the dictionary
                    node_list[column].append(node.val)

                    # add current node's left and right child in the queue
                    queue.append((node.left, column - 1))
                    queue.append((node.right, column + 1))
            
            #return the list of nodes ordered by columns
            return [node_list[x] for x in sorted(node_list)]
