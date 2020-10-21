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

    avg_my_time = 0
    avg_np_time = 0
    test_repeats = 10
    for test_repeat in range(test_repeats):
        tic = time.perf_counter()
        my_cov_matrix = my_numpy_covariance(signals)
        toc = time.perf_counter()
        avg_my_time += toc - tic

        tic = time.perf_counter()
        np_cov_matrix = np.cov(signals)
        toc = time.perf_counter()
        avg_np_time += toc - tic

        diff_matrix = np_cov_matrix - my_cov_matrix
        assert np.abs(diff_matrix).max() < 10 ** -6
        print(f"test repeat: {test_repeat + 1}")

    avg_my_time /= test_repeats
    avg_np_time /= test_repeats
    print(f"my_numpy_covariance: {avg_my_time:0.4f} seconds")
    print(f"np.cov: {avg_np_time:0.4f} seconds")
