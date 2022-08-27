n = input()


for i in range(int(n)):
    problem = input()
    if (problem == "P=NP"):
        print("skipped")
    else:
        prob = problem.split('+')
        result = int(prob[0]) + int(prob[1])
        print(result)
    
