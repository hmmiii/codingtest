def solution(num_list):
    even = ''.join([str(n) for n in num_list if n % 2 == 0])
    odd = ''.join([str(n) for n in num_list if n % 2 != 0])
    return eval(f'{even} + {odd}')