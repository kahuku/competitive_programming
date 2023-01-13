class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColor = image[sr][sc]

        def getNeighbors(i, j):
            neighbors = []
            if i - 1 >= 0 and image[i-1][j] == startColor:
                neighbors.append((i-1,j))
            if i + 1 < len(image) and image[i+1][j] == startColor:
                neighbors.append((i+1,j))
            if j - 1 >= 0 and image[i][j-1] == startColor:
                neighbors.append((i,j-1))
            if j + 1 < len(image[0]) and image[i][j+1] == startColor:
                neighbors.append((i,j+1))
            return neighbors

        neighbors = getNeighbors(sr, sc)
        neighbors.append((sr, sc))
        visited = set()
        while len(neighbors) > 0:
            new_neighbors = []
            for neighbor in neighbors:
                if neighbor not in visited:
                    image[neighbor[0]][neighbor[1]] = color
                    new_neighbors.extend(getNeighbors(neighbor[0], neighbor[1]))
                    visited.add(neighbor)
            neighbors = new_neighbors
        return image

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr = image[sr][sc]
        if curr == color:
            return image
        image[sr][sc] = color

        if sr-1 >= 0 and image[sr-1][sc] == curr:
            self.floodFill(image, sr-1, sc, color)
        if sr+1 < len(image) and image[sr+1][sc] == curr:
            self.floodFill(image, sr+1, sc, color)
        if sc-1 >= 0 and image[sr][sc-1] == curr:
            self.floodFill(image, sr, sc-1, color)
        if sc+1 < len(image[0]) and image[sr][sc+1] == curr:
            self.floodFill(image, sr, sc+1, color)

        return image