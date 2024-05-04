def dfsInorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
	if not root:
		return []

	ans = []

	stack = []
	curr = root

	while stack or curr:
		while curr:
			stack.append(curr)
			curr = curr.left

		node = stack.pop()
		ans.append(node.val)
		curr = node.right

	return ans