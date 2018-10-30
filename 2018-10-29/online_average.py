def online_mean(avg, size, data):
    '''Extend a previously computed average with new data.

    Arguments:
        avg: The old mean.
        size: The old size.
        data: The new data.

    Returns:
        The updated average.
    '''
    if len(data) == 0:
        return avg

    old_sum = avg * size
    new_sum = old_sum + sum(data)
    new_size = size + len(data)
    new_avg = new_sum / new_size

    return new_avg



def online_mean_stable(avg, size, data):
    '''Extend a previously computed average with new data.

    This version has better numerical stability by using Welfords method.

    To explain numerical stability, consider the usual formula for a mean:
    ``mean(data) = sum(data) / len(data)``. In this case, each element of
    the data may be small, and thus the mean will be small, but the intermediate
    sum could be huge if the dataset is huge. If the sum is huge, the result
    could suffer from rounding error or overflow. Numerical stability is a
    property of algorithms where the intermediate computations are always
    within an acceptable neighborhood of the inputs and final result.

    Welfords method maintains numerical stability by updating the average one
    element at a time.

    See:
        https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_Online_algorithm
        https://en.wikipedia.org/wiki/Numerical_stability#Stability_in_numerical_linear_algebra

    Arguments:
        avg: The old mean.
        size: The old size.
        data: The new data.

    Returns:
        The updated average.
    '''
    if len(data) == 0:
        return avg

    next = data[0]
    size = size + 1
    avg = avg + (next - avg) / size

    return online_mean_better(avg, size, data[1:])
