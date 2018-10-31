# NumPy is the array library for Python.
# It is part of SciPy (pronounced “Sigh Pie”), a Python-based ecosystem of
# open-source software for mathematics, science, and engineering.
# https://www.scipy.org/
import numpy as np


def rotate(im):
    '''Rotate an image by 90 degrees clockwise.

    This version crates a new image and copies pixels from the input.

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

    We start with pointers in the corners and rotate the elements 90 degrees:

        [[ 0, **, **,  3],      [[12, **, **,  0],
         [**, __, __, **],  ->   [**, __, __, **],
         [**, __, __, **],       [**, __, __, **],
         [12, **, **, 15]]       [15, **, **,  3]]

    Then move our pointers and do another rotation:

        [[**,  1, **, **],      [[**,  8, **, **],
         [**, __, __,  7],  ->   [**, __, __,  1],
         [ 8, __, __, **],       [24, __, __, **],
         [**, **, 24, **]]       [**, **,  7, **]]

    We do one final rotation to complete the outer ring:

        [[**, **,  2, **],      [[**, **,  4, **],
         [ 4, __, __, **],  ->   [23, __, __, **],
         [**, __, __, 11],       [**, __, __,  2],
         [**, 23, **, **]]       [**, 11, **, **]]

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

    # For each layer, for each rotation in the layer.
    for y in range(h//2):
        for x in range(y, w-1-y):
            # Get coordinates for the 4 pointers.
            a = (y, x)
            b = rotate_coords(*a)
            c = rotate_coords(*b)
            d = rotate_coords(*c)

            # Swap the elements clockwise.
            # In Java and C++, this requires a temp variable.
            im[a], im[b], im[c], im[d] \
            = im[d], im[a], im[b], im[c]

    return im


def rotate_strided(im):
    '''Rotate an image in-place by 90 degrees clockwise.

    This method operates on strided arrays.

    A strided array is one of many ways to implement an n-dimensional array.
    One property of strided arrays is that they can be rotated in-place and
    in constant time. You can even rotate non-square images.

    A strided array is a view into a one dimensional array. This view consists
    of three parts: an origin index, a shape, and stride list. The origin index
    ponts into the 1D array of the element which should appear at the origin,
    e.g. the element to appear at ``(0, 0)`` in a 2D array. The shape is a list
    of lengths for each axis, e.g. the pair ``(height, width)`` for a 2D array.
    And the strides tell us how to move the origin index along each axis.

    Finding the element in the 1D array given an index into a 2D view follows a
    simple formula. The index of the element at ``(y, x)`` is:

        i = origin + (y * strides[0]) + (x * strides[1])

    For example, this 3-by-4 image:

        [[ 0,  1,  2,  3],
         [ 4,  5,  6,  7],
         [ 8,  9, 10, 11]]

    is implemented by this strided array:

        storage = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        image = {
            origin: 0,
            shape: (3, 4),
            strides: (4, 1),
        }

    We can check the structure by hand. The element at ``(1, 2)`` in the image
    should be element ``6`` in the storage array. The index formula gives
    ``i = 0 + (1 * 4) + (2 * 1) = 6``.

    Rotation can be broken down into two operations: a transpose followed by
    flipping the rows. Performing a transpose in a strided array is easy. We
    simply swap the order in both the shape and the strides:

        storage = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        transpose = {
            origin: 0,
            shape: (4, 3),
            strides: (1, 4),
        }

    We can again check the structure by hand. The element at ``(1, 2)`` in the
    transpose should be element ``9`` in the storage array. The index formula
    gives ``i = 0 + (1 * 1) + (2 * 4) = 9``.

    The next step is flipping along the rows. We can accomplish this by flipping
    the sign of the row stride and updating the origin.

        storage = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        rotated = {
            origin: 8,
            shape: (4, 3),
            strides: (1, -4),
        }

    The formula to update the origin when flipping along axis ``i`` is:

        new_origin = origin + (shape[i] - 1) + stride[i]

    in other words, to reverse the rows of a 2D array, the new origin is the
    index that was previously at the end of the first row: ``(0, width - 1)``.

    We can yet again check the structure by hand. The element at ``(1, 2)`` in
    the rotated image should be element ``1`` in the storage array. The index
    formula gives ``i = 8 + (1 * 1) + (2 * -4) = 1``.

    With all that being said, numpy arrays are strided arrays, and both
    transpose and flip are simple to express.

    Technically, this returns a new view into the same underlying storage.
    '''
    im = im.T         # transpose
    im = im[:, ::-1]  # flip rows
    return im


def test_rotate():
    '''Test the rotation algorithms.
    '''
    image = np.array(
        [[ 0,  1,  2,  3,  4],
         [ 5,  6,  7,  8,  9],
         [10, 11, 12, 13, 14],
         [15, 16, 17, 18, 19],
         [20, 21, 22, 23, 24]]
    )

    rotated = np.array(
        [[20, 15, 10,  5,  0],
         [21, 16, 11,  6,  1],
         [22, 17, 12,  7,  2],
         [23, 18, 13,  8,  3],
         [24, 19, 14,  9,  4]]
    )

    assert (rotate(image) == rotated).all()
    assert (rotate_inplace(image.copy()) == rotated).all()
    assert (rotate_strided(image) == rotated).all()
