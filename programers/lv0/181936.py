'''
문제 : 181936 - 공배수
날짜 : 2023-11-03 16:59
## 문제
정수 `number`와 `n`, `m`이 주어집니다. `number`가 `n`의 배수이면서 `m`의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.

### 제한사항
- 10 ≤ `number` ≤ 100
- 2 ≤ `n`, `m` < 10

'''
def solution(number, n, m):
    return int(not(number % n) and not(number % m))