def solution(ineq, eq, n, m):
    answer = 0
    oper = ineq+eq.replace('!','')
    if oper == '>=':
        if n >= m:
            answer = 1
    elif oper == '<=':
        if n <= m:
            answer = 1
    elif oper == '>':
        if n > m:
            answer = 1
    elif oper == '<':
        if n < m:
            answer = 1
    return answer