def online_mean(avg, size, data):
    '''Extend a previously computed average with new data.

    Arguments:
        avg: The old mean.
        size: The old size.
        data: The new data.
    '''
    if len(data) == 0:
        return avg

    next = data[0]
    size = size + 1
    avg = avg + (next - avg) / size

    return online_mean(avg, size, data[1:])
