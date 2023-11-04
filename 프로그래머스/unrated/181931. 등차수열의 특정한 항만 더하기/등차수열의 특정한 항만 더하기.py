def solution(a, d, included):
    answer = 0
    for idx, i in enumerate(included):
        degree = idx + 1
        term = a + (degree - 1) * d
        if i:
            answer+=term
    return answer