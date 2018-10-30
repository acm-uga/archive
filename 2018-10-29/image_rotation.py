# NumPy is the array library for Python.
# It is part of SciPy (pronounced “Sigh Pie”), a Python-based ecosystem of
# open-source software for mathematics, science, and engineering.
# https://www.scipy.org/
import numpy as np


def rotate(im):
    '''Rotate an image by 90 degrees clockwise.

    Arguments:
        im (2D array):
            The image being rotated.

    Returns:
        A new 2D array which is like ``im`` but rotated.
    '''
    # Create a new array of zeros for the rotated image.
    h, w = im.shape
    out = np.zeros(shape=(w, h))

    # The formula for the rotated index is: ``(y, x) -> (x, h-y-1)``.
    # Think of it this way: swapping ``(y, x) -> (x, y)`` transposes the image,
    # then ``(x, y) -> (x, h-y-1)`` reverses the rows.
    def rotate_coords(y, x):
        return (x, h-y-1)

    # Populate the new image.
    for y in range(h):
        for x in range(w):
            src = (y, x)
            dst = rotate_coords(y, x)
            out[dst] = im[src]

    return out


def rotate_inplace(im):
    '''Rotate an image in-place by 90 degrees clockwise.

    This is a weird algorithm:

    We work in rings, starting with the elements touching the outer edge, then
    the elements one index from the edge, then two from the edge, etc. For each
    ring, we consider four pointers, each starting in a corner. We exchange the
    elements uner the pointers in 90 rotation, then we step each pointer along
    the ring.

    Visually, we start with something like this:

        [[ 0,  1,  2,  3],
         [ 4,  5,  6,  7],
         [ 8,  9, 10, 11],
         [12, 23, 24, 15]]

    For the first stage, we only consider the outer ring:

        [[ 0,  1,  2,  3],
         [ 4, __, __,  7],
         [ 8, __, __, 11],
         [12, 23, 24, 15]]

    We start with pointers in the corners:

        [[ 0, **, **,  3],
         [**, __, __, **],
         [**, __, __, **],
         [12, **, **, 15]]

    Rotate 90 degrees:

        [[12, **, **,  0],
         [**, __, __, **],
         [**, __, __, **],
         [15, **, **,  3]]

    Then move our pointers and do it again:

        [[**,  1, **, **],      [[**,  8, **, **],
         [**, __, __,  7],  ->   [**, __, __,  1],
         [ 8, __, __, **],       [24, __, __, **],
         [**, **, 24, **]]       [**, **,  7, **]]

    When the ring is done, we move inwards a level and repeat:

        [[__, __, __, __],      [[__, __, __, __],
         [__,  5,  6, __],  ->   [__,  9,  5, __],
         [__,  9, 10, __],       [__, 10,  6, __],
         [__, __, __, __]]       [__, __, __, __]]

    Arguments:
        im (2D array):
            The image being rotated. Since this is an in-place rotation, the
            array must be square.

    Returns:
        Returns ``im`` back. It is rotated in-place.
    '''
    # The shape of the image must be square.
    h, w = im.shape
    assert h == w

    # The formula for the rotated index is: ``(y, x) -> (x, h-y-1)``.
    # Think of it this way: swapping ``(y, x) -> (x, y)`` transposes the image,
    # then ``(x, y) -> (x, h-y-1)`` reverses the rows.
    def rotate_coords(y, x):
        return (x, h-y-1)

    # For each layer, for each rotation in the layer,
    for y in range(h//2):
        for x in range(y, w-1-y):
            # Get coordinates for the 4 pointers.
            a = (y, x)
            b = rotate_coords(*a)
            c = rotate_coords(*b)
            d = rotate_coords(*c)

            # Do the rotation.
            # In other languages, this requires 4 temp variables.
            im[a], im[b], im[c], im[d] \
            = im[d], im[a], im[b], im[c]

    return im
