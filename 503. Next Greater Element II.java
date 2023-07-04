class Solution {
    public int[] nextGreaterElements(int[] nums) {
        // Brute force
        ArrayList<Integer> ans = new ArrayList<>();
        int j;
        int[] returnAns = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            j = i + 1;
            while ( j < nums.length ) {
                if ( nums[j] > nums[i] ) {
                    ans.add(nums[j]);
                    break;
                }
                j++;
            }
            if ( ans.size() < i + 1 ) {
                j = 0;
                while ( j < i ) {
                    if ( nums[j] > nums[i] ) {
                        ans.add(nums[j]);
                        break;
                    }
                    j++;
                }
            }
            System.out.println(ans.size());
            if ( ans.size() < i + 1 ) {
                ans.add(-1);
            }
        }
        System.out.println(ans);
        for (int i = 0; i < returnAns.length; i++) {
            returnAns[i] = ans.get(i).intValue();
        }
        return returnAns;
    }
}