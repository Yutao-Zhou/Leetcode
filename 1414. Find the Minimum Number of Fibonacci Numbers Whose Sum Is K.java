class Solution {
    public int findMinFibonacciNumbers(int k) {
        // generate and reverse search
        ArrayList<Integer> fibonacci = new ArrayList<Integer>(Arrays.asList(1, 1));
        int counter = 2;
        int ans = 0;
        while ( fibonacci.get(counter - 1) <= k ) {
            fibonacci.add(fibonacci.get(counter - 1) + fibonacci.get(counter - 2));
            counter++;
        }
        while (k > 0) {
            if ( fibonacci.get(counter - 1) <= k ) {
                k -= fibonacci.get(counter - 1);
                ans++;
            }
            counter--;
        }
        return ans;
    }
}