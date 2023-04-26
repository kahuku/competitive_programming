class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        biggest, smallest = len(people) - 1, 0
        people.sort()
        boats = 0
        used = 0
        while used < len(people) and smallest <= biggest:
            cap = people[biggest]
            used += 1
            print("Used", people[biggest])
            if cap < limit:
                if people[smallest] <= limit - cap:
                    print("used", people[smallest])
                    used += 1
                    smallest += 1
            biggest -= 1
            boats += 1
            print()

        return boats