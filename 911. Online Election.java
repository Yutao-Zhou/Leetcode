class TopVotedCandidate {
    // memory optimized
    int personLen;
    int[] times;
    int[] win;
    public TopVotedCandidate(int[] persons, int[] times) {
        HashMap<Integer,Integer> vote = new HashMap<Integer,Integer>();
        this.win = new int[persons.length];
        int currentWin = -1;
        this.personLen = persons.length;
        this.times = times;
        for(int i = 0; i < personLen; i++) {
            if(vote.get(persons[i]) != null) {
                vote.put(persons[i], vote.get(persons[i]) + 1);
            } else {
                vote.put(persons[i], 1);
            }
            if(vote.get(persons[i]) == Collections.max(vote.values())) {
                    currentWin = persons[i];
                }
            win[i] = currentWin;
        }
    }
    
    public int q(int t) {
        int l = 0;
        int r = this.personLen - 1;
        int mid = (int) (Math.floor((l + r) / 2));
        while(l < r) {
            mid = (int) (Math.floor((l + r) / 2));
            if(times[mid] < t) {
                l = mid + 1;
            } else if(times[mid] == t) {
                l = mid;
                break;
            } else {
                r = mid - 1;
            }
        }
        if(times[l] > t) {
            l--;
        }
        return this.win[l];
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj.q(t);
 */