class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        charSet = set()
        charMap = {}
        # shortestStr = ""
        minLeft, minRight = 0, 1
        count = 1001

        for char in t :
            charSet.add(char)
            charMap[char] = 0

        # for key, value in enumerate(s) : 
        #     charMap[key] = charMap.get(key, 0 ) + 1
        
        left, right = 0, 1
        if s[left] in charSet :
            charMap[s[left]] = 1

        while right < len(s) :
            
            if s[right] in charSet: 
                charMap[s[right]] += 1

            while  all( v >= 1 for v in charMap.values()) :
                if ( right - left + 1 < count ): 
                    minLeft = left
                    minRight = right
                    count = right - left + 1
                if s[left] in charSet : 
                    charMap[s[left]] -= 1
                left += 1
                       
            right += 1
            
        if count == 1001 :
            return ""
        else : 
           return  s[minLeft:minRight+1]




if __name__ == "__main__":
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(solution.minWindow(s, t))  # Output the result