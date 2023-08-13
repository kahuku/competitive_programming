# Goldman Sachs 2024 summer intern app
# given list of ints, find how many pairs of ints have an absolute difference of t

def abs_diff_2_sum(arr, t):
    count = 0
    s = set()
    for num in arr:
        if num - t in s:
            count += 1
        s.add(num)
    return count