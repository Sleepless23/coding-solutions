# First Unique Character in a String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, find the  **first**  non-repeating character in it and return its index. If it  **does not**  exist, return `-1`.

 

 **Example 1:** 

 **Input:**  s = "leetcode"

 **Output:**  0

 **Explanation:** 

The character `'l'` at index 0 is the first character that does not occur at any other index.

 **Example 2:** 

 **Input:**  s = "loveleetcode"

 **Output:**  2

 **Example 3:** 

 **Input:**  s = "aabb"

 **Output:**  -1

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of only lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 5477 ms (beats 5.07%)  
**Memory:** 19.5 MB (beats 83.59%)  
**Submitted:** 2026-10-25T22:56:50.337Z  

```py
class Solution:
    def firstUniqChar(self, s: str) -> int:
    
        letters = []

        for letter in s:

            l_count = s.count(letter)

            if l_count == 1:

                letters.append(s.index(letter))

        if letters:

            return letters.pop(0)
            
        else:

            return -1
        

        
```

---

[View on LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/)