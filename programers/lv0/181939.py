'''
문제 : 181939 - 더 크게합치기
날짜 : 2023-11-03 16:04
## 문제
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

- 12 ⊕ 3 = 123
- 3 ⊕ 12 = 312

양의 정수 `a`와 `b`가 주어졌을 때, `a` ⊕ `b`와 `b` ⊕ `a` 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.

단, `a` ⊕ `b`와 `b` ⊕ `a`가 같다면 `a` ⊕ `b`를 return 합니다.

### 제한사항
- 1 ≤ `a`, `b` < 10,000

### 입출력 예
|a|b|result|
|---|---|---|
|9|91|991|
|89|8|898|
'''

def solution(a, b):
    a, b = map(str, (a,b))
    ab = a+b
    ba = b+a
    answer = ''
    if int(ab) > int(ba):
        answer = ab
    elif int(ba) > int(ab):
        answer = ba
    else:
        answer = ab
    return answer

'''
## 더 좋아 보이는 다른 사람 풀이

```python
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))
```
'''