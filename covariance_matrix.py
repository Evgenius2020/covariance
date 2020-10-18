from covariance import covariance


def covariance_matrix(signals):
    matrix_size = len(signals)
    matrix = [[0] * matrix_size for _ in range(matrix_size)]
    for row in range(matrix_size):
        for column in range(matrix_size):
            if column >= row:
                matrix[row][column] = covariance(signals[row], signals[column])
            else:
                matrix[row][column] = matrix[column][row]
    return matrix


if __name__ == '__main__':
    n, m = 50, 5000
    signals = [[(i + 1) / (j + 1) for j in range(m)] for i in range(n)]
    matrix = covariance_matrix(signals)
    assert len(matrix) == n
    assert max(map(len, matrix)) == min(map(len, matrix)) == n
    for row in range(n):
        for column in range(n):
            if column < row:
                continue
            assert matrix[row][column] == matrix[column][row]
