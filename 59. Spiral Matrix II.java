class Solution {
    public int[][] generateMatrix(int n) {
        // fillout in order
        int[][] ans = new int[n][n];
        int filled = 0;
        int x = 0;
        int y = 0;
        char direction = 'r';
        while(filled < n * n) {
            if(direction == 'r') {
                while(x < n && ans[y][x] == 0) {
                ans[y][x] = filled + 1;
                filled++;
                x++;
                }
                x--;
                y++;
                direction = 'd';
            } else if(direction == 'd') {
                while(y < n && ans[y][x] == 0) {
                ans[y][x] = filled + 1;
                filled++;
                y++;
                }
                x--;
                y--;
                direction = 'l';
            } else if(direction == 'l') {
                while(x >= 0 && ans[y][x] == 0) {
                ans[y][x] = filled + 1;
                filled++;
                x--;
                }
                x++;
                y--;
                direction = 'u';
            } else if(direction == 'u') {
                while(y >= 0 && ans[y][x] == 0) {
                ans[y][x] = filled + 1;
                filled++;
                y--;
                }
                x++;
                y++;
                direction = 'r';
            }
        }
        return ans;
    }
}