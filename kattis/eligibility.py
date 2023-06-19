for _ in range(int(input())):
    name, post, birth, courses = input().split()
    post = int(post.split('/')[0])
    birth = int(birth.split('/')[0])
    courses = int(courses)

    if post >= 2010 or birth >= 1991:
        print(name, 'eligible')
    elif courses > 5 * 8:
        print(name, 'ineligible')
    else:
        print(name, 'coach petitions')