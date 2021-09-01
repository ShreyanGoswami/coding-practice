from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def traverse(index, preorder, limit):
            if index[0] == len(preorder) or preorder[index[0]] > limit:
                return None

            node = TreeNode(preorder[index[0]])
            index[0] += 1
            node.left = traverse(index, preorder, node.val)
            node.right = traverse(index, preorder, limit)
            return node

        return traverse([0], preorder, 100000001)


if __name__ == "__main__":
    s = Solution()
    root = s.bstFromPreorder([8, 5, 1, 7, 10, 12])
    x = 1
