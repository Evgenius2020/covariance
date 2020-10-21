def covariance(x, y):
    assert len(x) == len(y)
    mx = sum(x) / len(x)
    my = sum(y) / len(y)
    return sum([x[i] * y[i] for i in range(len(x))]) / len(x) - mx * my


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

    seq = matrix[0]
    seq_mean = sum(seq) / n
    seq_variance = sum([(seq[i] - seq_mean) ** 2 for i in range(n)]) / n
    assert abs(seq_variance - covariance(seq, seq)) < 10 ** -10

    for row in range(n):
        for column in range(n):
            if column < row:
                continue
            assert matrix[row][column] == matrix[column][row]
