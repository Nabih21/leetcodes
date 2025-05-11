class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subMap = {}
        left, right = 0, 1
        longestSub = 1 
        tempSub = 1

        if len(s) == 0 : 
            return 0 
        subMap[s[left]] = 1

        while right < len(s) :
            if subMap.get(s[right], 0) > 0:

                if s[right] == s[left] : 
                    left += 1
                else : 
                    subMap.clear()
                    subMap[s[right]] = 1
                    left = right 
                    tempSub = 1
            else : 
                subMap[s[right]] = subMap.get(s[right], 0) + 1
                tempSub += 1

            longestSub = max(tempSub, longestSub) 
            right += 1    

        return longestSub
