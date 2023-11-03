'''
문제 : 181942 - 문자열 섞기
날짜 : 2023-11-03 15:42
## 문제
길이가 같은 두 문자열 `str1`과 `str2`가 주어집니다.

두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.

### 제한사항
- 1 ≤ `str1`의 길이 = `str2`의 길이 ≤ 10
    - `str1`과 `str2`는 알파벳 소문자로 이루어진 문자열입니다.

### 입출력 예

|str1|str2|result|
|---|---|---|
|"aaaaa"|"bbbbb"|"ababababab"|
'''

def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i]
        answer += str2[i]
    return answer

'''
## 더 좋아 보이는 다른 사람 풀이

```python
def solution(str1, str2):
    answer = ''
    for i in range(0,len(str1)):
        answer = answer + str1[i] + str2[i]
    return answer
```

- 한 줄로 처리했다. 나와 비슷.

'''