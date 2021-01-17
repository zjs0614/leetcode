package src.p1_two_sum;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> records = new HashMap<Integer, Integer>();

        for (int i=0; i<nums.length; i++) {
            int rest = target - nums[i];
            if (records.get(rest) != null) {
                return new int[]{records.get(rest), i};
            }
            records.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}