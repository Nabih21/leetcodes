#include <vector>
#include <string>
#include <iostream>
#include <unordered_map>
#include <stack>
#include <unordered_set>




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

std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {

    std::vector < std:: vector<std::string >> results;
    std::unordered_map<std::string, std::vector<std::string> > myMap;

    for (int i = 0; i < strs.size(); i++)
    {
        std::vector<int> keys(26, 0);
        std::string str = strs[i];
        for (int j = 0; j < str.size(); j++)
        {
            ++keys[str[j] - 'a'];
        }

        std::string keyString;
        for (int a = 0; a < keys.size(); a++)
        {
            keyString += ',' + std::to_string(keys[a]);
        }

        myMap[keyString].push_back(str);

    }

    for (const auto& anagrams : myMap)
    {
        results.push_back(anagrams.second);
    }

    return results;
}


 std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        
        std::unordered_map<int, int> frequencyMap ; 
        std::stack<int> countingStack;
        std::vector<int> result;
        for (int i = 0; i <= nums.size() -1 ; i++ ) 
        {
            ++frequencyMap[nums[i]] ;
            if ( !countingStack.empty()) 
            {
                if ( frequencyMap[countingStack.top()] > frequencyMap[nums[i]] )  
                {

                  int temp = countingStack.top() ;
                  countingStack.pop() ;
                  countingStack.push(nums[i]); 
                  countingStack.push(temp); 
                }
                else 
                {
                    countingStack.push(nums[i]);
                }
            }
            else 
            {
                countingStack.push(nums[i]);
            }
        }

        std::unordered_set<int> mySet ; 
        while ( k != 0 ) 
        {
            if ( !mySet.count(countingStack.top()) )
            {
            result.push_back( countingStack.top() );
            mySet.insert(countingStack.top());
            countingStack.pop() ; 
            --k;
            }
            else {
                countingStack.pop();
            }
        }
        return result;
    }


 std::string encode(std::vector<std::string>& strs) {
     std::string result;
     for (int i = 0; i < strs.size(); i++)
     {

         result += strs[i] + '|';
     }

     return result;

 }

 std::vector<std::string> decode(std::string s) {
     std::vector<std::string> result;

     std::string temp;
     for (int i = 0; i < s.length(); i++)
     {
         if (s[i] != '|')
         {
             if (s[i] != '\0')
             {
                 temp += s[i];
             }
         }
         else {
             result.push_back(temp);
             temp.clear();
         }

     }

     return result;

 }


int main() {

    std::vector<int> nums = { 1,2,2,3,3,3 };
    //int target = 10;
   //int res =  findMin(nums);

 /*   twoSum(nums, target);

    std::vector<std::string> testVec = { "bdddddddddd" , "bbbbbbbbbbc" };

    groupAnagrams(testVec);*/

    topKFrequent(nums, 2);
    

    return 0;
}
