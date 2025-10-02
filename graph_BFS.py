def bfs(matrix):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def bfs(row, col):
        queue = [(row, col)]
        visited.add((row, col))

        while queue:
            node_r, node_c = queue.pop(0)

            # Traverse neighbors.
            for dir_r, dir_c in directions:
                next_r, next_c = node_r + dir_r, node_c + dir_c

                if 0 <= next_r < rows and 0 <= next_c < cols:
                    # Add in question-specific checks, where relevant.
                    queue.append((next_r, next_c))
                    visited.add((next_r, next_c))

    for row in range(rows):
        for col in range(cols):
            bfs(row, col)