class Solution {
    public void sortColors(int[] nums) {
      int low =0;
      int mid=0;
      int h = nums.length -1;
      
      while (mid <= h) {
         if (nums[mid]==0){
            int tmp = nums[mid];
            nums[mid] = nums[low];
            nums[low] = tmp;
            low++;
            mid++;
         }
         else if(nums[mid]==1){
            mid++;
         }
         else{
            int tmp = nums[mid];
            nums[mid] = nums[h];
            nums[h] = tmp;
            h--;
         }
      }
    }
}