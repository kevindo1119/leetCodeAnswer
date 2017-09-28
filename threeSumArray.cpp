#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    // This is a constant space solution
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
	    // my own solution is based on sorted array
	// lCounter trace from first element, and rCounter trace from last element
	// shift the lCounter and rCounter based on comparesion with target.
	// since the lCounter and rCounter together counts n elements
	// so the run time will be O(n)
	// Note:
	//	1. My Algo solves:
	//		a) Whether there is a soltion
	//		b) I can find one solution
	//		c) If there's more than one solution, I can't find the second
	// 	2. Using Brute Force, this problem can be done in O(n^2).
        // 	3. Using Hash table, this problem can also can be done in O(n).
        
        // Corner checking
        if (nums.size() <= 2) {
            return result;
        }
        
        // sort the array
        std::sort(nums.begin(),nums.end());
        
        for (int i=0; i< nums.size()-2; ++i) {
            int lCounter = i + 1;
            // rCounter = n-1; last element
            int rCounter = nums.size() - 1;
            
            while (lCounter < rCounter) {
                
                    vector<int> tempResult;
                    if (nums.at(i) + nums.at(lCounter) + nums.at(rCounter) == 0) {
                        // x + y + z = 0
                        // cout <<"first is: " <<  nums.at (i) << endl;
                        // cout <<"second is: " <<  nums.at (lCounter) << endl;
                        // cout <<"third is: " <<  nums.at (rCounter) << endl;
                        tempResult.push_back(nums.at(i));
                        tempResult.push_back(nums.at(lCounter));
                        tempResult.push_back(nums.at(rCounter));
                        result.push_back(tempResult);
                        ++lCounter;
                        --rCounter;
                        
                        while (lCounter < rCounter && nums.at(lCounter - 1) == nums.at(lCounter)) {
                            ++lCounter;
                        }
                        
                        while (lCounter < rCounter && nums.at(rCounter) == nums.at(rCounter+1)) {
                            --rCounter;
                        }
                    } else if (nums.at(i) + nums.at(lCounter) + nums.at(rCounter) < 0) {
                        ++lCounter;
                    } else {
                        // nums.at(i) + nums.at(lCounter) + nums.at(rCounter) > 0
                        --rCounter;
                    }
                    
                    while (i < nums.size()-1 && nums.at(i) == nums.at(i+1)) {
                        ++i;
                    }
            }
        }
        return result;
    }
};

public:
    vector<int> threeSum(vector<int>& nums, int target) {
    // my own solution is based on sorted array
	// Uses my private function; twoSum to help three sum, its basically:
	// twoSum(ints, target-every element in array)
	// functin returns true if there's a solution with x + y = target - z;
	// so the run time will be O(n*n) = O(n^2)
    // And this threeSum problem is modified by me:
    //      Original quesiton target == 0
    //      New use int target
	// Note:
	//	1. My Algo solves:
	//		a) Whether there is a soltion
	//		b) I can find one solution
	//		c) If there's more than one solution, I can't find the second
	// 	2. Using Brute Force, this problem can be done in O(n^3).
        // 	3. Using Hash table, this problem can also can be done in O(n^2).
        int lCounter = 0;
        int rCounter = nums.size()-1;
	// init lCounter to 0, rCounter to n-1
	vector<int> result;

	for (int i = 0; i < nums.size(); ++i) {
		vector<int> result = this->twoSum(nums, target-nums.at(i)); 
		// result first stores intermidiate value x and y
		if (result.size() == 2) {
			// there is a solution makes x+y = target-z
			// and x, y are stored in result
			result.push_back(nums.at(i));
			return result;
		} else {
			continue;
		}
	}
	// there's no solution and we can return an empty vector
	vector<int> temp;
	return temp;
	}
};

// Test Driver
int main() {

	Solution sol;
	vector<int> nums;
	nums.push_back(2);
	nums.push_back(3);
	nums.push_back(4);
	nums.push_back(5);
	vector<int> result = sol.threeSum(nums, 10);
	for (int i=0; i < result.size(); ++i) {
		cout << result[i] << ' ';
	}

	return 0;
}
