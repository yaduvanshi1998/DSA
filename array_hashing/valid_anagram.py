# Valid Anagram

'''Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.'''


s = "racecar"
t = "carrace"
#brute force code
def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    sorted_s = str(sorted(s)).lower()
    sorted_t = str(sorted(t)).lower()
    if sorted_s == sorted_t:
        return True
    return False

print(valid_anagram(s,t))

# Time complexity id O(nlog m)
# Space complexity id O(n)

def valid_anagram(s,t):
    hashmap_s = {}
    hashmap_t = {}
    if len(s) != len(t):
        return False
    
    for i in s:
        if i not in hashmap_s:
            hashmap_s[i] = 1
        elif i in hashmap_s:
            hashmap_s[i] += 1
    
    for i in t:
        if i not in hashmap_t:
            hashmap_t[i] = 1
        elif i in hashmap_t:
            hashmap_t[i] += 1

    for ch in hashmap_s:
        if hashmap_s[ch] != hashmap_t.get(ch, 0):
            return False
    return True

print(valid_anagram(s,t))

# Time complexity id O(n)
# Space complexity id O(n)
    

