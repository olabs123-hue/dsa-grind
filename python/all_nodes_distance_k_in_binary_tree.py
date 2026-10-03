# ======================================
# LeetCode Problem: all nodes distance k in binary tree
# Language: python3
# Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Synced by: LinkCode
# Date: 10/3/2026, 1:49:26 PM
# ======================================


from collections import defaultdict, deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            build_graph(node.left, node)
            build_graph(node.right, node)
        
        build_graph(root, None)
        
        visited = {target}
        queue = deque([target])
        distance = 0
        
        while queue:
            if distance == k:
                return [node.val for node in queue]
            
            for _ in range(len(queue)):
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            distance += 1
        
        return []