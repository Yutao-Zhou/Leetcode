class Solution {
    public int numRabbits(int[] answers) {
        int ans = 0;
        HashMap<Integer, Integer> frequency = new HashMap<Integer, Integer>();
        for (int answer : answers) {
            if (frequency.containsKey(answer)) {
                frequency.put(answer, frequency.get(answer) + 1);
            } else {
                frequency.put(answer, 1);
            }
        }
        for (int key: frequency.keySet()) {
            int group = frequency.get(key) / (key + 1);
            if (frequency.get(key) % (key + 1) != 0) {
                group++;
            }
            ans += group * (key + 1);
        }
        return ans;
    }
}