def hourglassSum(arr):
    sums = []
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            val = arr[i][j]+ arr[i][j+1]+ arr[i][j+2] + arr[i+1][j+1] +arr[i+2][j]+ arr[i+2][j+1]+ arr[i+2][j+2]
            sums.append(val)
    return max(sums)
