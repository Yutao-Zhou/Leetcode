class Solution {
    public int minSetSize(int[] arr) {
        // HashMap frequency
        int ans = 0;
        int removed = 0;
        HashMap <Integer, Integer> frequency = new HashMap <Integer, Integer>();
        for (int n : arr) {
            if (frequency.containsKey(n)) {
                frequency.put(n, frequency.get(n) + 1);
            } else {
                frequency.put(n, 1);
            }
        }
        List<Integer> freq = new ArrayList<Integer>(frequency.values());
        Collections.sort(freq);
        int i = freq.size() - 1;
        while (removed < arr.length / 2) {
            removed += freq.get(i);
            ans++;
            i--;
        }
        return ans;
    }
}