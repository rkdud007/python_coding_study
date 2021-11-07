def solution(sizes):
    max_a = 0
    max_b = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            blank = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = blank
    max_a = max(a[0] for a in sizes)
    max_b = max(a[1] for a in sizes)
    return max_a * max_b
