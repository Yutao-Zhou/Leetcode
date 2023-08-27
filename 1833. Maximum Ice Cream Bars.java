class Solution {
    public int maxIceCream(int[] costs, int coins) {
        int ans = 0;
        Arrays.sort(costs);
        for ( int iceCream : costs) {
            coins -= iceCream;
            if( coins >= 0) {
                ans++;
            } else {
                break;
            }
        }
        return ans;
    }
}