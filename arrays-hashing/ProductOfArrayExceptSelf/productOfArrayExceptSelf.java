import java.util.*;

class Solution {

    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] prefix = new int[n + 1];
        int[] suffix = new int[n + 1];

        Arrays.fill(prefix, 1);
        Arrays.fill(suffix, 1);

        for (int i = 0; i < n; i++)
            prefix[i + 1] = prefix[i] * nums[i];

        int i = n;
        while (i > 0) {
            suffix[i - 1] = suffix[i] * nums[i - 1];
            i--;
        }

        int[] res = new int[n];
        for (int j = 0; j < n; j++) {
            int suffixProd = suffix[j + 1] / suffix[n];
            int prefixProd = prefix[j] / prefix[0];
            res[j] = suffixProd * prefixProd;
        }

        return res;
    }

    public int[] productExceptSelfBetter(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];

        // 1. Compute prefix products directly into res
        int prefix = 1;
        for (int i = 0; i < n; i++) {
            res[i] = prefix;
            prefix *= nums[i];
        }

        // 2. Multiply by suffix products on the fly (from right to left)
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= suffix;
            suffix *= nums[i];
        }

        return res;
    }
}