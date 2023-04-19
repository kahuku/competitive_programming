from collections import defaultdict
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def convert(time):
            hrs, mins = time.split(":")
            return 60 * int(hrs) + int(mins)
        
        swipes = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            swipes[name].append(convert(time))

        violators = []
        for person, times in list(swipes.items()):
            if len(times) < 3:
                continue
            times.sort()
            for i in range(2, len(times)):
                if times[i] - times[i - 2] <= 60:
                    violators.append(person)
                    break
        
        return sorted(violators)