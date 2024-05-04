# 1) Solution using list of Visited nodes : Tree is visited from First leaf to Root Node
def dfsPostorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
	if not root:
		return []

	ans = []

	stack = [root]
	visited = [False]

	while stack:
		curr = stack.pop()
		v = visited.pop()

		if v:
			ans.append(curr.val)
		else:
			stack.append(curr)
			visited.append(True)
			if curr.right:
				stack.append(curr.right)
				visited.append(False)
			if curr.left:
				stack.append(curr.left)
				visited.append(False)

	return ans




# 2) Reverse of Preorder solution : Tree is visited Reversed (from Root Node to First leaf)
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
	if not root:
		return []

	ans = []
	
	stack = [root]

	while stack:
		curr = stack.pop(0)
		ans.insert(0, curr.val)

		if curr.left:
			stack.insert(0, curr.left)
		if curr.right:
			stack.insert(0, curr.right)

	return ans