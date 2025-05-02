class Solution:
    def maxArea(self, heights: list[int]) -> int:
        
        maxArea = 0 

        left, right = 0, len(heights) - 1

        while left < right :
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width
            if maxArea < area :
                maxArea = area
            leftValue = heights[left]
            rightValue = heights[right]
            if leftValue < rightValue : 
                left += 1 
            else : 
                right -= 1
        return maxArea
    
    
if __name__ == "__main__":
    solution = Solution()
    heights=[1,7,2,5,12,3,500,500,7,8,4,7,3,6]
    print(solution.maxArea(heights))  # Output the result




