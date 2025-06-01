# Group Anagrams

'''Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.'''

strs = ["act","pots","tops","cat","stop","hat"]

strs = ["x"]

strs = [""]

def group_anagram(strs):
    hashtable = {}
    for i in strs:
        sorted_strs = ''.join(sorted(i))
        if sorted_strs not in hashtable:
            hashtable[sorted_strs] = [i]
        elif sorted_strs in hashtable:
            hashtable[sorted_strs].append(i)
    return list(hashtable.values())

print(group_anagram(strs))

# Time complexity = O(n.k log k)
# Space complexity = O(n.k)