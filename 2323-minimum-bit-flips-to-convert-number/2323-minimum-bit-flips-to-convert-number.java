import java.util.*;

class Solution {
    public int minBitFlips(int start, int goal) {
        String bt = Integer.toBinaryString(start^goal);
            
            long cnt = bt.chars().filter(c -> c == '1').count();
            
            return (int)cnt;
    }
}