# Lucid Summer 2024 Intern app
# Given a list of git transactions, return the branch with the highest number of changed files
# Ex:
# transactions = [
#    "switch branch1",
#    "commit file1",
#    "commit file2",
#    "switch branch2",
#    "commit file1"]
# Returns:
# "branch1"

from collections import defaultdict
def solution(transactions):
    d = defaultdict(set())
    branch = None
    for t in transactions:
        if t.split()[0] == "switch":
            branch = t.split()[1]
        else:
            d[branch].add(t.split()[1])
    return sorted(d.items(), key=lambda x: len(x[1]), reverse=True)[0][0]