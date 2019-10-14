from src.gini import gini_gain_quotient, avoid_zero
from src.maximum import index_of_maximum
from mpyc.runtime import mpc
from dataclasses import dataclass, field
from typing import Any


def select_best_attribute(samples, outcomes):
    """
    Selects the best attribute for splitting a dataset.
    This is based on which attribute would yield the highest Gini gain.

    Keyword arguments:
    samples -- a matrix containing a sample in each row and an attribute value in each cell
    outcomes -- an array that for each sample contains the expected outcome

    Return value:
    Column index of the attribute that is best suited for splitting the dataset.

    Attribute values and outcomes are expected to be either 0 or 1.
    """
    aggregates = calculate_aggregates(samples, outcomes)
    gains = map(Aggregation.gini_gain_quotient, aggregates)
    gains = [(numerator, avoid_zero(denominator))
             for (numerator, denominator) in gains]
    return index_of_maximum(*gains)


def calculate_aggregates(samples, outcomes):
    if len(samples) == 0:
        raise ValueError("Expected at least one sample")

    number_of_samples = len(samples)
    number_of_attributes = len(samples[0])

    aggregates = []

    for column in range(number_of_attributes):
        aggregation = Aggregation(total=number_of_samples)
        aggregates.append(aggregation)
        for row in range(number_of_samples):
            value = samples[row][column]
            outcome = outcomes[row]
            aggregation.right_total += value
            aggregation.left_amount_classified_one += (1 - value) * outcome
            aggregation.right_amount_classified_one += value * outcome

    return aggregates


def partition_on(samples, is_active, attribute_index, threshold):
    num_attributes = len(samples[0])
    is_selected_attribute = [
        i == attribute_index for i in range(num_attributes)]

    selected_attribute = mpc.matrix_prod(
        [is_selected_attribute], samples, True)[0]

    left = [value <= threshold for value in selected_attribute]
    right = [(1 - l) for l in left]

    return left, right


@dataclass
class Aggregation:
    total: Any = 0
    right_total: Any = 0
    left_amount_classified_one: Any = 0
    right_amount_classified_one: Any = 0

    @property
    def left_total(self):
        return self.total - self.right_total

    @property
    def left_amount_classified_zero(self):
        return self.left_total - self.left_amount_classified_one

    @property
    def right_amount_classified_zero(self):
        return self.right_total - self.right_amount_classified_one

    def gini_gain_quotient(self):
        return gini_gain_quotient(
            self.left_total,
            self.right_total,
            self.left_amount_classified_zero,
            self.left_amount_classified_one,
            self.right_amount_classified_zero,
            self.right_amount_classified_one
        )