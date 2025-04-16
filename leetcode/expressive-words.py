class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def compress(s):
            l, c = [], []
            for ch in s:
                if not l or ch != l[-1]:
                    l.append(ch)
                    c.append(1)
                else:
                    c[-1] += 1
            return l, c

        def check(sl, sc, q):
            ql, qc = compress(q)
            if sl != ql:
                return False
            for i in range(len(sc)):
                if sc[i] < 3 and sc[i] != qc[i]:
                    return False
                if sc[i] >= 3 and sc[i] < qc[i]:
                    return False
            return True

        sl, sc = compress(s)
        return sum([check(sl, sc, word) for word in words])