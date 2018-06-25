class Solution {
    public int peakIndexInMountainArray(int[] A) {
       // if(a.length <= 1) return 0;
        int peek_1 = 0, peek_2 = 0,max = Integer.MIN_VALUE;
        int index = 0;
        boolean forward = false,backward = false;
        while(!forward){
            if(A[index]>=max){
                peek_1 = index;
                max = A[index];
            }else{
                forward = true;
            }
            index++;
        }
        
        return peek_1;
    }
}
