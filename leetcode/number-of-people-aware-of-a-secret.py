class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        people = [0] * forget
        people.append(1)
        for i in range(1, n):
            people.append(sum([people[forget + i - j] for j in range(delay, forget)]))
        return sum(people[-forget:]) % (10 ** 9 + 7)