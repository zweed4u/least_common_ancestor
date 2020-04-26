#!//usr/bin/python3
# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem
class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.info}"


def lca(root, v1, v2):
    # sort vertices such that v1 is lesser/left then v2 right
    v1, v2 = min([v1, v2]), max([v1, v2])

    curr_node = root
    if curr_node.info == v1 or curr_node.info == v2:
        return curr_node
    if v1 < curr_node.info < v2:
        return curr_node
    while curr_node.left is not None or curr_node.right is not None:
        if v1 < curr_node.info < v2:
            return curr_node
        if curr_node.info == v1 or curr_node.info == v2:
            return curr_node
        if v1 < curr_node.info and v2 < curr_node.info:
            curr_node = curr_node.left
        elif v1 > curr_node.info and v2 > curr_node.info:
            curr_node = curr_node.right
        else:
            pass


"""
EXAMPLE 1
                5
        3              8
    2       4       6
1                       7 
"""
root = Node(5)
exampleTree = root
exampleTree.left = Node(3)
exampleTree.left.left = Node(2)
exampleTree.left.right = Node(4)
exampleTree.left.left.left = Node(1)
exampleTree.right = Node(8)
exampleTree.right.left = Node(6)
exampleTree.right.left.right = Node(7)

v1, v2 = 4, 8
print(f"Least common ancestor: {lca(exampleTree, v1, v2)}")


"""
EXAMPLE 2
                    9
                7
            5       8
        4       6
    3
1
"""
root = Node(9)
exampleTree = root
exampleTree.left = Node(7)
exampleTree.left.left = Node(5)
exampleTree.left.right = Node(8)
exampleTree.left.left.left = Node(4)
exampleTree.left.left.right = Node(6)
exampleTree.left.left.left.left = Node(3)
exampleTree.left.left.left.left.left = Node(1)

v1, v2 = 8, 6
print(f"Least common ancestor: {lca(exampleTree, v1, v2)}")
