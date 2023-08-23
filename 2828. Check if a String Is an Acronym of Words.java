class Solution {
    public boolean isAcronym(List<String> words, String s) {
        //  Brute force
        // String ans = "";
        // for (String word : words) {
        //     ans = ans + word.charAt(0);
        // }
        // return ans.equals(s);

        // StringBuilder
        // StringBuilder ans = new StringBuilder();
        // for (String word : words) {
        //     ans.append(word.charAt(0));
        // }
        // return ans.toString().equals(s);

        // Compare on the fly
        if (words.size() != s.length()) {
            return false;
        }
        for (int i = 0; i < words.size(); i++) {
            if (s.charAt(i) != words.get(i).charAt(0)) {
                return false;
            }
        }
        return true;
    }
}