class Solution:


    def longest_balanced(self, s: str) -> int:
        state_map = {tuple(): -1}
        count = {}

        max_length = 0 

        for i, char in enumerate(s):
            count[char] = count.get(char, 0) + 1

            chars = sorted(count.keys())
            if len(chars) == 1:
                max_length = max(max_length, 1)
                continue

            first_char = chars[0]
            state = tuple(count[c] - count[first_char] for c in chars[1:])

            if state in state_map:
                length = i - state_map[state]
                max_length = max(max_length, length)
            else:
                state_map[state] = i
            
        

        return max_length