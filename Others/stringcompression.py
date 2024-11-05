''' 
Input: word = "abcde"

Output: "1a1b1c1d1e"

Explanation:

Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.

For each prefix, append "1" followed by the character to comp.

'''


class Solution:
    def compressedString(self, word: str) -> str:
        # hashmap = {}
        # res = []
        # for x in word:
        #     hashmap[x] = word.count(x)
        # for k,v in hashmap.items():
        #     if v > 9:
        #         res.append(str(9))
        #         res.append(k)
        #         v = v - 9
        #     res.append(str(v))
        #     res.append(k)
        # return "".join(res)
        comp = ""
        cnt = 1
        ch = word[0]
        for x in range(1,len(word)):
            if word[x] == ch and cnt < 9:
                cnt = cnt + 1
            else:
                comp += str(cnt) + ch
                ch = word[x]
                cnt = 1
        comp = comp + str(cnt) + ch
        return comp
