class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {} # char : number of that char
        for c in s:
            if c in hashmap:
                hashmap[c] = hashmap[c] + 1
            else:
                hashmap[c] = 1

        for c in t:
            if c in hashmap:
                hashmap[c] = hashmap[c] - 1
            else:
                return False
        
        for c in hashmap:
            if hashmap[c] != 0:
                return False

        return True
        
