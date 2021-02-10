def average_contiguous_subarrays(k, arr):
    windowSt, windowSu = 0, 0.0
    result = []

    for windowE in range(len(arr)):
        windowSu += arr[windowE]

        if windowE >= k-1:
            result.append(windowSu/k)
            windowSu -= arr[windowSt]
            windowSt += 1
    return result


arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
print(average_contiguous_subarrays(5,arr))
