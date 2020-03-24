from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, arr):
        self.root = self.__generate(arr)

    def __generate(self, arr):
        if len(arr) < 1:
            return None
        
        # Assume first element as tree root
        root = Node(self.__pop_first(arr))

        # Create a deque to support tree insertion
        parent_queue = deque()
        parent_queue.append(root)

        while parent_queue.__len__() > 0:
            node = parent_queue.popleft()
            left = self.__pop_first(arr)
            right = self.__pop_first(arr)

            if left != None:
                node.left = Node(left)
                parent_queue.append(node.left)
            if right != None:
                node.right = Node(right)
                parent_queue.append(node.right)
        
        return root

    def __pop_first(self, arr):
        if len(arr) > 0:
            return arr.pop(0)
        return None

    def bfs(self):
        node_traverse = deque()
        node_traverse.append(self.root)
        while node_traverse.__len__() > 0:
            node = node_traverse.popleft()
            if node != None:
                print(node.value)
                if node.left != None:
                    node_traverse.append(node.left)
                if node.right != None:
                    node_traverse.append(node.right)
    
    def dfs_preorder(self, node):
        if node == None:
            return
        print(node.value)
        self.dfs_preorder(node.left)
        self.dfs_preorder(node.right)
    
    def dfs_inorder(self, node):
        if node == None:
            return
        self.dfs_inorder(node.left)
        print(node.value)
        self.dfs_inorder(node.right)
    
    def dfs_postorder(self, node):
        if node == None:
            return
        self.dfs_postorder(node.left)
        self.dfs_postorder(node.right)
        print(node.value)