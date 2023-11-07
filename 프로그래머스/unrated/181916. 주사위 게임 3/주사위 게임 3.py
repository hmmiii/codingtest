def solution(a, b, c, d):
    tmp = str(a)+str(b)+str(c)+str(d)
    an, bn, cn, dn = tmp.count(str(a)), tmp.count(str(b)), tmp.count(str(c)), tmp.count(str(d))
    answer = 0
    if max(an,bn,cn,dn) == 4:
        answer = 1111 * a
    elif max(an,bn,cn,dn) == 3:
        p = int([x for x in tmp if tmp.count(str(x)) == 3][0])
        q = int([x for x in tmp if tmp.count(str(x)) == 1][0])
        print(p,q)
        answer = (10 * p + q)**2
    elif min(an,bn,cn,dn) == 2 and max(an,bn,cn,dn) == 2:
        p, q = list(set([a, b, c, d]))[:2]
        answer = (p + q) * (abs(p - q))
    elif max(an,bn,cn,dn) == 2 and min(an,bn,cn,dn) == 1:
        p = int([x for x in tmp if tmp.count(str(x)) == 2][0])
        qnr = set([a,b,c,d])
        qnr.discard(p)
        q, r = map(int, list(qnr))
        answer = q * r        
    elif max(an,bn,cn,dn) == 1:
        answer = min(a,b,c,d)
    return answer