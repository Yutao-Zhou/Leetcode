class Solution {
    public String reorganizeString(String s) {
        // Count and recrate
        char[] ans = new char[s.length()];
        int[] frequency = new int[26];
        for (int i = 0; i < s.length(); i++) {
            frequency[(int) s.charAt(i) - 97] += 1;
        }
        int maxCount = 0, letter = 0;
        for (int i = 0; i < frequency.length; i++) {
            if (frequency[i] > maxCount) {
                maxCount = frequency[i];
                letter = i;
            }
        }
        int j = 0;
        while (frequency[letter] != 0 && j < ans.length) {
            ans[j] = (char) (letter + 'a');
            frequency[letter]--;
            j += 2;
        }
        if (frequency[letter] != 0) {
            return "";
        }
        for (int i = 0; i < frequency.length; i++) {
            while (frequency[i] > 0) {
                if (j >= ans.length) {
                    j = 1;
                }
                ans[j] = (char) (i + 'a');
                frequency[i]--;
                j += 2;
            }
        }
        return String.valueOf(ans);
    }
}