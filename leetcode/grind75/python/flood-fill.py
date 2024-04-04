# 2d Array, BFS

class Solution:
    # O(n) time | O(n) space
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirs = [1, 0, -1, 0, 1]
        q = [(sr, sc)]
        visited = set()
        while q:
            r, c = q.pop()
            visited.add((r, c))
            for i, j in zip(dirs, dirs[1:]):
                nr, nc = r + i, c + j
                if (nr, nc) not in visited and 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == image[r][c]:
                    q.append((nr, nc))
            image[r][c] = color
        return image