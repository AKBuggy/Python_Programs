from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res


def construct_tree_from_list(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        current = queue.popleft()

        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)

        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)

        i += 1

    return root


def parse_input(input_str: str) -> List[Optional[int]]:
    # Check if the input_str is only "[]"
    if input_str.strip() == '[]':
        return []
    # Otherwise, proceed to parse the string
    values = input_str.strip()[1:-1].split(',')
    # Ensure that we ignore empty strings resulting from split
    nodes = [int(val) if val.strip() != "null" and val.strip() != '' else None for val in values]
    return nodes



# Main execution starts here
if __name__ == "__main__":
    # Take input from the user
    input_str = input("Enter tree nodes in the format [3,9,20,null,null,15,7]: ")
    nodes = parse_input(input_str)

    # Construct the tree
    root = construct_tree_from_list(nodes)

    # Perform level order traversal
    sol = Solution()
    print(sol.levelOrder(root))
