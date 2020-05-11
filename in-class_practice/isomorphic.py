'''Leetcode #205: - https://leetcode.com/problems/isomorphic-strings/ - Easy

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''

def is_isomorphic(text1, text2):
    if len(text1) != len(text2):
        return False
        
    mapped = {}

    for i, char in enumerate(text1):
        if char in mapped:
            if text2[i] != mapped[char]:
                return False
        else:
            if text2[i] in mapped.values():
                return False
            mapped[text1[i]] = text2[i]
        i += 1
    return True
    

print(is_isomorphic('foo', 'bar'))
