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