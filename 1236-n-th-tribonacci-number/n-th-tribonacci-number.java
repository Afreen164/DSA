class Solution {
    public int tribonacci(int n) {
        if(n==0){

            return 0;
        }
        else if(n==1){
            return 1;
        }
        else if(n==2){
            return 1;
        }

        int one=0;
        int two =1;
        int three=1;

        for(int i=1; i<=n; i++){
            int four= one + two + three;

            one = two;
            two = three;
            three= four;
        }
        return one;
        
    }
}