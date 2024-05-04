# Recursive solution

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