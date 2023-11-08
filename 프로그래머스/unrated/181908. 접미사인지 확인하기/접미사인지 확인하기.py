def solution(my_string, is_suffix):
    answer = 0
    arr = []
    for idx, i in enumerate(my_string):
        arr.append(my_string[idx:])
    answer = 1 if any(x == is_suffix for x in arr) else 0
    return answer