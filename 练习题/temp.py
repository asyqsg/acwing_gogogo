n, q = list(map(int, input().split()))
nums = list(map(int, input().split()))


def get_left(nums, k, l, r):
    while l < r:
        mid = (l + r) >> 1
        if nums[mid] >= k:
            r = mid
        else:
            l = mid + 1
    if nums[l] != k:
        return -1
    return l


def get_right(nums, k, l, r):
    while l < r:
        mid = (l + r + 1) >> 1
        if nums[mid] <= k:
            l = mid
        else:
            r = mid - 1
    if nums[r] != k:
        return -1
    return r


if __name__ == '__main__':
    for i in range(q):
        k = int(input())
        res = [get_left(nums, k, 0, n - 1), get_right(nums, k, 0, n - 1)]
        for i in res:
            print(i, end=' ')
