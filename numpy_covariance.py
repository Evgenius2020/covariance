import time
import numpy as np


def my_numpy_covariance(signals: np.ndarray):
    n = signals.shape[0]
    m = signals.shape[1]
    means = signals.mean(axis=1).reshape((n, 1))
    means = means.dot(means.transpose())
    res = signals.dot(signals.transpose()) / m - means
    return res


if __name__ == '__main__':
    n, m = 200, 300000
    signals = np.random.random((n, m))

    tic = time.perf_counter()
    np_matrix = my_numpy_covariance(signals)
    toc = time.perf_counter()
    print(f"my_numpy_covariance: {toc - tic:0.4f} seconds")

    tic = time.perf_counter()
    np_cov_matrix = np.cov(signals)
    toc = time.perf_counter()
    print(f"np.cov: {toc - tic:0.4f} seconds")

    diff_matrix = np_cov_matrix - np_matrix
    assert np.abs(diff_matrix).max() < 10 ** -6
