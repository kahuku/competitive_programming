# I liked this solution better but it was TLE

# from sys import stdin
# from functools import lru_cache

# scores = {
#     3: 1,
#     4: 1,
#     5: 2,
#     6: 3,
#     7: 5,
#     8: 11
# }

# dirs = [(0, 1), (-1, 0), (1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.isEnd = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.isEnd = True

# @lru_cache(None)
# def valid(r, c):
#     return 0 <= r < 4 and 0 <= c < 4

# @lru_cache(None)
# def neighbors(r, c):
#     return [(r + x, c + y) for x, y in dirs if valid(r + x, c + y)]

# def boggle(board, words):
#     visited = [[False] * 4 for _ in range(4)]
#     found = set()
#     root = words.root

#     def recurse(r, c, node, currentWord):
#         if visited[r][c]:
#             return
        
#         char = board[r][c]
#         if char not in node.children:
#             return

#         # visit
#         visited[r][c] = True
#         node = node.children[char]
#         currentWord += char

#         if node.isEnd:
#             found.add(currentWord)

#         # search neighbors
#         for nr, nc in neighbors(r, c):
#             recurse(nr, nc, node, currentWord)

#         # post visit cleanup
#         visited[r][c] = False

#     for r in range(4):
#         for c in range(4):
#             recurse(r, c, root, "")
#     return list(found)

# def solve(board, d):
#     words = boggle(board, d)
#     score = 0
#     topScore, topWord = 0, ''
#     for word in words:
#         newScore = scores.get(len(word), 0)
#         score += newScore
#         if newScore > topScore:
#             topWord = word
#             topScore = newScore
#         elif newScore == topScore:
#             topWord = min(word, topWord)
#     return f"{score} {topWord} {len(words)}"
    

# lines = [line.strip() for line in stdin.readlines()]
# trie = Trie()
# i = 0
# for j in range(int(lines[0])):
#     trie.insert(lines[j + 1])
# i += j + 3
# n = int(lines[i])
# for j in range(n):
#     board = [list(lines[i + j + k]) for k in range(1, 5)]
#     i += 4
#     print(solve(board, trie))



from sys import stdin

# Scoring rules for words of different lengths
scores = {
    3: 1,
    4: 1,
    5: 2,
    6: 3,
    7: 5,
    8: 11
}

# Directions for 8 possible moves in a 2D grid (up, down, left, right, and diagonals)
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search_prefix(self, prefix):
        """Searches for a given prefix in the Trie and returns the last node reached or None if not found."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

def is_valid(r, c):
    """Check if a given row and column are within the bounds of the board."""
    return 0 <= r < 4 and 0 <= c < 4

def boggle(board, trie):
    found = set()  # Set to store found words and prevent duplicates
    visited = [[False] * 4 for _ in range(4)]  # Track visited cells in the board

    def recurse(r, c, node, currentWord):
        if visited[r][c]:
            return

        char = board[r][c]
        if char not in node.children:
            return

        # Mark this node as visited
        visited[r][c] = True
        node = node.children[char]
        currentWord += char

        # If it's a complete word, add to found
        if node.isEnd:
            found.add(currentWord)

        # Recurse to all valid neighbors
        for dx, dy in dirs:
            nr, nc = r + dx, c + dy
            if is_valid(nr, nc):
                recurse(nr, nc, node, currentWord)

        # Backtrack: unmark the visited cell
        visited[r][c] = False

    # Start DFS from each cell on the board
    for r in range(4):
        for c in range(4):
            recurse(r, c, trie.root, "")

    return list(found)

def solve(board, trie):
    words = boggle(board, trie)
    score = 0
    longest_word = ""
    num_words_found = len(words)

    # Calculate score and determine the longest word
    for word in words:
        word_score = scores.get(len(word), 0)
        score += word_score
        if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
            longest_word = word

    return f"{score} {longest_word} {num_words_found}"

lines = [line.strip() for line in stdin.readlines()]
trie = Trie()
i = 0
for j in range(int(lines[0])):
    trie.insert(lines[j + 1])
i += j + 3
n = int(lines[i])
for j in range(n):
    board = [list(lines[i + j + k]) for k in range(1, 5)]
    i += 4
    print(solve(board, trie))