# -*- coding: utf-8 -*-
"""DrCIF test code."""
import numpy as np
from numpy import testing
from sklearn.metrics import accuracy_score

from sktime.classification.interval_based import DrCIF
from sktime.datasets import load_basic_motions, load_unit_test


def test_drcif_on_unit_test_data():
    """Test of DrCIF on unit test data."""
    # load unit test data
    X_train, y_train = load_unit_test(split="train")
    X_test, y_test = load_unit_test(split="test")
    indices = np.random.RandomState(0).choice(len(y_train), 10, replace=False)

    # train DrCIF
    drcif = DrCIF(n_estimators=10, random_state=0, save_transformed_data=True)
    drcif.fit(X_train, y_train)

    # assert probabilities are the same
    probas = drcif.predict_proba(X_test[indices])
    testing.assert_array_equal(probas, drcif_unit_test_probas)

    # test train estimate
    train_probas = drcif._get_train_probs(X_train, y_train)
    train_preds = drcif.classes_[np.argmax(train_probas, axis=1)]
    assert accuracy_score(y_train, train_preds) >= 0.75


def test_contracted_drcif_on_unit_test_data():
    """Test of contracted DrCIF on unit test data."""
    # load unit test data
    X_train, y_train = load_unit_test(split="train")

    # train contracted DrCIF
    drcif = DrCIF(
        time_limit_in_minutes=0.25,
        contract_max_n_estimators=10,
        random_state=0,
    )
    drcif.fit(X_train, y_train)

    assert len(drcif.estimators_) > 1


def test_drcif_on_basic_motions():
    """Test of DrCIF on basic motions data."""
    # load basic motions data
    X_train, y_train = load_basic_motions(split="train")
    X_test, y_test = load_basic_motions(split="test")
    indices = np.random.RandomState(4).choice(len(y_train), 10, replace=False)

    # train DrCIF
    drcif = DrCIF(n_estimators=10, random_state=0)
    drcif.fit(X_train.iloc[indices], y_train[indices])

    # assert probabilities are the same
    probas = drcif.predict_proba(X_test.iloc[indices])
    testing.assert_array_equal(probas, drcif_basic_motions_probas)


drcif_unit_test_probas = np.array(
    [
        [
            0.0,
            1.0,
        ],
        [
            1.0,
            0.0,
        ],
        [
            0.0,
            1.0,
        ],
        [
            1.0,
            0.0,
        ],
        [
            1.0,
            0.0,
        ],
        [
            1.0,
            0.0,
        ],
        [
            0.9,
            0.1,
        ],
        [
            0.0,
            1.0,
        ],
        [
            1.0,
            0.0,
        ],
        [
            1.0,
            0.0,
        ],
    ]
)
drcif_basic_motions_probas = np.array(
    [
        [
            0.0,
            0.0,
            0.0,
            1.0,
        ],
        [
            0.7,
            0.3,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            1.0,
            0.0,
        ],
        [
            0.1,
            0.9,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.0,
            1.0,
        ],
        [
            0.0,
            0.0,
            0.2,
            0.8,
        ],
        [
            0.7,
            0.1,
            0.0,
            0.2,
        ],
        [
            0.0,
            0.0,
            1.0,
            0.0,
        ],
        [
            0.2,
            0.8,
            0.0,
            0.0,
        ],
        [
            0.1,
            0.9,
            0.0,
            0.0,
        ],
    ]
)
