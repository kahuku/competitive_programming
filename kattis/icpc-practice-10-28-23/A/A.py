from sys import stdin
from collections import defaultdict

def parse_facts(line):
    facts = []
    curr = ''
    for c in line:
        if c == ' ': continue
        curr += c
        if c == ')':
            facts.append(curr)
            curr = ''
            continue
    return facts

def eval_query(query, facts):
    name = query.split('(')[0]
    args = query.split('(')[1][:-1]
    args = args.split(',')
    facts_list = facts[name][len(args)]
    out = 0
    for fact in facts_list:
        if comp(args, fact):
            out += 1
    return out

def comp(query_args, fact_args):
    d = {}
    valid = True
    for i in range(len(query_args)):
        if query_args[i] == '_':
            continue
        elif query_args[i][0] == '_':
            # variable
            if query_args[i] in d:
                if d[query_args[i]] != fact_args[i]: return False
            else:
                d[query_args[i]] = fact_args[i]
        else:
            if query_args[i] != fact_args[i]: return False
    return valid

raw = stdin.readlines()
facts_list = []
query_list = []
found = False
for line in raw:
    if line == '\n':
        found = True
        continue
    if not found:
        # facts
        facts_list = facts_list + parse_facts(line)
    else:
        # queries
        query_list = query_list + parse_facts(line)
    
facts = defaultdict(lambda: defaultdict(list))
for fact in facts_list:
    name = fact.split('(')[0]
    args = fact.split('(')[1][:-1]
    args = args.split(',')
    facts[name][len(args)].append(args)

out = []

for query in query_list:
    out.append(eval_query(query, facts))

for line in out:
    print(line)