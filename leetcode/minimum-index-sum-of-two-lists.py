class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m1, m2 = {}, {}
        for i, item in enumerate(list1):
            m1[item] = i
        for i, item in enumerate(list2):
            m2[item] = i
        shared = set(list1).intersection(set(list2))
        out = []
        m = math.inf
        for item in shared:
            if m1[item] + m2[item] < m:
                m = m1[item] + m2[item]
                out = [item]
            elif m1[item] + m2[item] == m:
                out.append(item)
        return out