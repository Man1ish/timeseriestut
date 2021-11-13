import stumpy
time_series = [0, 1, 3, 2, 9, 1, 14, 15, 1, 2, 2, 10, 7]
n = len(time_series)
print(time_series[0:2])
print(time_series[4:7])
print(time_series[2:10])

m = 4
i = 0  # starting index for the first subsequence
j = 8  # starting index for the second subsequence

subseq_1 = time_series[i:i+m]
subseq_2 = time_series[j:j+m]

print(subseq_1, subseq_2)

import math

D = 0
for k in range(m):
    D += (time_series[i+k] - time_series[j+k])**2
print(f"The square root of {D} = {math.sqrt(D)}")