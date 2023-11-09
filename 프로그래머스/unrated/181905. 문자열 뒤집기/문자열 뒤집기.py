def solution(my_string, s, e):
    reverse_txt = ''.join(reversed(my_string[s:e+1]))
    return my_string[:s] + reverse_txt + my_string[e+1:]