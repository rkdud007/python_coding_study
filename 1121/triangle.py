def solution(n):
    answer =[]
    end = n * (n + 1) / 2
    cnt= n-1
    blank = [range(n+1,end+1,1)]
    print(blank)
    for i in range(1,n+1,1):
        answer.append([i])

    new = blank[0:cnt+1]
    print(f"new = {new}")
    direction =1

    # while(cnt >0):
    #     if (direction % 3) == 1:
    #
    #
    #     elif (direction % 3) == 2:
    #         answer[n].insert(blank[:cnt+1])
    #
    #
    #     elif (direction % 3) ==0 :
    #
    #
    #     cnt -= 1
    #     direction += 1

    return answer

print(solution(4))

