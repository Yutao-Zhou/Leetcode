class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>(); 
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        for(int e : nums) {
            if(freqMap.containsKey(e)) {
                freqMap.put(e, freqMap.get(e) + 1);
            } else {
                freqMap.put(e, 1);
            }
        }
        for (int key : freqMap.keySet()) {
            for (int i = 0; i < freqMap.get(key); i++) {
                if (i >= ans.size()) {
                    ans.add(new ArrayList<>());
                }
                ans.get(i).add(key);
            }
        }
        return ans;
    }
}