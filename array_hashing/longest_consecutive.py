# Longest Consecutive Sequence

'''Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9'''


nums = [2,20,4,10,3,4,5]

def longest_consequtive(nums):
    numset = set(nums)
    longest = 0

    for i in nums:
        if (i-1) not in numset:
            length = 0
            while (i+length) in numset:
                length += 1
            longest = max(longest, length) 
    return longest

print(longest_consequtive(nums)) 

# Time Complexity: O(n)

# Space Complexity: O(n)

