# Lucid Summer 2024 Intern app
# Given a number n, return a box of size n x n with a border of asterisks

def solution(n):
    return ['*' * n] + ['*' + ' ' * (n - 2) + '*' for _ in range(n - 2)] + ['*' * n]