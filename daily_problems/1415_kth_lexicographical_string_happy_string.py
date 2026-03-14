class Solution:


    def get_happy_string(n: int, k: int) -> str:
        # total happy numbers = 3 * [2 ^ (n-1)]
        if k > 3 * ( 1<< (n-1)):
            return ""
        
        result = []
        choices = ['a', 'b', 'c']

        for i in range(n):

            subtree_size =  1 << (n-1-i) # 2 ^ (n-1 -i)

            for ch in choices:
                if k <= subtree_size:
                    result.append(ch)

                    choices = [c for c in  ['a','b','c'] if c != ch]
                    break 
                k -= subtree_size
        return ''.join(result)