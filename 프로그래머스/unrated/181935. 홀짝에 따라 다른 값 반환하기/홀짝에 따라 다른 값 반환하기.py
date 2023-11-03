def solution(n):
    answer = 0
    if not(n % 2):
        for i in range(1, n+1):
            answer = answer + i**2 if not(i % 2) else answer + 0
    else:
        for i in range(1, n+1):    
            answer = answer + i if i % 2 else answer + 0
    return answer