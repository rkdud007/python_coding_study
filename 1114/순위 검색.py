def solution(info, query):
    answer = []
    info_re = []
    for i in info:
        info_re.append(i.split(" "))
    for k in query:
        match = k.split(' ')
        for i in match:
            if i != 'and' or i != '-':
                for m in info_re:
                    

    print(info_re)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])