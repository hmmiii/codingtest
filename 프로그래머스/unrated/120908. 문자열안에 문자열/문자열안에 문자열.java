class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        answer = str1.indexOf(str2) != -1  ? 1 : 2;
        return answer;
    }
}