#Two Sum

'''Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000'''

# nums = [3,4,5,6]
# target = 7

# nums = [4,5,6]
# target = 10

nums = [5,5]
target = 10

# two pointer works only if the input list is sorted.

def two_sum(nums,target):
    left = 0
    right = len(nums)-1
    while left < right:
        summation = nums[left] + nums[right]
        if summation == target:
            return [left, right]
        elif summation < target:
            left += 1
        elif summation > target:
            right -= 1
    return []

print(two_sum(nums,target))

# Time complexity: O(n) 
# Space complexity: O(1)

# Brute Force code
def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            summation = nums[i] + nums[j] 
            if summation == target:
                return [i,j]
    return []
        
print(two_sum(nums,target))

# Time complexity: O(n^2) 
# Space complexity: O(1)

