'''
문제 : 181933 - flag에 따라 다른 값 반환하기
날짜 : 2023-11-03 17:37
## 문제
두 정수 `a`, `b`와 boolean 변수 `flag`가 매개변수로 주어질 때, `flag`가 true면 `a` + `b`를 false면 `a` - `b`를 return 하는 solution 함수를 작성해 주세요.

### 제한사항
- -1,000 ≤ `a`, `b` ≤ 1,000

### 입출력 예
|a|b|flag|result|
|---|---|---|---|
|-4|7|true|3|
|-4|7|false|-11|
'''

def solution(a, b, flag):
    return a+b if flag else a-b