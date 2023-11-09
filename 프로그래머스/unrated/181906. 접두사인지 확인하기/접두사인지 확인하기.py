def solution(my_string, is_prefix):
    answer = 0
    for idx,str in enumerate(my_string):
        if my_string[:idx] == is_prefix:
            answer = 1
        else:
            pass
    return answer