def solution(n):
    answer = [[[] for _ in range(i) ]for i in range(1,n+1)]
    num = 1
    for i in range(n):
        if i %3 == 0:
            for k in range(n-i):
                answer[k+i//3*2][i//3] = num
                num+=1
        elif i % 3 ==1:
            for k in range(n-i):
                answer[n-1-i//3][i//3+k+1] = num
                num+=1
        elif i % 3== 2:
            for k in range(n-i):
                answer[n-k-2-i//3][n-k-2-(i//3)*2] = num
                num+=1
    final = []
    for i  in answer:
        final += i
    return final

n = int(input())
print(solution(n))

