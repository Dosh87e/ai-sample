using System;
using System.Collections.Generic;

public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        var lastSeen = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++) {
            if (lastSeen.ContainsKey(nums[i]) && i - lastSeen[nums[i]] <= k) {
                return true;
            }
            lastSeen[nums[i]] = i;
        }

        return false;
    }
}
