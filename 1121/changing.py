def solution(s):
    cnt = 0
    zero = 0
    while(s != '1'):
        bf = len(s)
        s = s.replace('0', '')
        af = len(s)
        zero += (bf - af)
        s = format(af, 'b')
        cnt += 1
    answer = [cnt, zero]
    return answer

print(solution("1111111"))
