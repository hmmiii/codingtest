def solution(num_list):
    sum_num = 0
    mul_num = 1
    for i in num_list:
        sum_num += i
        mul_num *= i

    sum_num **= 2
    
    if mul_num < sum_num:
        return 1
    else:
        return 0