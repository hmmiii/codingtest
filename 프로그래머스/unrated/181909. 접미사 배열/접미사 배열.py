def solution(my_string):
    answer = []
    for idx,i in enumerate(my_string):
        answer.append(my_string[idx:])
    answer.sort()
    return answer