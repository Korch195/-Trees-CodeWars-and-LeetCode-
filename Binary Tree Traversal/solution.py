class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

# Pre-order traversal
def pre_order(node: 'Node'):
    result = [node.data]
    result.extend(pre_order(node.left))
    result.extend(pre_order(node.right))
    return result if node else []

# In-order traversal
def in_order(node: 'Node'):
    result = []
    result.extend(in_order(node.left))
    result.append(node.data)
    result.extend(in_order(node.right))
    return result if node else []

# Post-order traversal
def post_order(node: 'Node'):
    result = []
    result.extend(in_order(node.left))
    result.extend(in_order(node.right))
    result.append(node.data)
    return result if node else []
