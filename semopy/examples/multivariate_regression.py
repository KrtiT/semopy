#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Univariate regression example model.

True parameter values are 2, 6, -10 (regression parameters):
    y = 2*x1 + 6*x2 - 10*x3 + eps
    eps ~ N(0, 1)
"""
import pandas as pd

__desc = 'y ~ x1 + x2 + x3'

__filename = '%s/multivariate_data.csv' % '/'.join(__file__.split('/')[:-1])


def get_model():
    """
    Retrieve model description in semopy syntax.

    Returnsunivariate_regression
    -------
    str
        Model's description.

    """
    return __desc


def get_data():
    """
    Retrieve dataset.

    Returns
    -------
    pd.DataFrame
        Dataset.

    """
    return pd.read_csv(__filename, index_col=0)
