n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))

pre_sum = [0] * (n + 1)

for i in range(n):
    pre_sum[i + 1] = pre_sum[i] + nums[i]

for i in range(m):
    l, r = list(map(int, input().split()))
    print(pre_sum[r] - pre_sum[l - 1])

