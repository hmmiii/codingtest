'''
문제 : 181940 - 문자열 곱하기
날짜 : 2023-11-03 15:51
## 문제
문자열 `my_string`과 정수 `k`가 주어질 때, `my_string`을 `k`번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.

### 제한사항
- 1 ≤ `my_string`의 길이 ≤ 100
- `my_string`은 영소문자로만 이루어져 있습니다.
- 1 ≤ `k` ≤ 100

### 입출력 예

|my_string|k|result|
|---|---|---|
|"string"|3|"stringstringstring"|
|"love"|10|"lovelovelovelovelovelovelovelovelovelove"|
'''

def solution(my_string, k):
    return my_string * k

'''
## 더 좋아 보이는 다른 사람 풀이

```python
동일하다 NICE !
```
'''