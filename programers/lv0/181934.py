'''
문제 : 181934 - 조건 문자열
날짜 : 2023-11-03 17:33
## 문제
문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.

- 두 수가 `n`과 `m`이라면
    - ">", "=" : `n` >= `m`
    - "<", "=" : `n` <= `m`
    - ">", "!" : `n` > `m`
    - "<", "!" : `n` < `m`

두 문자열 `ineq`와 `eq`가 주어집니다. `ineq`는 "<"와 ">"중 하나고, `eq`는 "="와 "!"중 하나입니다. 그리고 두 정수 `n`과 `m`이 주어질 때, `n`과 `m`이 `ineq`와 `eq`의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.

### 제한사항
- 1 ≤ `n`, `m` ≤ 100

### 입출력 예
|ineq|eq|n|m|result|
|---|---|---|---|---|
|"<"|"="|20|50|1|
|">"|"!"|41|78|0|
'''

def solution(ineq, eq, n, m):
    answer = 0
    oper = ineq+eq.replace('!','')
    if oper == '>=':
        if n >= m:
            answer = 1
    elif oper == '<=':
        if n <= m:
            answer = 1
    elif oper == '>':
        if n > m:
            answer = 1
    elif oper == '<':
        if n < m:
            answer = 1
    return answer

'''
## 더 좋아 보이는 다른 사람 풀이

```python
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))
```

- eval 함수로 문자열을 받아 계산식을 수행할 수 있다.
'''