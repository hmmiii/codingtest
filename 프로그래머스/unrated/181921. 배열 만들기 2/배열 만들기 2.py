def solution(l, r):
    answer = []
    for i in range(l,r+1):
        for j in str(i):
            tmp = ''
            if j == '0' or j == '5':
                continue
            else:
                break
        else:
            answer.append(i)

    if not(answer):
        answer.append(-1)
    return answer
            