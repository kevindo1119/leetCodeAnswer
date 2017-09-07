#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
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
        int lCounter = 0;
        int rCounter = nums.size()-1;
	// init lCounter to 0, rCounter to n-1
	vector<int> result;
	while (true) {
		if (lCounter == rCounter) {
		// if lCounter equals rCounter, we meet at middle of the array
		// adn we didn't find a solution.
			break;
		}
		if (nums.at(lCounter) + nums.at(rCounter) == target) {
			// nums.at(L) + nums.at(R) = target.
			result.push_back(lCounter+1);
			result.push_back(rCounter+1);
			break;
		}
		else if (nums.at(lCounter) + nums.at(rCounter) < target) {
			++lCounter;
		}
		else {
		//		else if (nums.at(lCounter) + nums.at(rCounter) > target) {
			--rCounter;
		}
	}
	return result;
    }
};

// Test Driver
int main() {

	Solution sol;
	vector<int> nums;
	nums.push_back(2);
	nums.push_back(3);
	nums.push_back(4);
	int target = 6;
	vector<int> result = sol.twoSum(nums, target);
	for (int i=0; i < result.size(); ++i) {
		cout << result[i] << ' ';
	}

	return 0;
}
