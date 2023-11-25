class Solution {
    public String solution(String my_string) {
        String answer = "";
        for(int i = my_string.length()-1 ; -1 < i ; i--){
            answer = answer + my_string.charAt(i);
        }

        return answer;
    }
}