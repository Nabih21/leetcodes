class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        setMap = {}
        left, right = 0,1
        minLeft, minRight = 0, 0 
        charMap = {}
        count = 1001
        currentValues, totalValues = 0, 0 


        for char in t : 
            if setMap.get(char, 0 )  == 0 : 
                totalValues += 1 
            setMap[char] = setMap.get(char, 0 ) + 1
            charMap[char] = 0

        
        if setMap.get(s[left], 0 ) >= 1 :
            charMap[s[left]] = 1
            if charMap[s[left]] >= setMap[s[left]] : 
                currentValues += 1
            if len(t) == 1 : 
                return s[0]


        
        while right < len(s) : 
            if setMap.get(s[right], 0) > 0 and not right == left : 
                charMap[s[right]] = charMap.get(s[right], 0) +  1
                
                if charMap[s[right]] == setMap[s[right]] : 
                    currentValues += 1
            
            while  currentValues >= totalValues :
                if right - left + 1 < count : 
                    minLeft = left
                    minRight = right 
                    count = right - left + 1

                if  setMap.get(s[left], 0) > 0  :
                    charMap[s[left]] -= 1
                    if charMap[s[left]] < setMap[s[left]] : 
                        currentValues -= 1
                left += 1
                
            right += 1
        
        if count == 1001 : 
            return ""
        else : 
            return s[minLeft:minRight+1]

       

if __name__ == "__main__":
    solution = Solution()
    s = "ADOBECODEBANCEEEE"
    t = "ABC"
    # s = "aab"
    # t = "aa"
    # s = "OUZODYXAZV" 
    # t = "XYZ"
    # s="aaaaaaaaaaaabbbbbcdd"
    # t="abcdd"
    print(solution.minWindow(s, t))  # Output the result