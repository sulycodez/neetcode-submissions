class Solution:
    def isValid(self, s: str) -> bool:
        valid = []
        Map = { "(" : ")", "{" : "}", "[": "]" }
        for c in s: 
            if c in Map:
                valid.append(c)
            else:
                if not valid or Map[valid[-1]] != c :
                    return False
                valid.pop()
        return not valid 
                
              