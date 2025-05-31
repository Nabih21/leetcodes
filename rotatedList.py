class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        res = -1
        pivot = -1
        count = 0
        mid = 0
        

        while left <= right : 
            count += 1
            mid = (left + right)//2 
            if nums[mid-1] > nums[mid] and nums[mid] < nums[mid+1] :
                pivot = mid 
                break  
            elif nums[left] < nums[mid] :
                left = mid + 1 
            elif nums[mid] < nums[right]: 
                right = mid 
            
    
        
        return pivot
    
    

if __name__ == "__main__":
    solution = Solution()
    # nums = [4,5,6,7,0,1,2]
    nums=[3,5,6,0,1,2]

    print(solution.search(nums, 4))  # Output the result

                