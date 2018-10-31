class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_path(root, path, k):
    if root is None:
        return False

    if root.key is k:
        return True
    
    path.append(root.key)

    if ((root.left is not None and find_path(root.left, path, k))
        or (root.right is not None and find_path(root.right, path, k))):
        return True   

    path.pop()

    return False

def find_lca(root, n1, n2):
    path1 = []
    path2 = []

    if (not find_path(root, path1, n1) or not find_path(root, path2, n2)):
        return -1

    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] is not path2[i]:
            break
        i += 1

    return path1[i-1]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.left  = Node(6)
root.right.right = Node(7)

print("LCA(2, 3) = %d" %(find_lca(root, 2, 3))) 
print("LCA(6, 7) = %d" %(find_lca(root, 6, 7)))
print("LCA(4, 5) = %d" %(find_lca(root, 4, 5))) 
print("LCA(8, 9) = %d" %(find_lca(root, 8, 9))) 