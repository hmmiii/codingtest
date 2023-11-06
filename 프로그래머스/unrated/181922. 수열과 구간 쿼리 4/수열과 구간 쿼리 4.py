def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s,e+1):
            if k == 0:
                arr[i] +=0
            else:
                arr[i] = arr[i] + 1 if not(i%k) else arr[i] + 0
    return arr