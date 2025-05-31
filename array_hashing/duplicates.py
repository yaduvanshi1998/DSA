# Contains Duplicate

'''Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false'''

nums = [1, 2, 3, 3]

def duplicates(nums):
    hashmap = {}
    for i in nums:
        if i in hashmap:
            hashmap[i] += 1
            return True
        elif i not in hashmap: 
            hashmap[i] = 1
    return False

print(duplicates(nums))

# Time complexity id O(n)
# Space complexity id O(1)

# or 

def hasDuplicate(nums):
    hashtable = {}
    for i in nums:
        if i in hashtable:
            return True
        else:
            hashtable[i] = 1
    return False

print(hasDuplicate(nums))


# Time complexity id O(n)
# Space complexity id O(1)

# OR

def hasDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

print(hasDuplicate(nums))

# Time complexity id O(n^2)
# Space complexity id O(1)