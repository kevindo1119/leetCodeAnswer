#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
        vector<vector<int>> threeSum(vector<int>& nums, int target) {
                // Note that this is the naive solution and this algo uses O(n^3) runtime
                // And this threeSum problem is modified by me:
                //      Original quesiton target == 0
                //      New use int target
                vector<vector<int>> result;
                for (int i=0; i < nums.size(); ++i) {
                        for (int j=i+1; j < nums.size(); ++j) {
                                for (int k=j+1; k < nums.size(); ++k) {
                                        if (nums.at(i) + nums.at(j) + nums.at(k) == target) {
                                                vector<int> tempResult{nums.at(i), nums.at(j), nums.at(k)};
                                                result.push_back(tempResult);
                                        }
                                }
                        }
                }
                return result;
        }
};

// Test Diver

int main() {

        Solution sol;
        vector<int> nums;
        nums.push_back(-1);
        nums.push_back(0);
        nums.push_back(1);
        nums.push_back(2);
        nums.push_back(-1);
        nums.push_back(-4);
        int target = 0;

        vector<vector<int>> result;
        result = sol.threeSum(nums, target);
        for (int i=0; i < result.size(); ++i) {
                for (int j=0; j < result.size(); ++j) {
                        cout << result[i][j] << ' ';
                }
                cout << endl;
        }
}
