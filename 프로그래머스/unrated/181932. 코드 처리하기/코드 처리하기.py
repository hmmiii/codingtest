def solution(code):
    mode = 0
    rat = ''
    for idx, i in enumerate(code):
        if mode == 0:
            if i != '1':
                if not(idx % 2):
                    rat += i
            else:
                mode = 1
        else:
            if i != '1':
                if idx % 2:
                    rat += i
            else:
                mode = 0  
    
    if rat:
        return rat
    else:
        return "EMPTY"