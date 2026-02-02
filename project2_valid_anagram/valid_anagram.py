class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        
        #Create an empty dictionary
        counts = {}

        #Assign a value to the key (letter) in string 1
        for c in s:
            if c in counts:
                counts [c] += 1
            else:
                counts [c] = 1

        #nil out the value for keys that also appear in string 2
        for c in t:
            if c in counts:
                counts [c] -=1

        for key in counts:
            if counts [key] != 0:
                return False
        
        
        return True

 
        