class Solution {
    public String[] findRelativeRanks(int[] nums) {
        int [] temp = new int [nums.length];
     for (int i =0;i< nums.length; i++){
         temp[i] = nums[i];
     }
        Arrays.sort(nums);
        //recork the mark and the ranking
        Map <Integer, Integer> ranking  = new HashMap<Integer, Integer>(); 
        String[] result = new String [nums.length];
        for (int i =0;i< nums.length; i++){
            ranking.put(nums[i],nums.length-i) ;
        }
        
    for (int i =0;i< temp.length; i++){
        int rank = ranking.get(temp[i]);
            if(rank==1) result[i] = "Gold Medal";
            else if(rank==2) result[i] = "Silver Medal";
            else if(rank==3) result[i] = "Bronze Medal";
            else result[i] = String.valueOf(rank);
        }
        
        return result;
    }
}
