def bfsTraversal(self, root: Optional[TreeNode]) -> List[int]:
	if not root:
		return []

	ans = []
	queue = [root]

	while queue:
		curr = queue.pop(0)
		ans.append(curr.val)

		if curr.left:
			queue.append(curr.left)
		if curr.right:
			queue.append(curr.right)

	return ans