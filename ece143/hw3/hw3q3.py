def slide_window(x, width, increment):
    '''Returns a sequence of overlapping lists from the input list.

    Parameters
    ----------
    x: input list.
    width: size of each window.
    increment: factor by which the inputs should be incremented to generate the output list.

    Returns
    -------
    List of lists
        A sequence of overlapping lists from the input list

    Examples
    --------
       slide_window(list(range(18)),5,2)
           [[0, 1, 2, 3, 4],
           [2, 3, 4, 5, 6],
           [4, 5, 6, 7, 8],
           [6, 7, 8, 9, 10],
           [8, 9, 10, 11, 12],
           [10, 11, 12, 13, 14],
           [12, 13, 14, 15, 16]]

    '''

    assert isinstance(x, list)
    assert isinstance(width, int)
    assert isinstance(increment, int)
    assert width >= 0
    assert increment >= 0
    assert width <= len(x)

    output = []

    for i in range(0, len(x), increment):

        row = x[i:i + width]
        if (len(row) == width):
            output.append(row)

    return output
