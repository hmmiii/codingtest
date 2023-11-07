def solution(my_string, queries):
    answer = my_string
    for s,e in queries:
        rev = ''.join(reversed(answer[s:e+1]))
        answer = answer[:s] + rev + answer[e+1:]
    return answer