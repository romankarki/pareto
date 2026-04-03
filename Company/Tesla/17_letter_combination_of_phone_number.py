from typing import List

class Solution: 

    def letter_combination(self, digits: str) -> List[str]:
        t = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d','e','f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        res = [] 
        def dfs(i, curr):
            if len(digits) == len(curr):
                word = "".join(curr)
                res.append(word)
                return 

            if i >= len(digits):
                return 
            
            arr = t[digits[i]]
            for each in arr:
                curr.append(each)
                dfs(i+1, curr)
                curr.pop()

        dfs(0, [])
        return res 