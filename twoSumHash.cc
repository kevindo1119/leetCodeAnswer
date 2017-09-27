#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
        vector<int> twoSum(vector<int>& nums, int target) {
                // Use Hashing to reduce the runtime of picking int,
                // Can use double hashing or Single Hashing
                unordered_map<int, int> hashTable;
                //init hashTable
                for (int i = 0; i < nums.size(); ++i) {
                        hashTable[nums.at(i)] = i;
                }

                for (int i = 0; i < nums.size(); ++i) {
                        int rest = target - nums.at(i);

                        if (hashTable.find(rest) != hashTable.end()){
                                int index = hashTable.at(rest);
                                if (index == i) {
                                        continue;
                                } else {
                                        vector<int> result;
                                        result.push_back(i);
                                        result.push_back(index);
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
