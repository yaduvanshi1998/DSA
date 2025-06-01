# Encode and Decode Strings

'''Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.'''

strs =  ["neet","code","love","you"]

def encode(strs):
    encoded_strs = ""
    for i in strs:
        encoded_strs += str(len(i)) + "#" + i
    return encoded_strs 

encoded_data = encode(strs)

def decode(encoded_data):
    i = 0
    right = len(encoded_data) - 1
    result = []
    while i < right:
        j = i
        while encoded_data[j] != "#":
            j += 1
        length = int(encoded_data[i:j])
        result.append(encoded_data[j + 1 : j + 1 + length])
        i = j + 1 + length
    return result

print(encode(strs))
print(decode(encoded_data))

