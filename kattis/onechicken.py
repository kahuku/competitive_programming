n, m = map(int, input().split())
if n > m:
    if n - m == 1:
        print("Dr. Chaz needs 1 more piece of chicken!")
    else:
        print("Dr. Chaz needs", n - m, "more pieces of chicken!")
else:
    if m - n == 1:
        print("Dr. Chaz will have 1 piece of chicken left over!")
    else:
        print("Dr. Chaz will have", m - n, "pieces of chicken left over!")