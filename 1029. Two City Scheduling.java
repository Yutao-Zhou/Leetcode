class Solution {
    public int twoCitySchedCost(int[][] costs) {
        int ans = 0;
        int[] cost_diff = new int[costs.length];
        for (int i = 0; i < costs.length; i++) {
            cost_diff[i] = costs[i][0] - costs[i][1];
            ans += costs[i][0];
        }
        Arrays.sort(cost_diff);
        for (int i = cost_diff.length / 2; i < cost_diff.length; i++) {
            ans -= cost_diff[i];
        }
        return ans;
    }
}