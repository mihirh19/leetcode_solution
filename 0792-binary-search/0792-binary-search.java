class Solution {
          public int help(int[] nums, int target, int l, int r){
            if (l <=r){
               int mid = l + (r - l) / 2;
               if (nums[mid] == target){
                  return mid;
               }
               if (nums[mid] < target){
                  return help(nums, target, mid + 1, r);
               }
               return help(nums, target, l, mid - 1);
            }
            return -1;
         }
    public int search(int[] nums, int target) {
        return help(nums, target, 0, nums.length - 1);
    }
}