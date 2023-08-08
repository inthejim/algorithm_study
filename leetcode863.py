# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        #parents[node]=parent

        def dfs(node, parent):
            if parent:
                parents[node.val] = parent
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)

        dfs(root, None)

        queue = deque([])
        queue.append(target)
        dist = 0

        visited = set()
        visited.add(target)

        while queue and dist != k:
            for i in range(len(queue)):
                nei = queue.popleft()

                if nei.left and nei.left not in visited:
                    queue.append(nei.left)
                    visited.add(nei.left)

                if nei.right and nei.right not in visited:
                    queue.append(nei.right)
                    visited.add(nei.right)

                #부모 노드
                if nei.val in parents and parents[nei.val] not in visited:
                    queue.append(parents[nei.val])
                    visited.add(parents[nei.val])

            dist += 1

        ans = []
        while queue:
            ans.append(queue.popleft().val)

        return ans

        
