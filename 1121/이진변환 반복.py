def solution(s):
    ctn = 0
    result = 0
    round_num = 0
    while True:
        round_num+=1
        ctn = 0
        for i in s:
            if i == "1":
                ctn +=1
            else:
                result += 1
        output = str(bin(ctn))[2:]
        s = output
        if output == "1":
            break

    return [round_num, result]

print(solution("110010101001"))