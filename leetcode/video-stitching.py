class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x: (x[0], -1 * x[1]))
        reached, possible_ends, ans = 0, set(), 0
        while clips:
            while clips and clips[0][1] <= reached: clips.pop(0)
            while clips and clips[0][0] <= reached: possible_ends.add(clips.pop(0)[1])

            if not possible_ends: return -1
            reached = max(possible_ends)
            ans += 1
            if reached >= time: return ans
            possible_ends.clear()
        
        return -1