# Recursive solution

def quickSort(arr):
	if len(arr) < 2:
		return arr

	left = []
	right = []
	pivot = arr.pop()

	for num in arr:
		if num > pivot:
			right.append(num)
		else:
			left.append(num)

	return quickSort(left) + [pivot] + quickSort(right)