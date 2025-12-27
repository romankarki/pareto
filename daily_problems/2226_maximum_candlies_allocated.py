class Solution:

    def max_candies(self, candies, k):
        total = sum(candies)
        if total < k: 
            return 0 
        if total == k: 
            return 1
        
        l = 1
        r = total // k

        ans = l

        while l <= r:
            m = (l + r) // 2
            if self.can_be_dist(candies, m, k) : 
                ans = m 
                l = m + 1
            else:
                r = m - 1 

        return ans


    def can_be_dist(self, candies, pile, target):

        output = 0 
        for each in candies: 

            y = each // pile
            output += y 

        return output >= target


i = [5, 8, 5, 100]
k = 3

s = Solution()

a = s.max_candies(i, k)

print("answer is",a)