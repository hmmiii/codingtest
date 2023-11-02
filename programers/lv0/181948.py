'''
문제 : 181948 - 특수문자 출력하기
날짜 : 2023-11-02 20:39
## 문제
다음과 같이 출력하도록 코드를 작성해 주세요.

### 제한사항


### 입출력 예
#### 입력
```

```
#### 출력
```
!@#$%^&*(\'"<>?:;
```
'''

print(r'!@#$%^&*(\'"<>?:;')

'''
1. - " \<- 큰따옴표에 백슬래시를 추가
2. r'' 안에 입력하면 특수문자 뭐든 된다.

1번 방법 사용 시 : 백슬래시를 추가해 주어야 하는 특수문자

print("\n") //줄바꿈
print("\t") //수평 탭(Tab)
print("\\") // \ 백슬래시
print("\"") // " 큰 따옴표
print("\'") // ' 작은 따옴표

'''