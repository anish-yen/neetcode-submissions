class Solution {
    public boolean hasDuplicate(int[] nums) {
        element = 0;
        counter = 0;
        for (int i =0; i< nums.length; i++) {
            if (nums[i] == element) {
                counter++;
                
            }
            if (counter > 1) {
                return true;
            }
            // 1343
        }
    }
}