def solution(my_string):
    answer = []
    upper = []
    lower = []
    
    for i in range(65,91):
        num = 0
        for str in my_string:
            if i == ord(str):
                num += 1
        upper.append(num)
    
    for i in range(97,123):
        num = 0
        for str in my_string:
            if i == ord(str):
                num += 1
        lower.append(num)
    
    answer = upper + lower
    
    
    return answer