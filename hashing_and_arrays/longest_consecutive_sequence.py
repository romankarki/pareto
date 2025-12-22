def longest_sequence(nums):
    '''
    basically by sorting adn counting consecutives also works fine 
    but the bottle neck is o(n lon(n))

    we can do better with a single scan or multiple single shot scans  
    '''
    numSet = set(nums)

    longest = 0 
    for num in numSet:
        if (num - 1) not in numSet:
            length = 1 
            while (num + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest