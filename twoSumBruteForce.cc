#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
        vector<int> twoSum(vector<int>& nums, int target) {
                for (int i = 0; i < nums.size(); ++i) {
                        for (int j = i+1; j < nums.size(); ++j) {
                                if (target - nums.at(i) == nums.at(j)) {
                                        vector<int> result{i, j};
                                        return result;
                                }
                        }
                }
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
