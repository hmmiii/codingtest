def solution(arr, idx):
    answer = -1
    for index, i in enumerate(arr[idx:]):
        print(index)
        if i == 1:
            answer = index+idx
            break
        else:
            continue
    return answer