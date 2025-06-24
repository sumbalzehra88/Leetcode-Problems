class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n);
        int leftsum = 0;
        int totalsum = 0;

        for (int num : nums) {
            totalsum += num;
        }

        for (int i = 0; i < n; i++) {
            int rightsum = totalsum - leftsum - nums[i];
            result[i] = abs(leftsum - rightsum);
            leftsum += nums[i];
        }

        return result;
    }
};
