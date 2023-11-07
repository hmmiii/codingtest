def solution(x1, x2, x3, x4):
    g1,g2,answer = False, False, False
    if x1 or x2:
        g1 = True
    if x3 or x4:
        g2 = True
    if g1 and g2:
        answer = True
    return answer