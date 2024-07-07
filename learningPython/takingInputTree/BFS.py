import collections
from typing import Optional, List


class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


class BFS:
    def bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([root])
        res = []

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)

            if level:
                res.append(level)

        return res
