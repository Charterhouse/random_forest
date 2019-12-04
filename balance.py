from mpyc.runtime import mpc

from src.dataset import ObliviousDataset, Sample
from src.output import output
from src.secint import secint as s
from src.forest import train_forest


def sample(ins, out):
    return Sample([s(i) for i in ins], s(out))


samples = ObliviousDataset.create(
    sample([1, 1, 1, 2], 1),
    sample([1, 1, 1, 3], 1),
    sample([1, 1, 1, 4], 1),
    sample([1, 1, 1, 5], 1),
    sample([1, 1, 2, 1], 1),
    sample([1, 1, 2, 2], 1),
    sample([1, 1, 2, 3], 1),
    sample([1, 1, 2, 4], 1),
    sample([1, 1, 2, 5], 1),
    sample([1, 1, 3, 1], 1),
    sample([1, 1, 3, 2], 1),
    sample([1, 1, 3, 3], 1),
    sample([1, 1, 3, 4], 1),
    sample([1, 1, 3, 5], 1),
    sample([1, 1, 4, 1], 1),
    sample([1, 1, 4, 2], 1),
    sample([1, 1, 4, 3], 1),
    sample([1, 1, 4, 4], 1),
    sample([1, 1, 4, 5], 1),
    sample([1, 1, 5, 1], 1),
    sample([1, 1, 5, 2], 1),
    sample([1, 1, 5, 3], 1),
    sample([1, 1, 5, 4], 1),
    sample([1, 1, 5, 5], 1),
    sample([1, 2, 1, 1], 0),

    sample([1, 2, 1, 3], 1),
    sample([1, 2, 1, 4], 1),
    sample([1, 2, 1, 5], 1),

    sample([1, 2, 2, 2], 1),
    sample([1, 2, 2, 3], 1),
    sample([1, 2, 2, 4], 1),
    sample([1, 2, 2, 5], 1),
    sample([1, 2, 3, 1], 1),
    sample([1, 2, 3, 2], 1),
    sample([1, 2, 3, 3], 1),
    sample([1, 2, 3, 4], 1),
    sample([1, 2, 3, 5], 1),
    sample([1, 2, 4, 1], 1),
    sample([1, 2, 4, 2], 1),
    sample([1, 2, 4, 3], 1),
    sample([1, 2, 4, 4], 1),
    sample([1, 2, 4, 5], 1),
    sample([1, 2, 5, 1], 1),
    sample([1, 2, 5, 2], 1),
    sample([1, 2, 5, 3], 1),
    sample([1, 2, 5, 4], 1),
    sample([1, 2, 5, 5], 1),
    sample([1, 3, 1, 1], 0),
    sample([1, 3, 1, 2], 0),

    sample([1, 3, 1, 4], 1),
    sample([1, 3, 1, 5], 1),
    sample([1, 3, 2, 1], 0),
    sample([1, 3, 2, 2], 1),
    sample([1, 3, 2, 3], 1),
    sample([1, 3, 2, 4], 1),
    sample([1, 3, 2, 5], 1),

    sample([1, 3, 3, 2], 1),
    sample([1, 3, 3, 3], 1),
    sample([1, 3, 3, 4], 1),
    sample([1, 3, 3, 5], 1),
    sample([1, 3, 4, 1], 1),
    sample([1, 3, 4, 2], 1),
    sample([1, 3, 4, 3], 1),
    sample([1, 3, 4, 4], 1),
    sample([1, 3, 4, 5], 1),
    sample([1, 3, 5, 1], 1),
    sample([1, 3, 5, 2], 1),
    sample([1, 3, 5, 3], 1),
    sample([1, 3, 5, 4], 1),
    sample([1, 3, 5, 5], 1),
    sample([1, 4, 1, 1], 0),
    sample([1, 4, 1, 2], 0),
    sample([1, 4, 1, 3], 0),

    sample([1, 4, 1, 5], 1),
    sample([1, 4, 2, 1], 0),

    sample([1, 4, 2, 3], 1),
    sample([1, 4, 2, 4], 1),
    sample([1, 4, 2, 5], 1),
    sample([1, 4, 3, 1], 0),
    sample([1, 4, 3, 2], 1),
    sample([1, 4, 3, 3], 1),
    sample([1, 4, 3, 4], 1),
    sample([1, 4, 3, 5], 1),

    sample([1, 4, 4, 2], 1),
    sample([1, 4, 4, 3], 1),
    sample([1, 4, 4, 4], 1),
    sample([1, 4, 4, 5], 1),
    sample([1, 4, 5, 1], 1),
    sample([1, 4, 5, 2], 1),
    sample([1, 4, 5, 3], 1),
    sample([1, 4, 5, 4], 1),
    sample([1, 4, 5, 5], 1),
    sample([1, 5, 1, 1], 0),
    sample([1, 5, 1, 2], 0),
    sample([1, 5, 1, 3], 0),
    sample([1, 5, 1, 4], 0),

    sample([1, 5, 2, 1], 0),
    sample([1, 5, 2, 2], 0),
    sample([1, 5, 2, 3], 1),
    sample([1, 5, 2, 4], 1),
    sample([1, 5, 2, 5], 1),
    sample([1, 5, 3, 1], 0),
    sample([1, 5, 3, 2], 1),
    sample([1, 5, 3, 3], 1),
    sample([1, 5, 3, 4], 1),
    sample([1, 5, 3, 5], 1),
    sample([1, 5, 4, 1], 0),
    sample([1, 5, 4, 2], 1),
    sample([1, 5, 4, 3], 1),
    sample([1, 5, 4, 4], 1),
    sample([1, 5, 4, 5], 1),

    sample([1, 5, 5, 2], 1),
    sample([1, 5, 5, 3], 1),
    sample([1, 5, 5, 4], 1),
    sample([1, 5, 5, 5], 1),
    sample([2, 1, 1, 1], 0),

    sample([2, 1, 1, 3], 1),
    sample([2, 1, 1, 4], 1),
    sample([2, 1, 1, 5], 1),

    sample([2, 1, 2, 2], 1),
    sample([2, 1, 2, 3], 1),
    sample([2, 1, 2, 4], 1),
    sample([2, 1, 2, 5], 1),
    sample([2, 1, 3, 1], 1),
    sample([2, 1, 3, 2], 1),
    sample([2, 1, 3, 3], 1),
    sample([2, 1, 3, 4], 1),
    sample([2, 1, 3, 5], 1),
    sample([2, 1, 4, 1], 1),
    sample([2, 1, 4, 2], 1),
    sample([2, 1, 4, 3], 1),
    sample([2, 1, 4, 4], 1),
    sample([2, 1, 4, 5], 1),
    sample([2, 1, 5, 1], 1),
    sample([2, 1, 5, 2], 1),
    sample([2, 1, 5, 3], 1),
    sample([2, 1, 5, 4], 1),
    sample([2, 1, 5, 5], 1),
    sample([2, 2, 1, 1], 0),
    sample([2, 2, 1, 2], 0),
    sample([2, 2, 1, 3], 0),

    sample([2, 2, 1, 5], 1),
    sample([2, 2, 2, 1], 0),

    sample([2, 2, 2, 3], 1),
    sample([2, 2, 2, 4], 1),
    sample([2, 2, 2, 5], 1),
    sample([2, 2, 3, 1], 0),
    sample([2, 2, 3, 2], 1),
    sample([2, 2, 3, 3], 1),
    sample([2, 2, 3, 4], 1),
    sample([2, 2, 3, 5], 1),

    sample([2, 2, 4, 2], 1),
    sample([2, 2, 4, 3], 1),
    sample([2, 2, 4, 4], 1),
    sample([2, 2, 4, 5], 1),
    sample([2, 2, 5, 1], 1),
    sample([2, 2, 5, 2], 1),
    sample([2, 2, 5, 3], 1),
    sample([2, 2, 5, 4], 1),
    sample([2, 2, 5, 5], 1),
    sample([2, 3, 1, 1], 0),
    sample([2, 3, 1, 2], 0),
    sample([2, 3, 1, 3], 0),
    sample([2, 3, 1, 4], 0),
    sample([2, 3, 1, 5], 0),
    sample([2, 3, 2, 1], 0),
    sample([2, 3, 2, 2], 0),

    sample([2, 3, 2, 4], 1),
    sample([2, 3, 2, 5], 1),
    sample([2, 3, 3, 1], 0),

    sample([2, 3, 3, 3], 1),
    sample([2, 3, 3, 4], 1),
    sample([2, 3, 3, 5], 1),
    sample([2, 3, 4, 1], 0),
    sample([2, 3, 4, 2], 1),
    sample([2, 3, 4, 3], 1),
    sample([2, 3, 4, 4], 1),
    sample([2, 3, 4, 5], 1),
    sample([2, 3, 5, 1], 0),
    sample([2, 3, 5, 2], 1),
    sample([2, 3, 5, 3], 1),
    sample([2, 3, 5, 4], 1),
    sample([2, 3, 5, 5], 1),
    sample([2, 4, 1, 1], 0),
    sample([2, 4, 1, 2], 0),
    sample([2, 4, 1, 3], 0),
    sample([2, 4, 1, 4], 0),
    sample([2, 4, 1, 5], 0),
    sample([2, 4, 2, 1], 0),
    sample([2, 4, 2, 2], 0),
    sample([2, 4, 2, 3], 0),

    sample([2, 4, 2, 5], 1),
    sample([2, 4, 3, 1], 0),
    sample([2, 4, 3, 2], 0),
    sample([2, 4, 3, 3], 1),
    sample([2, 4, 3, 4], 1),
    sample([2, 4, 3, 5], 1),
    sample([2, 4, 4, 1], 0),

    sample([2, 4, 4, 3], 1),
    sample([2, 4, 4, 4], 1),
    sample([2, 4, 4, 5], 1),
    sample([2, 4, 5, 1], 0),
    sample([2, 4, 5, 2], 1),
    sample([2, 4, 5, 3], 1),
    sample([2, 4, 5, 4], 1),
    sample([2, 4, 5, 5], 1),
    sample([2, 5, 1, 1], 0),
    sample([2, 5, 1, 2], 0),
    sample([2, 5, 1, 3], 0),
    sample([2, 5, 1, 4], 0),
    sample([2, 5, 1, 5], 0),
    sample([2, 5, 2, 1], 0),
    sample([2, 5, 2, 2], 0),
    sample([2, 5, 2, 3], 0),
    sample([2, 5, 2, 4], 0),

    sample([2, 5, 3, 1], 0),
    sample([2, 5, 3, 2], 0),
    sample([2, 5, 3, 3], 0),
    sample([2, 5, 3, 4], 1),
    sample([2, 5, 3, 5], 1),
    sample([2, 5, 4, 1], 0),
    sample([2, 5, 4, 2], 0),
    sample([2, 5, 4, 3], 1),
    sample([2, 5, 4, 4], 1),
    sample([2, 5, 4, 5], 1),
    sample([2, 5, 5, 1], 0),

    sample([2, 5, 5, 3], 1),
    sample([2, 5, 5, 4], 1),
    sample([2, 5, 5, 5], 1),
    sample([3, 1, 1, 1], 0),
    sample([3, 1, 1, 2], 0),

    sample([3, 1, 1, 4], 1),
    sample([3, 1, 1, 5], 1),
    sample([3, 1, 2, 1], 0),
    sample([3, 1, 2, 2], 1),
    sample([3, 1, 2, 3], 1),
    sample([3, 1, 2, 4], 1),
    sample([3, 1, 2, 5], 1),

    sample([3, 1, 3, 2], 1),
    sample([3, 1, 3, 3], 1),
    sample([3, 1, 3, 4], 1),
    sample([3, 1, 3, 5], 1),
    sample([3, 1, 4, 1], 1),
    sample([3, 1, 4, 2], 1),
    sample([3, 1, 4, 3], 1),
    sample([3, 1, 4, 4], 1),
    sample([3, 1, 4, 5], 1),
    sample([3, 1, 5, 1], 1),
    sample([3, 1, 5, 2], 1),
    sample([3, 1, 5, 3], 1),
    sample([3, 1, 5, 4], 1),
    sample([3, 1, 5, 5], 1),
    sample([3, 2, 1, 1], 0),
    sample([3, 2, 1, 2], 0),
    sample([3, 2, 1, 3], 0),
    sample([3, 2, 1, 4], 0),
    sample([3, 2, 1, 5], 0),
    sample([3, 2, 2, 1], 0),
    sample([3, 2, 2, 2], 0),

    sample([3, 2, 2, 4], 1),
    sample([3, 2, 2, 5], 1),
    sample([3, 2, 3, 1], 0),

    sample([3, 2, 3, 3], 1),
    sample([3, 2, 3, 4], 1),
    sample([3, 2, 3, 5], 1),
    sample([3, 2, 4, 1], 0),
    sample([3, 2, 4, 2], 1),
    sample([3, 2, 4, 3], 1),
    sample([3, 2, 4, 4], 1),
    sample([3, 2, 4, 5], 1),
    sample([3, 2, 5, 1], 0),
    sample([3, 2, 5, 2], 1),
    sample([3, 2, 5, 3], 1),
    sample([3, 2, 5, 4], 1),
    sample([3, 2, 5, 5], 1),
    sample([3, 3, 1, 1], 0),
    sample([3, 3, 1, 2], 0),
    sample([3, 3, 1, 3], 0),
    sample([3, 3, 1, 4], 0),
    sample([3, 3, 1, 5], 0),
    sample([3, 3, 2, 1], 0),
    sample([3, 3, 2, 2], 0),
    sample([3, 3, 2, 3], 0),
    sample([3, 3, 2, 4], 0),
    sample([3, 3, 2, 5], 1),
    sample([3, 3, 3, 1], 0),
    sample([3, 3, 3, 2], 0),

    sample([3, 3, 3, 4], 1),
    sample([3, 3, 3, 5], 1),
    sample([3, 3, 4, 1], 0),
    sample([3, 3, 4, 2], 0),
    sample([3, 3, 4, 3], 1),
    sample([3, 3, 4, 4], 1),
    sample([3, 3, 4, 5], 1),
    sample([3, 3, 5, 1], 0),
    sample([3, 3, 5, 2], 1),
    sample([3, 3, 5, 3], 1),
    sample([3, 3, 5, 4], 1),
    sample([3, 3, 5, 5], 1),
    sample([3, 4, 1, 1], 0),
    sample([3, 4, 1, 2], 0),
    sample([3, 4, 1, 3], 0),
    sample([3, 4, 1, 4], 0),
    sample([3, 4, 1, 5], 0),
    sample([3, 4, 2, 1], 0),
    sample([3, 4, 2, 2], 0),
    sample([3, 4, 2, 3], 0),
    sample([3, 4, 2, 4], 0),
    sample([3, 4, 2, 5], 0),
    sample([3, 4, 3, 1], 0),
    sample([3, 4, 3, 2], 0),
    sample([3, 4, 3, 3], 0),

    sample([3, 4, 3, 5], 1),
    sample([3, 4, 4, 1], 0),
    sample([3, 4, 4, 2], 0),

    sample([3, 4, 4, 4], 1),
    sample([3, 4, 4, 5], 1),
    sample([3, 4, 5, 1], 0),
    sample([3, 4, 5, 2], 0),
    sample([3, 4, 5, 3], 1),
    sample([3, 4, 5, 4], 1),
    sample([3, 4, 5, 5], 1),
    sample([3, 5, 1, 1], 0),
    sample([3, 5, 1, 2], 0),
    sample([3, 5, 1, 3], 0),
    sample([3, 5, 1, 4], 0),
    sample([3, 5, 1, 5], 0),
    sample([3, 5, 2, 1], 0),
    sample([3, 5, 2, 2], 0),
    sample([3, 5, 2, 3], 0),
    sample([3, 5, 2, 4], 0),
    sample([3, 5, 2, 5], 0),
    sample([3, 5, 3, 1], 0),
    sample([3, 5, 3, 2], 0),
    sample([3, 5, 3, 3], 0),
    sample([3, 5, 3, 4], 0),

    sample([3, 5, 4, 1], 0),
    sample([3, 5, 4, 2], 0),
    sample([3, 5, 4, 3], 0),
    sample([3, 5, 4, 4], 1),
    sample([3, 5, 4, 5], 1),
    sample([3, 5, 5, 1], 0),
    sample([3, 5, 5, 2], 0),

    sample([3, 5, 5, 4], 1),
    sample([3, 5, 5, 5], 1),
    sample([4, 1, 1, 1], 0),
    sample([4, 1, 1, 2], 0),
    sample([4, 1, 1, 3], 0),

    sample([4, 1, 1, 5], 1),
    sample([4, 1, 2, 1], 0),

    sample([4, 1, 2, 3], 1),
    sample([4, 1, 2, 4], 1),
    sample([4, 1, 2, 5], 1),
    sample([4, 1, 3, 1], 0),
    sample([4, 1, 3, 2], 1),
    sample([4, 1, 3, 3], 1),
    sample([4, 1, 3, 4], 1),
    sample([4, 1, 3, 5], 1),

    sample([4, 1, 4, 2], 1),
    sample([4, 1, 4, 3], 1),
    sample([4, 1, 4, 4], 1),
    sample([4, 1, 4, 5], 1),
    sample([4, 1, 5, 1], 1),
    sample([4, 1, 5, 2], 1),
    sample([4, 1, 5, 3], 1),
    sample([4, 1, 5, 4], 1),
    sample([4, 1, 5, 5], 1),
    sample([4, 2, 1, 1], 0),
    sample([4, 2, 1, 2], 0),
    sample([4, 2, 1, 3], 0),
    sample([4, 2, 1, 4], 0),
    sample([4, 2, 1, 5], 0),
    sample([4, 2, 2, 1], 0),
    sample([4, 2, 2, 2], 0),
    sample([4, 2, 2, 3], 0),

    sample([4, 2, 2, 5], 1),
    sample([4, 2, 3, 1], 0),
    sample([4, 2, 3, 2], 0),
    sample([4, 2, 3, 3], 1),
    sample([4, 2, 3, 4], 1),
    sample([4, 2, 3, 5], 1),
    sample([4, 2, 4, 1], 0),

    sample([4, 2, 4, 3], 1),
    sample([4, 2, 4, 4], 1),
    sample([4, 2, 4, 5], 1),
    sample([4, 2, 5, 1], 0),
    sample([4, 2, 5, 2], 1),
    sample([4, 2, 5, 3], 1),
    sample([4, 2, 5, 4], 1),
    sample([4, 2, 5, 5], 1),
    sample([4, 3, 1, 1], 0),
    sample([4, 3, 1, 2], 0),
    sample([4, 3, 1, 3], 0),
    sample([4, 3, 1, 4], 0),
    sample([4, 3, 1, 5], 0),
    sample([4, 3, 2, 1], 0),
    sample([4, 3, 2, 2], 0),
    sample([4, 3, 2, 3], 0),
    sample([4, 3, 2, 4], 0),
    sample([4, 3, 2, 5], 0),
    sample([4, 3, 3, 1], 0),
    sample([4, 3, 3, 2], 0),
    sample([4, 3, 3, 3], 0),

    sample([4, 3, 3, 5], 1),
    sample([4, 3, 4, 1], 0),
    sample([4, 3, 4, 2], 0),

    sample([4, 3, 4, 4], 1),
    sample([4, 3, 4, 5], 1),
    sample([4, 3, 5, 1], 0),
    sample([4, 3, 5, 2], 0),
    sample([4, 3, 5, 3], 1),
    sample([4, 3, 5, 4], 1),
    sample([4, 3, 5, 5], 1),
    sample([4, 4, 1, 1], 0),
    sample([4, 4, 1, 2], 0),
    sample([4, 4, 1, 3], 0),
    sample([4, 4, 1, 4], 0),
    sample([4, 4, 1, 5], 0),
    sample([4, 4, 2, 1], 0),
    sample([4, 4, 2, 2], 0),
    sample([4, 4, 2, 3], 0),
    sample([4, 4, 2, 4], 0),
    sample([4, 4, 2, 5], 0),
    sample([4, 4, 3, 1], 0),
    sample([4, 4, 3, 2], 0),
    sample([4, 4, 3, 3], 0),
    sample([4, 4, 3, 4], 0),
    sample([4, 4, 3, 5], 0),
    sample([4, 4, 4, 1], 0),
    sample([4, 4, 4, 2], 0),
    sample([4, 4, 4, 3], 0),

    sample([4, 4, 4, 5], 1),
    sample([4, 4, 5, 1], 0),
    sample([4, 4, 5, 2], 0),
    sample([4, 4, 5, 3], 0),
    sample([4, 4, 5, 4], 1),
    sample([4, 4, 5, 5], 1),
    sample([4, 5, 1, 1], 0),
    sample([4, 5, 1, 2], 0),
    sample([4, 5, 1, 3], 0),
    sample([4, 5, 1, 4], 0),
    sample([4, 5, 1, 5], 0),
    sample([4, 5, 2, 1], 0),
    sample([4, 5, 2, 2], 0),
    sample([4, 5, 2, 3], 0),
    sample([4, 5, 2, 4], 0),
    sample([4, 5, 2, 5], 0),
    sample([4, 5, 3, 1], 0),
    sample([4, 5, 3, 2], 0),
    sample([4, 5, 3, 3], 0),
    sample([4, 5, 3, 4], 0),
    sample([4, 5, 3, 5], 0),
    sample([4, 5, 4, 1], 0),
    sample([4, 5, 4, 2], 0),
    sample([4, 5, 4, 3], 0),
    sample([4, 5, 4, 4], 0),

    sample([4, 5, 5, 1], 0),
    sample([4, 5, 5, 2], 0),
    sample([4, 5, 5, 3], 0),

    sample([4, 5, 5, 5], 1),
    sample([5, 1, 1, 1], 0),
    sample([5, 1, 1, 2], 0),
    sample([5, 1, 1, 3], 0),
    sample([5, 1, 1, 4], 0),

    sample([5, 1, 2, 1], 0),
    sample([5, 1, 2, 2], 0),
    sample([5, 1, 2, 3], 1),
    sample([5, 1, 2, 4], 1),
    sample([5, 1, 2, 5], 1),
    sample([5, 1, 3, 1], 0),
    sample([5, 1, 3, 2], 1),
    sample([5, 1, 3, 3], 1),
    sample([5, 1, 3, 4], 1),
    sample([5, 1, 3, 5], 1),
    sample([5, 1, 4, 1], 0),
    sample([5, 1, 4, 2], 1),
    sample([5, 1, 4, 3], 1),
    sample([5, 1, 4, 4], 1),
    sample([5, 1, 4, 5], 1),

    sample([5, 1, 5, 2], 1),
    sample([5, 1, 5, 3], 1),
    sample([5, 1, 5, 4], 1),
    sample([5, 1, 5, 5], 1),
    sample([5, 2, 1, 1], 0),
    sample([5, 2, 1, 2], 0),
    sample([5, 2, 1, 3], 0),
    sample([5, 2, 1, 4], 0),
    sample([5, 2, 1, 5], 0),
    sample([5, 2, 2, 1], 0),
    sample([5, 2, 2, 2], 0),
    sample([5, 2, 2, 3], 0),
    sample([5, 2, 2, 4], 0),

    sample([5, 2, 3, 1], 0),
    sample([5, 2, 3, 2], 0),
    sample([5, 2, 3, 3], 0),
    sample([5, 2, 3, 4], 1),
    sample([5, 2, 3, 5], 1),
    sample([5, 2, 4, 1], 0),
    sample([5, 2, 4, 2], 0),
    sample([5, 2, 4, 3], 1),
    sample([5, 2, 4, 4], 1),
    sample([5, 2, 4, 5], 1),
    sample([5, 2, 5, 1], 0),

    sample([5, 2, 5, 3], 1),
    sample([5, 2, 5, 4], 1),
    sample([5, 2, 5, 5], 1),
    sample([5, 3, 1, 1], 0),
    sample([5, 3, 1, 2], 0),
    sample([5, 3, 1, 3], 0),
    sample([5, 3, 1, 4], 0),
    sample([5, 3, 1, 5], 0),
    sample([5, 3, 2, 1], 0),
    sample([5, 3, 2, 2], 0),
    sample([5, 3, 2, 3], 0),
    sample([5, 3, 2, 4], 0),
    sample([5, 3, 2, 5], 0),
    sample([5, 3, 3, 1], 0),
    sample([5, 3, 3, 2], 0),
    sample([5, 3, 3, 3], 0),
    sample([5, 3, 3, 4], 0),

    sample([5, 3, 4, 1], 0),
    sample([5, 3, 4, 2], 0),
    sample([5, 3, 4, 3], 0),
    sample([5, 3, 4, 4], 1),
    sample([5, 3, 4, 5], 1),
    sample([5, 3, 5, 1], 0),
    sample([5, 3, 5, 2], 0),

    sample([5, 3, 5, 4], 1),
    sample([5, 3, 5, 5], 1),
    sample([5, 4, 1, 1], 0),
    sample([5, 4, 1, 2], 0),
    sample([5, 4, 1, 3], 0),
    sample([5, 4, 1, 4], 0),
    sample([5, 4, 1, 5], 0),
    sample([5, 4, 2, 1], 0),
    sample([5, 4, 2, 2], 0),
    sample([5, 4, 2, 3], 0),
    sample([5, 4, 2, 4], 0),
    sample([5, 4, 2, 5], 0),
    sample([5, 4, 3, 1], 0),
    sample([5, 4, 3, 2], 0),
    sample([5, 4, 3, 3], 0),
    sample([5, 4, 3, 4], 0),
    sample([5, 4, 3, 5], 0),
    sample([5, 4, 4, 1], 0),
    sample([5, 4, 4, 2], 0),
    sample([5, 4, 4, 3], 0),
    sample([5, 4, 4, 4], 0),

    sample([5, 4, 5, 1], 0),
    sample([5, 4, 5, 2], 0),
    sample([5, 4, 5, 3], 0),

    sample([5, 4, 5, 5], 1),
    sample([5, 5, 1, 1], 0),
    sample([5, 5, 1, 2], 0),
    sample([5, 5, 1, 3], 0),
    sample([5, 5, 1, 4], 0),
    sample([5, 5, 1, 5], 0),
    sample([5, 5, 2, 1], 0),
    sample([5, 5, 2, 2], 0),
    sample([5, 5, 2, 3], 0),
    sample([5, 5, 2, 4], 0),
    sample([5, 5, 2, 5], 0),
    sample([5, 5, 3, 1], 0),
    sample([5, 5, 3, 2], 0),
    sample([5, 5, 3, 3], 0),
    sample([5, 5, 3, 4], 0),
    sample([5, 5, 3, 5], 0),
    sample([5, 5, 4, 1], 0),
    sample([5, 5, 4, 2], 0),
    sample([5, 5, 4, 3], 0),
    sample([5, 5, 4, 4], 0),
    sample([5, 5, 4, 5], 0),
    sample([5, 5, 5, 1], 0),
    sample([5, 5, 5, 2], 0),
    sample([5, 5, 5, 3], 0),
    sample([5, 5, 5, 4], 0),
    continuous_attributes=[0, 1, 2, 3]
)


async def main():
    async with mpc:
        forest = await output(await train_forest(samples, amount=2, depth=4))
        for index, tree in enumerate(forest):
            print(f"Tree #{index}")
            tree.pretty_print()


if __name__ == '__main__':
    mpc.run(main())
