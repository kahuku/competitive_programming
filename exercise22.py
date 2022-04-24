
"""
with open('onion_articles.txt','r') as open_file:
    all_text = open_file.read()
    print(all_text)
"""

with open('onion_articles.txt','r') as open_file:
    line = open_file.readline()
    while line:
        print(line)
        line = open_file.readline()
