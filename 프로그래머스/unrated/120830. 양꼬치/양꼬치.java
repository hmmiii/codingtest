class Solution {
    public int solution(int n, int k) {
        // 양꼬치는 그냥 금액에 인분을 곱한다
        // 음료수는 10인분마다 서비스 1개
        // 양꼬치 인분 / 10 = 서비스 개수?
        int yang = 12000 * n;
        int service = n / 10;
        int drink = 2000 * (k - service);
        int answer = yang + drink;
        return answer;
    }
}