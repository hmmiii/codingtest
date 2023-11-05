def solution(numLog):
    key = dict(zip([1,-1,10,-10], ['w','s','d','a']))
    answer = ''
    for i in range(1, len(numLog)):
        answer += key[int(numLog[i] - numLog[i-1])]
    return answer