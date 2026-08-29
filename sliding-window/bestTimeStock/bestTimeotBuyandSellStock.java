import java.util.*;

class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int i = 0, j = 1;

        while (j < prices.length) {
            if (prices[i] >= prices[j])
                i = j;

            else if (prices[j] > prices[i]) {
                int curr_profit = prices[j] - prices[i];
                max = Math.max(max, curr_profit);
            }

            j++;
        }

        return max;
    }
}
