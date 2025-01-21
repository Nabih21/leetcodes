#include <vector>
#include <iostream>
#include <unordered_map>



int findMin(std::vector<int>& nums) {


    int n = nums.size();

    int left = 0, right = n - 1;
    int min = nums[right] ;
   

    while (left <= right) {
        int middle = (left + right) / 2;
        if (nums[middle] > nums[0])
        {
            if (nums[middle] > nums[n - 1])
            {
                left = middle + 1;
            }
            else
            {
                if (min > nums[middle]) {
                    min = nums[middle];
                }
                right = middle - 1;
            }
        }
        else if (nums[middle] < nums[0]) {
            if (min > nums[middle]) {
                min = nums[middle];
            }
            right = middle - 1;
        }
        else {
            if (min > nums[middle]) {
                min = nums[middle];
            }
            left = middle + 1; 
        }
    }


    return min;
}

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::vector<int> resultVector;
    std::unordered_map<int, int> myMap;
    for (int i = 0; i < nums.size() - 1; i++)
    {

        int complement = target - nums[i];
        if (myMap.count(complement)) {
            resultVector.push_back(myMap[complement]);
            resultVector.push_back(i);
        }
        myMap[nums[i]] = i;
    }
    return resultVector;
}


int main() {

    std::vector<int> nums = {4,5,6 };
    int target = 10;
   //int res =  findMin(nums);

    twoSum(nums, target);

 

    return 0;
}
