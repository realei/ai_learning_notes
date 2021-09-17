class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n= len(s1)
        m = len(s2)

        for i in range(n-m):
            print(s1[i:i+m])
            if set(s1[i:i+m]) == set(s2):
                return True
        
        return False
