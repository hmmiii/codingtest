class Solution {
    public int solution(int n) {
        double sqr = Math.sqrt(n);
        if (sqr % 1 == 0){
            return 1;
        }else{
            return 2;
        }
    }
}
