from collections import defaultdict

def anagram(s, t):
    '''Determine if ``s`` is an anagram of ``t``.

    Arguments:
        s (Sequence): The first sequence.
        t (Sequence): The second sequence.

    Returns:
        bool:
            True when ``s`` and ``t`` are anagrams of each other.
    '''
    # Count the number of occurences of each letter in ``s``.
    s_counts = defaultdict(lambda: 0)
    for char in s:
        s_counts[char] += 1

    # Count the number of occurences of each letter in ``t``.
    t_counts = defaultdict(lambda: 0)
    for char in t:
        t_counts[char] += 1

    # They're anagrams if the counts are the same.
    return s_counts == t_counts
