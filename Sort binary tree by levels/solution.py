from collections import  deque
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
def tree_by_levels(node: 'Node'):
    if not node:
        return []
    queue = deque([node])
    result = []
    while queue:
        result.append(queue.popleft().value)
        if result[-1].left:
            queue.append(node.left)
        if result[-1].right:
            queue.append(node.right)
    return result

    