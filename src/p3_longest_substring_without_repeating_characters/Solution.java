package src.p3_longest_substring_without_repeating_characters;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int start = 0, end = 0, result = 0;
        char[] chars = s.toCharArray();
        Map<Character, Integer> records = new HashMap<>();
        for (int i=0; i<chars.length; i++) {
            if (chars.length - start < result) {
                break;
            }
            end = i;
            if (records.containsKey(chars[i])) {
                int newStart = records.get(chars[i]) + 1;
                for (int j=start; j<newStart; j++) {
                    records.remove(chars[j]);
                }
                start = newStart;
            }
            records.put(chars[i], i);
            result = end - start + 1 > result ? end - start + 1 : result;
        }
        return result;
    }
}
