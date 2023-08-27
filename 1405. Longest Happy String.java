class Solution {
    public String longestDiverseString(int a, int b, int c) {
        char[] ans = new char[a + b + c];
        char[] answer = ans;
        int last_a = 0, last_b = 0, last_c = 0;
        for (int i = 0; i < ans.length; i++) {
            if (a != 0 && ((a >= b && a >= c && last_a != 2) || last_b == 2 || last_c == 2)) {
                ans[i] = 'a';
                a--;
                last_a++;
                last_b = 0;
                last_c = 0;
            } else if (b != 0 && ((b >= a && b >= c && last_b != 2) || last_a == 2 || last_c == 2)) {
                ans[i] = 'b';
                b--;
                last_b++;
                last_a = 0;
                last_c = 0;
            } else if (c != 0 && ((c >= a && c >= b && last_c != 2) || last_a == 2 || last_b == 2)) {
                ans[i] = 'c';
                c--;
                last_c++;
                last_a = 0;
                last_b = 0;
            } else {
                answer = Arrays.copyOfRange(ans, 0, i);
                break; 
            }
        }
        return String.valueOf(answer);
    }
}