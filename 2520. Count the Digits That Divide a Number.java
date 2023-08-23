class Solution {
    public int countDigits(int num) {
        // convert to string and loop
        // int ans = 0;
        // String numString = Integer.toString(num);
        // for (char chr: numString.toCharArray()) {
        //     if (num % Character.getNumericValue(chr) == 0){
        //         ans++;
        //     };
        // }
        // return ans;

        // math loop
        int ans = 0;
        int n = num;
        while (n > 0) {
            if (num % (n % 10) == 0) {
                ans++;
            }
            n /= 10;
        }
        return ans;
    }
}