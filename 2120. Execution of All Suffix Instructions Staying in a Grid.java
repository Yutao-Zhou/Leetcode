class Solution {
    public int[] executeInstructions(int n, int[] startPos, String s) {
        // simulation
        int[] ans = new int[s.length()];
        for(int i = 0; i < s.length(); i++) {
            int position[] = startPos.clone();
            int step = 0;
            for(int j = i; j < s.length(); j++) {
                switch(s.charAt(j)) {
                    case 'L':
                        position[1]--;
                        break;
                    case 'R':
                        position[1]++;
                        break;
                    case 'U':
                        position[0]--;
                        break;
                    case 'D':
                        position[0]++;
                        break;
                }
                if(position[0] < 0 || position[0] >= n || position[1] < 0 || position[1] >= n) {
                    break;
                }
                step++;
            }
            ans[i] = step;
        }
        return ans; 
    }
}