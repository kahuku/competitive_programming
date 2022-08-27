f_correct, my_answers, friend_answers = int(input()), input(), input()
num_questions = len(my_answers)
samesies = sum(a == b for a, b in zip(my_answers, friend_answers))
if samesies >= f_correct:
    print(num_questions - (samesies - f_correct))
else:
    print(num_questions - (f_correct - samesies))