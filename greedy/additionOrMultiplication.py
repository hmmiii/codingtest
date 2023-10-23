# 첫째 줄에 여러 개의 숫자로 구성된 문자열 S가 주어집니다. (1 <= S의 길이 <= 20)
# 첫째 줄에 만들 수 있는 가장 큰 수를 출력합니다.

# 1. 숫자를 왼쪽에서 오른쪽으로 연산해가며 가장 큰 수를 만든다.
# 2. 이때 덧셈 또는 곱셈을 선택할 수 있는데, 일반적으로 덧셈보다는 곱셈이 더 큰 수를 만든다.
# 3. 하지만, 0과의 연산의 경우 곱셈을 할 시 0이 되므로 이 때에는 덧셈을 해야 한다.
# 4. 또한 1과의 연산의 경우에도 곱셈보다 덧셈이 더 큰 값이므로 이 때에는 덧셈을 해야 한다.
# 5. 즉, 1 이하의 수와의 연산인 경우 덧셈을 한다.


### 나의 풀이
# data = input()
# result = 0
# for i in range(len(data)):
#     if data[i] <= '1' or result <= 1:
#         result += int(data[i])
#     else:
#         result *= int(data[i])

# print(result)

### 책 풀이
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중 하나라도 '0' 혹은 '1'인 경우, 곱하기 보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)