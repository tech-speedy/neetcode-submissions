class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int N = nums.size();
        sort(begin(nums), end(nums));
        for(int i = 1; i < N; ++i){
            if (nums[i] == nums[i - 1])
            return true;
        }
        return false;
    }
};