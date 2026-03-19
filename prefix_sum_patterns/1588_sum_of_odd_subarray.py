class Solution: 

    def sum_odd_length_brute(self, arr):

        subarrays = []

        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)+1):
                candidate = arr[i:j]
                if len(candidate)  % 2 == 1:
                    subarrays.append(candidate)

        result = 0 
        for each in subarrays:
            result += sum(subarrays)
        return result 