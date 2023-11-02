'''
문제 : 181943 - 문자열 겹쳐쓰기
날짜 : 2023-11-02 22:12
## 문제
문자열 `my_string`, `overwrite_string`과 정수 `s`가 주어집니다. 문자열 `my_string`의 인덱스 `s`부터 `overwrite_string`의 길이만큼을 문자열 `overwrite_string`으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

### 제한사항
- `my_string`와 `overwrite_string`은 숫자와 알파벳으로 이루어져 있습니다.
- 1 ≤ `overwrite_string`의 길이 ≤ `my_string`의 길이 ≤ 1,000
- 0 ≤ `s` ≤ `my_string`의 길이 - `overwrite_string`의 길이

### 입출력 예
|my_string|overwrite_string|s|result|
|---|---|---|---|
|"He11oWor1d"|"lloWorl"|2|"HelloWorld"|
|"Program29b8UYP"|"merS123"|7|"ProgrammerS123"|
'''

def solution(my_string, overwrite_string, s):
    answer = my_string[0:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer

print(solution("He11oWor1d", "lloWorl", 0))

'''
## 더 좋아 보이는 다른 사람 풀이

```python
def solution(my_string, overwrite_string, s):
	return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
```
'''