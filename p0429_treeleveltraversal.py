"Given an n-ary tree, return the level order traversal of its nodes' values."

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        # first in first out queue
        result = []
        nodelist = [root]
        while len(nodelist) > 0:
            result.append([n.val for n in nodelist if n is not None])
            nodelist = self.flatten([n.children for n in nodelist if n is not None])

        return [] if result == [[]] else result
    
    def flatten(self, list):
        newlist = []
        for l in list:
            for i in l:
                newlist.append(i)
        return newlist

n1 = Node(1, [
        Node(3, [
            Node(5, []), Node(6, [])]),
        Node(2, []),
        Node(4, [])])

n2 = Node(1, [
        Node(2, []),
        Node(3, [
            Node(6, []),
            Node(7, [
                Node(11, [
                    Node(14, [])
                ]),
            ])
        ]),
        Node(4, [
            Node(8, [
                Node(12, [])
            ])
        ]),
        Node(5, [
            Node(9, [
                Node(13, [])
            ]),
            Node(10, [])
        ])
])

n3 = Node(1, [])

s = Solution()
print(s.levelOrder(n1))
print(s.levelOrder(n2))
print(s.levelOrder(n3))
print(s.levelOrder(None))