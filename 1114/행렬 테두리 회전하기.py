def solution(rows, columns, queries):
    matrix = [ [i+k * columns for i in range(1, columns+1)] for k in range(rows) ]
    answer = []
    for x1,y1,x2,y2 in queries:
        compare = matrix[x1-1][y1-1]
        minValue = compare

        for k in range(x1-1,x2-1):
            i = matrix[k+1][y1-1]
            matrix[k][y1-1] = i
            minValue = min(minValue, i)

        for k in range(y1-1,y2-1):
            i = matrix[x2-1][k+1]
            matrix[x2-1][k] = i
            minValue = min(minValue, i)

        for k in range(x2-1,x1-1,-1):
            i = matrix[k-1][y2-1]
            matrix[k][y2-1] = i
            minValue = min(minValue, i)

        for k in range(y2-1,y1-1,-1):
            i = matrix[x1-1][k-1]
            matrix[x1-1][k] = i
            minValue = min(minValue, i)

        matrix[x1-1][y1] = compare
        answer.append(minValue)

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))