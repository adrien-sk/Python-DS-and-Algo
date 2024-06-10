# Find two numbers such that they add up to a specific target number
# Return the indices of the two numbers
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]

# One pointer travel from Left to Right, and one from Right to Left

numbers = [2,7,11,15]
target = 9

def twoSum(self, numbers: List[int], target: int) -> List[int]:
	left, right = 0, len(numbers) - 1

	while left < right:
		if numbers[left] + numbers[right] == target:
			return [left, right]

		if numbers[left] + numbers[right] < target:
			left += 1
		else:
			right -= 1