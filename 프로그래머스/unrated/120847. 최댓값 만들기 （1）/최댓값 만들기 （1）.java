class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        int max = 0;
        int prev = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] > max){
                prev = max;
                max = numbers[i];
            }else if (prev < max && numbers[i] > prev) {
                prev = numbers[i];
            }
        }
        answer = max * prev;
        return answer;
    }
}