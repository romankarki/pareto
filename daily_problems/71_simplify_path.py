from typing import List

class Solution:

    def simplify_path(self, path: str) -> str:

        res = []
        ip = []

        l, r = 0, len(path) - 1
        while l <= r:
            if path[l] == "/":
                l += 1
                continue
            each = ""
            while l<=r and path != "/":
                each += path[l]
                l += 1
            ip.append(each)
        
        for each in ip:
            if each == ".":
                continue

            if each == "..":
                res.pop()
                continue
            elif not len(res)  and each == "..":
                continue
            

            res.append(each)
        

        return "/" + "/".join(res)



s = Solution()

print(s.simplify_path("/.../a/../b/c/../d/./"))