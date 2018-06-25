class Solution {
    //math problems
    public int minMoves(int[] nums) {
       int sumBefore = IntStream.of(nums).sum();
        int length = nums.length;
        Arrays.sort(nums);
        int minNum = nums[0];
        return sumBefore- length*minNum;
    }
}
