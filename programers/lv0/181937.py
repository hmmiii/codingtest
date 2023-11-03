'''
문제 : 181937 - n의 배수
날짜 : 2023-11-03 16:45
## 문제
정수 `num`과 `n`이 매개 변수로 주어질 때, `num`이 `n`의 배수이면 1을 return `n`의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.

### 제한사항
- 2 ≤ `num` ≤ 100
- 2 ≤ `n` ≤ 9

### 입출력 예
|num|n|result|
|---|---|---|
|98|2|1|
|34|3|0|
'''

def solution(num, n):
    return 1 if num % n == 0 else 0

# [[삼항연산자]]를 사용했는데, 파이썬은 타 언어와 사용법이 좀 달랐다.

'''
## 더 좋아 보이는 다른 사람 풀이

```python
def solution(num, n):
    return int(not(num % n))
```

- 불리언을 int형으로 변환하니 1또는 0이된다.
'''