def bfs(matrix):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):
        queue = [(i, j)]

        while queue:
            curr_i, curr_j = queue.pop(0)

            if not (curr_i, curr_j) in visited:
                visited.add((curr_i, curr_j))

                # Traverse neighbors.
                for dir_i, dir_j in directions:
                    next_i, next_j = i + dir_i, j + dir_j

                    if 0 <= next_i < rows and 0 <= next_j < cols:
                        # Add in question-specific checks, where relevant.
                        queue.append((next_i, next_j))

    for i in range(rows):
        for j in range(cols):
            traverse(i, j)