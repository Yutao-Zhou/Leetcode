class Solution {
    public int maxJump(int[] stones) {
        int ans = 0;
        if (stones.length % 2 == 1) {
            for (int i = 2; i < stones.length; i += 2) {
                ans = Math.max(stones[i] - stones[i - 2], ans);
            }
            ans = Math.max(stones[stones.length - 1] - stones[stones.length - 2], ans);
            for (int i = stones.length - 4; i >= 0; i -= 2) {
                ans = Math.max(stones[i + 2] - stones[i], ans);
            }
            ans = Math.max(stones[1] - stones[0], ans);
        } else {
            for (int i = 2; i < stones.length; i += 2) {
                ans = Math.max(stones[i] - stones[i - 2], ans);
            }
            ans = Math.max(stones[stones.length - 1] - stones[stones.length - 2], ans);
            for (int i = stones.length - 3; i >= 0; i -= 2) {
                ans = Math.max(stones[i + 2] - stones[i], ans);
            }
            ans = Math.max(stones[1] - stones[0], ans);
        }
        return ans;
    }
}