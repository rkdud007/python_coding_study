def solution(numbers):
    answer = 0
    nl = [0,1,2,3,4,5,6,7,8,9]
    for i in range(len(numbers)):
        if numbers[i] in nl:
            nl.remove(numbers[i])
    answer = sum(nl)
    return answer