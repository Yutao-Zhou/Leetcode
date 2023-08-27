class Solution {
    public String strWithout3a3b(int a, int b) {
        char[] ans = new char[a + b];
        int last_a = 0;
        int last_b = 0;
        for (int i = 0; i < ans.length; i++) {
            if ((a > b && last_a != 2) || last_b == 2) {
                ans[i] = 'a';
                a--;
                last_a++;
                last_b = 0;
            } else {
                ans[i] = 'b';
                b--;
                last_b++;
                last_a = 0;
            }
        }
        return String.valueOf(ans);
    }
}