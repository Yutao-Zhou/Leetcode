class Solution {
    public int maximumPopulation(int[][] logs) {
        // count and calculate
        int population = 0;
        int currentMax = 0;
        int ans = 0;
        int j = 0;
        int[] birth = new int[logs.length];
        int[] death = new int[logs.length];
        for (int i = 0; i < logs.length; i++) {
            birth[i] = logs[i][0];
            death[i] = logs[i][1];
        }
        Arrays.sort(birth);
        Arrays.sort(death);
        System.out.println(Arrays.toString(birth));
        System.out.println(Arrays.toString(death));
        for (int i = 0; i < logs.length; i++) {
            population++;
            while (j < logs.length && death[j] <= birth[i]) {
                population--;
                j++;
            }
            if (population > currentMax) {
                currentMax = population;
                ans = birth[i];
            }
        }
        return ans;
    }
}