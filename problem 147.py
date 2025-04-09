# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        already_cloned_nodes = {}

        q = deque()
        q.append(node)
        new_node = Node(node.val)
        # Clone the 1st node and then map it with its original node in the map
        already_cloned_nodes[node] = new_node

        while q:
            curr_node = q.popleft()

            # go through the neighbors and create the clones for it if it doesnt exist in the hm
            for nbr in curr_node.neighbors:
                if nbr not in already_cloned_nodes:
                    already_cloned_nodes[nbr] = Node(nbr.val)
                    q.append(nbr)

# in the hm the clones are created to its neighbors append its corresponding cloned neighbors 
                already_cloned_nodes[curr_node].neighbors.append(already_cloned_nodes[nbr])

        return already_cloned_nodes[node]
# TC: O(V+E)
# SC: O(V) v for queue and v for hashmap



#####------------------------------------------------------------



"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        already_cloned_nodes = {}

        def dfs(node):
            if node in already_cloned_nodes:
                return already_cloned_nodes[node]
            
            new_node = Node(node.val)
            already_cloned_nodes[node] = new_node

            for nbr in node.neighbors:
                new_node.neighbors.append(dfs(nbr))
            
            return new_node

        return dfs(node)

# TC: O(V+E)
# SC: O(V)