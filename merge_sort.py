# Recursive solution

# On place : updating the array

def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		left = arr[:mid]
		right = arr[mid:]

		# Sort the two halves
		merge_sort(left)
		merge_sort(right)

		i = j = k = 0

		# Until we reach either end of either L or R, pick larger among elements L and R and place them in the correct position at arr[k]
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1

		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1


# With return statement

def sortArray(self, nums: List[int]) -> List[int]:
	if len(nums) < 2:
		return nums
	
	mid = len(nums) // 2
	left = self.sortArray(nums[:mid])
	right = self.sortArray(nums[mid:])
	p1, p2 = 0, 0
	res = []
	
	while p1 < len(left) and p2 < len(right):
		if left[p1] <= right[p2]:
			res.append(left[p1])
			p1 +=1
		else:
			res.append(right[p2])
			p2 +=1
	
	while p1 < len(left):
		res.append(left[p1])
		p1 += 1
	
	while p2 < len(right):
		res.append(right[p2])
		p2 += 1

	return res