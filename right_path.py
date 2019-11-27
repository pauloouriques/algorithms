class MyNode:
    left = None
    right = None
    root = None
    height = None


def get_tree(edges):
    tree_root = None
    tree = {}
    edges = edges.split(" ")
    for i in range(len(edges)):
        if edges[i] != "R" and edges[i] != "L":
            if edges[i + 1] != "R" and edges[i + 1] != "L":
                if edges[i] not in tree:
                    tree[edges[i]] = MyNode()
                    tree[edges[i]].root = edges[i]
                if tree_root is None:
                    tree_root = tree[edges[i]]
                    tree[edges[i]].height = 0
            elif edges[i + 1] == "R":
                if edges[i] not in tree:
                    tree[edges[i]] = MyNode()
                    tree[edges[i]].root = edges[i]
                tree[edges[i]].height = tree[edges[i - 1]].height + 1
                tree[edges[i - 1]].right = tree[edges[i]]
            elif edges[i + 1] == "L":
                if edges[i] not in tree:
                    tree[edges[i]] = MyNode()
                    tree[edges[i]].root = edges[i]
                tree[edges[i]].height = tree[edges[i - 1]].height + 1
                tree[edges[i - 1]].left = tree[edges[i]]
    return tree_root


def path(node, height):
    if node is None:
        return

    if node.height > height:
        print(node.root)

    path(node.right, height+1)
    path(node.left, height+1)

root = get_tree('1 2 L 1 3 R 2 4 L 2 5 R 3 6 L 3 7 R 4 8 R')
# root = get_tree('10 20 L 10 30 R 20 40 L 20 60 R')
path(root, 0)


