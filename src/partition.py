from mpyc.runtime import mpc


def partition_on(samples, is_active, attribute_index, threshold):
    """
    Splits given data set into left and right part based on the
    threshold value of the attribute on which to split. Returns
    a pair containing the rows left of the split and those right
    of the split.

    Keyword arguments:
    samples -- ObliviousDataset
    attribute_index -- index of attribute (column) used for splitting
    threshold -- value that determines whether rows end up left or right
    """
    selected_attribute = samples.column(attribute_index)

    left = [value <= threshold for value in selected_attribute]
    right = [(1 - l) for l in left]

    left = zero_if_inactive(left, is_active)
    right = zero_if_inactive(right, is_active)

    return left, right


def zero_if_inactive(values, is_active):
    return mpc.schur_prod(values, is_active)
