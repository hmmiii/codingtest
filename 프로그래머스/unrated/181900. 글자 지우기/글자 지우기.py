def solution(my_string, indices):
    answer = list(my_string)
    for idx, i in enumerate(sorted(indices)):
        del answer[i-idx]
    return ''.join(answer)