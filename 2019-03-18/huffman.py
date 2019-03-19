import heapq
from collections import defaultdict


class HuffmanTree:
    '''A Huffman tree

    Huffman trees are used for deriving Huffman code tables.

    See <https://en.m.wikipedia.org/wiki/Huffman_coding>.
    '''

    def __init__(self, value, freq, left=None, right=None):
        '''Create a binary Huffman tree.

        A Huffman tree has a value and a frequency. The value is a string
        listing the characters encoded by the tree. The frequency is the number
        of times any character encoded by the tree appears in the training text.

        Arguments:
            value (str): The characters encoded by this tree.
            freq (int): The sum of frequencies for all characters.
            left (HuffmanTree or None): The left subtree.
            right (HuffmanTree or None): The right subtree.
        '''
        self.value = value
        self.freq = freq
        self.left = left
        self.right = right

        # Validate the tree.
        # 1. If we have a left subtree, we must also have a right subtree.
        # 2. This value is the union of the subtree values.
        # 3. The subtree values cannot overlap.
        # 4. This frequency is the sum of the subtree frequencies.
        if left is not None:
            assert right is not None
            assert set(self.value) == set(left.value) | set(right.value)
            assert set() == set(left.value) & set(right.value)
            assert freq == left.freq + right.freq

    def __lt__(self, other):
        '''The definition of the less-than operator (<).

        Huffman trees are sorted by frequency. This enables us to build a
        min-heap of Huffman trees in the training algorithm.

        Arguments:
            other (HuffmanTree):
                The tree on the right-hand-side of the comparison.
        '''
        return self.freq < other.freq

    def get_codes(self, prefix=None):
        '''Get the table of codes represented by this Huffman tree.

        Arguments:
            prefix (list of int):
                Prepend this prefix to all codes in this tree.
        '''
        # The user is not expected to set ``prefix`` to anything.
        # The default is the empty list.
        prefix = prefix or []

        # If there is a left subtree there is also a right.
        # Recursivly get the codes for the left and right subtree, then combine
        # them together. We extend the prefix of the left subtree with a zero
        # and the right subtree with a one.
        if self.left is not None:
            assert self.right is not None
            left_codes = self.left.get_codes(prefix=(*prefix, 0))
            right_codes = self.right.get_codes(prefix=(*prefix, 1))
            return {**left_codes, **right_codes}

        # If we're at a leaf node, the tree represents a single character
        # and ``prefix`` is the code.
        else:
            assert self.right is None
            return {self.value: tuple(prefix)}

    @classmethod
    def from_text(cls, text):
        '''Learn an optimal Huffman tree from some text.
        '''
        # Compute the frequencies of each character.
        freqs = defaultdict(lambda: 0)
        for char in text:
            freqs[char] += 1

        # Create a leaf tree for each character.
        # ``cls`` refers to this class. It calls the ``__init__`` constructor.
        trees = [cls(char, freq) for char, freq in freqs.items()]

        # Iterativly take the two trees with the lowest frequencies and combine
        # them into a single new tree. We use a min-heap to quickly access the
        # two lowest frequency trees. The ``heapq`` library implements the heap
        # algorithms on top of a normal list.
        heapq.heapify(trees)
        while 1 < len(trees):
            left = heapq.heappop(trees)
            right = heapq.heappop(trees)
            value = left.value + right.value
            freq = left.freq + right.freq
            node = cls(value, freq, left, right)
            heapq.heappush(trees, node)

        # When we're done, our list of trees contains only one tree.
        return trees[0]


def huffman_codes(text):
    '''Learn a Huffman tree on some text and print its code table.
    '''
    tree = HuffmanTree.from_text(text)
    codes = tree.get_codes()
    for char, code in codes.items():
        print(f"'{char}': {code}")
