# Top K Frequent Elements

'''Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.'''


nums = [1,2,2,2,3,3,3,3,1]
k = 2

nums = [7,7]
k = 1

def topK_frequent(nums,k):
    hashtable = {}
    for i in nums:
        if i not in hashtable:
            hashtable[i] = 1
        elif i in hashtable:
            hashtable[i] += 1
    print(hashtable)

    def get_item(item):
        return item[1]    

    sorted_hashtable = sorted(hashtable.items(), key = get_item,  reverse = True)
    print(sorted_hashtable)
    result = []
    for i in range(k):
        result.append(sorted_hashtable[i][0])
    return result

print(topK_frequent(nums,k))

# Time complexity = O(n + m log m)
# Space complexity = O(m)