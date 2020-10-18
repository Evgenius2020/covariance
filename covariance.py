def covariance(x, y):
    assert len(x) == len(y)
    mx = sum(x) / len(x)
    my = sum(y) / len(y)
    return sum([x[i] * y[i] for i in range(len(x))]) / len(x) - mx * my


if __name__ == '__main__':
    n = 1000
    assert covariance([1 for i in range(n)], [0 for i in range(n)]) == 0
    seq = [1 / (i + 1) for i in range(n)]
    seq_mean = sum(seq) / n
    seq_variance = sum([(seq[i] - seq_mean) ** 2 for i in range(n)]) / n
    assert abs(seq_variance - covariance(seq, seq)) < 10 ** -10
