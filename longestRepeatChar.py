class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left, right = 0, 1
        changes = k 
        longestSub = 1
        temp = 1

        char = s[left] 
        while right < len(s) :
            if not char == s[right] :
                if changes > 0 :
                    changes -= 1
                    temp += 1
                else: 
                    left = right
                    changes = k
                    char = s[right] 
                    temp = 1
            else : 
                temp += 1
            longestSub = max(temp, longestSub) 
            right += 1
        
        return longestSub


if __name__ == "__main__":
    solution = Solution()
    s = "ABBB"
    k = 2
    print(solution.characterReplacement(s, k))  # Output the result