def colors(arr):
    counts = {}

    # Count 'em up
    for color in arr:
        if color in counts:
            counts[color] += 1
        else:
            counts[color] = 1

    # Get the most popular
    best = None
    best_count = 0
    for color, count in counts.items():
        if best_count < count:
            best = color
            best_count = count

    return best, best_count


def test_colors():
    assert colors(['c', 'v', 'c', 'b', 'm']) == ('c', 2)
    assert colors(['w', 'r', 'r', 'w', 'c', 'w', 'v']) == ('w', 3)
    assert colors(['r', 'o', 'b', 'y', 'b', 'm', 'g', 'b', 'b']) == ('b', 4)
