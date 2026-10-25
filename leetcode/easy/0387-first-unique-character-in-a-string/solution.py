class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = "leetcode"
        letters = [0, 3] #FIFO

        for letter in s:

            l_count = s.count(letter)

            if l_count == 1:

                letters.append(s.index(letter))

        if letters:

            return letters.pop(0)
            
        else:

            return -1
        

        