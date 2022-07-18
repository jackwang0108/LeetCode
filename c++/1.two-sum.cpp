#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        for (int i = 0; i < nums.size(); i++)
            for (int j = i + 1; j < nums.size(); j++)
                if (nums[i] + nums[j] == target)
                    return vector<int>{i, j};
        return vector<int>{-1, -1};
    }
};

int main(void)
{
    Solution s;
    vector<int> v1{2, 7, 11, 15};
    for (auto i : s.twoSum(v1, 9))
        cout << i << ", ";
    cout << endl;
    return 0;
}