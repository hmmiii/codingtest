def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        n  = 0 
        if len(i[s:s+l]):
            n = int(''.join([x for x in i[s:s+l]]))
        if n > k:
            answer.append(n)
    return answer