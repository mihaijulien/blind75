'''
Serialize a given binary tree to a file and deserialize it back to a tree. Make sure that the original and the deserialized trees are identical.

    Serialize: Write the tree to a file.

    Deserialize: Read from a file and reconstruct the tree in memory.

Serialize the tree into a list of integers, and then, deserialize it back from the list to a tree. For simplicity’s sake, there’s no need to write the list to the files.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        def preorder(root):
            if not root:
                result.append('null')
                return
            result.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        self.i = 0
        def preorder():
            if data[self.i] == 'null':
                self.i += 1
                return None
            root = TreeNode(int(data[self.i]))
            self.i += 1
            root.left = preorder()
            root.right = preorder()
            return root
        
        return preorder()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
