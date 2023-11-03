def solution(a, b):
    a, b = map(str, (a,b))
    ab = a+b
    ba = b+a
    answer = ''
    if int(ab) > int(ba):
        answer = int(ab)
    elif int(ba) > int(ab):
        answer = int(ba)
    else:
        answer = int(ab)
    return answer