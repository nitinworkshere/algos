def pascal_triange(line):
    arr = [[0 for _ in len(line)] for _ in range(len(line))]
    for line in range(line):
        for i in range(line+1):
            if i == 0 or i == line:
                arr[line][i] = 1
            else:
                arr[line][i] = arr[line-1][i]+arr[line-1][i-1]



