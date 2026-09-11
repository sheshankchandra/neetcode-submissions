from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            temp = str(len(s))
            temp += '#'
            temp += s
            encoded += temp
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decode = []

        if(len(s) == 0):
            return decode

        rem = 0
        i = 0
        curStr = ""

        while True:
            if i >= len(s):
                break
            
            if rem == 0:
                tempRem = ""
                while s[i+1] != '#':
                    tempRem += s[i]
                    i += 1
                tempRem += s[i]
                rem = int(tempRem)
                i += 2
            while rem != 0:
                curStr += s[i]
                i += 1
                rem -= 1
            decode.append(curStr)
            curStr = ""

        return decode