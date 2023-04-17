# [0, 2, 3] #index array (d[1])
# [0, 2, 5] prefix array
# []

## NOTHING WORKING SO FAR 

|0 - 2| + |0 - 3| = 5
|2 - 0| + |2 - 3| = 3
|3 - 0| + |3 - 2| = 4

|0 - 0| + |0 - 2| + |0 - 3| = 5
|2 - 0| + |2 - 2| + |2 - 3| = 3
|3 - 0| + |3 - 2| + |3 - 3| = 4

from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        
        #prefix each mini array?

        out = []
        for i in range(len(nums)):
            num = nums[i]
            other_indexes = d[num]
            if len(other_indexes) == 1:
                out.append(0)
                continue
            out.append(sum([abs(i - ind) for ind in other_indexes]))

        return out
    

from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        
        prefixes = defaultdict(list)
        postfixes = defaultdict(list)
        indexes = {}

        for key in d.keys():
            arr, arr2 = d[key], d[key]

            for i in range(1, len(arr)):
                arr[i] += arr[i - 1]
            prefixes[key] = arr

            # post = [[0] for i in range(len(arr2))]
            # post[-1] = arr2[-1]
            # for i in range(len(arr2) - 2, -1, -1):
            #     post[i] = post[i + 1] + arr2[i]
            post = list(accumulate(arr2[::-1], operator.add))[::-1]
            postfixes[key] = post

            indexes[key] = 0
            print(key, prefixes[key], postfixes[key])
        
        out = []
        for i in range(len(nums)):
            num = nums[i]
            other_indexes = d[num]
            if len(other_indexes) < 2:
                out.append(0)
                continue

            pre = prefixes[num]
            post = postfixes[num]
            num_left = indexes[num]
            other_index = indexes[num]
            indexes[num] += 1
            num_right = len(other_indexes) - 1 - num_left
            s = 0
            s += abs(pre[other_index - 1] - other_indexes[other_index] * num_left) if other_index != 0 else 0
            s += abs(post[other_index + 1] - other_indexes[other_index] * num_right) if other_index != len(other_indexes) - 1 else 0
            out.append(s)

        return out