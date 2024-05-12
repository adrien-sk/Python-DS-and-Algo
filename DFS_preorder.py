# ------------------------------------------------------------------------------
# Iterative
def dfsPreorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
	if not root:
		return []

	ans = []
	
	stack = [root]

	while stack:
		curr = stack.pop()
		ans.append(curr.val)

		if curr.right:
			stack.append(curr.right)
		if curr.left:
			stack.append(curr.left)

	return ans

# ------------------------------------------------------------------------------
# Recursive
def dfsPreorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
	def dfs(node):
		if not node:
			return
		
		ans.append(node.val)
		dfs(node.left)
		dfs(node.right)
		
	ans = []
	dfs(root)

	return ans