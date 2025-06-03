# Two Integer Sum II

'''Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O(1)
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Constraints:

2 <= numbers.length <= 1000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000'''

numbers = [1,2,3,4]
target = 3

def two_sum2(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            summation = numbers[i] + numbers[j]
            if summation == target and i < j:
                return [i + 1, j + 1]
    return []

print(two_sum2(numbers, target))

# Time complexity is O(n^2)
# Space complexity is O(1)

# Since we have sorted list we can use two pointer methods

def two_sum2(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        summation = numbers[left] + numbers[right]
        if summation < target:
            left += 1
        elif summation > target:
            right -= 1
        elif summation == target and left < right:
            return [left + 1, right + 1]
    return []

print(two_sum2(numbers, target))

# Time complexity is O(n)
# Space complexity is O(1)
