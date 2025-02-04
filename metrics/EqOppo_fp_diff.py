""" Equal opportunity - Protected and unprotected False postives difference """
import math
import sys
import numpy

from metrics.utils import calc_fp_fn
from metrics.Metric import Metric

class EqOppo_fp_diff(Metric):
    def __init__(self):
        Metric.__init__(self)
        self.name = 'EqOppo_fp_diff'

    def calc(self, actual, predicted, prob_predictions, dict_of_sensitive_lists, single_sensitive_name,
             unprotected_vals, positive_pred):
        sensitive = dict_of_sensitive_lists[single_sensitive_name]
        fp_unprotected, fp_protected, fn_protected, fn_unprotected = \
            calc_fp_fn(actual, predicted, sensitive, unprotected_vals, positive_pred)

        fp_diff = math.fabs(fp_protected - fp_unprotected)

        return fp_diff
