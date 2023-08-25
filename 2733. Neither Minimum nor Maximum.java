class Solution {
    public int findNonMinOrMax(int[] nums) {
        // Sort
        if (nums.length <= 2) {
            return -1;
        }
        Arrays.sort(nums);
        return nums[1];
    }
}