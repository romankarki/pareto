class Solution: 


    def vowel_conso_check(self, s: str) -> int: 
        v = 0 
        c = 0 

        vowels = set(["a","e","i","o","u"])
        consonants = set(["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"])


        for each in s:
            if each in vowels:
                v += 1
            if each in consonants:
                c += 1
        
        if c > 0:
            return v//c
        return 0