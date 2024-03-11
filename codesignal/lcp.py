# Lucid Summer 2024 Intern app
# Given two arrays of integers, return the length of the longest common prefix between any two integers from different arrays
# Ex:
# arr1 = [25, 256, 54567, 2, 54]
# arr2 = [30, 256, 3, 545683, 5]
# Ans: 4 (54567 and 545683 have prefix of 5456)

# TLE
def solution(arr1, arr2):
    arr1 = list(set(arr1))
    arr2 = list(set(arr2))
    longest = 0

    for num1 in arr1:
        num1 = str(num1)
        for num2 in arr2:
            num2 = str(num2)
            for i in range(len(num1)):
                if num1[i] != num2[i]:
                    break
            longest = max(longest, i)
    return longest

# Multithreaded
# Some bugs, didn't finish in time
from threading import Thread
def solution(arr1, arr2):
    def lcp(num1, arr2, d, i):
        longest = 0
        num1 = str(num1)
        for num2 in arr2:
            num2 = str(num2)
            for j in range(len(num1)):
                if num1[j] != num2[j]:
                    break
            longest = max(longest, j)
        d[i] = longest

    arr1 = list(set(arr1))
    arr2 = list(set(arr2))
    d = [0] * len(arr1)
    threads = []
    for i, num1 in enumerate(arr1):
        t = Thread(target=lcp, args=(num1, arr2, d, i))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return max(d)

# Trie solution
def solution(arr1, arr2):
    root = {}
    def addTrieNode(num):
        num = str(num)
        curr = root
        for dig in num:
            if dig not in curr:
                curr[dig] = {}
            curr = curr[dig]

    def countDepth(num):
        depth = 0
        num = str(num)
        curr = root
        for dig in num:
            if dig in curr:
                curr = curr[dig]
                depth += 1
            else:
                break
        return depth
    
    for num in arr1:
        addTrieNode(num)
    
    longest = 0
    for num in arr2:
        longest = max(countDepth(num), longest)

    return longest

print(solution([25, 256, 54567, 2, 54], [30, 256, 3, 545683, 5]))