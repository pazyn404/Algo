from bisect import bisect_left


# find count of subarrays such that sum equals given
def count1(l: list[int], target: int) -> int:
    res = 0
    #
    curr_sum = 0
    d = {0: 1}

    for num in l:
        curr_sum += num
        res += d.get(curr_sum - target, 0)
        d[curr_sum] = d.get(curr_sum, 0) + 1
    #
    return res


# find count of subarrays such that every has given length and sum equals given
def count2(l: list[int], target: int, sub_len: int) -> int:
    res = 0
    #
    curr_sum = 0
    d = {(-1, 0): 1}

    for i, num in enumerate(l):
        curr_sum += num
        res += d.get((i - sub_len, curr_sum - target), 0)
        d[(i, curr_sum)] = 1
    #
    return res


def helper(l: list[int], pos: int, sub_range: int) -> int:
    new_pos = bisect_left(l, pos - sub_range)
    return len(l) - new_pos


# find count of subarrays such that every has length in given range and sum equals given
def count3(l: list[int], target: int, sub_range: int) -> int:
    res = 0
    #
    curr_sum = 0
    d = {0: [0]}

    for i, num in enumerate(l):
        curr_sum += num
        res += helper(d.get(curr_sum - target, []), i, sub_range)
        if curr_sum in d:
            d[curr_sum].append(i)
        else:
            d[curr_sum] = [i]
    #
    return res


print(count1([3, 1, 3, 1, 2, 2, 3, 1, 1, 1, 1], 4))
print(count2([3, 1, 3, 1, 2, 2, 3, 1, 1, 1, 2], 4, 2))
print(count3([3, 1, 3, 1, 2, 2, 3, 1, 1, 1, 1], 4, 3))
