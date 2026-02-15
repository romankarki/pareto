class Solution:


    def longest_balanced(self, s: str) -> int:
        n = len(s)
        ans = 1

        # case 1 - single char runs
        cnt = 1 
        for i in range(1, n):
            if s[i] == s[i-1]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
        
        #case 2 - exactly two chars
        pairs = [('a','b'), ('a','c'), ('b','c')]

        for x, y in pairs:
            diff_map = {0: -1}
            dx = dy = 0 

            for i, ch in enumerate(s):
                if ch == x:
                    dx += 1
                elif ch == y:
                    dy += 1
                else:
                    diff_map = {0: i}
                    dx = dy = 0 
                    continue 
                diff = dx - dy 
                if diff in diff_map:
                    ans = max(ans, i - diff_map[diff])
                else:
                    diff_map[diff] = i 
        # case 3: all three chars

        ca = cb = cc = 0 
        diff_map = {(0,0):-1}

        for i, ch in enumerate(s):
            if ch =='a':
                ca += 1
            elif ch =='b':
                cb += 1
            else:
                cc += 1
            key = (ca - cb, ca - cc)
            if key in diff_map:
                ans = max(ans, i- diff_map[key])
            else:
                diff_map[key] = i 
        return ans 