# -*- coding: utf-8 -*-
"""RandomIntervals test code."""
import numpy as np
from numpy import testing

from sktime.datasets import load_basic_motions, load_unit_test
from sktime.transformations.panel.random_intervals import RandomIntervals


def test_random_intervals_on_unit_test():
    """Test of RandomIntervals on unit test data."""
    # load unit test data
    X_train, y_train = load_unit_test(split="train")
    indices = np.random.RandomState(0).choice(len(y_train), 5, replace=False)

    # fit random intervals
    ri = RandomIntervals(random_state=0, n_intervals=3)
    ri.fit(X_train[indices], y_train[indices])

    # assert transformed data is the same
    data = ri.transform(X_train[indices])
    testing.assert_array_almost_equal(data, random_intervals_unit_test_data)


def test_random_intervals_on_basic_motions():
    """Test of RandomIntervals on basic motions data."""
    # load basic motions data
    X_train, y_train = load_basic_motions(split="train")
    indices = np.random.RandomState(4).choice(len(y_train), 5, replace=False)

    # fit random intervals
    ri = RandomIntervals(random_state=0, n_intervals=3)
    ri.fit(X_train.iloc[indices], y_train[indices])

    # assert transformed data is the same
    data = ri.transform(X_train.iloc[indices])
    testing.assert_array_almost_equal(data, random_intervals_basic_motions_data)


random_intervals_unit_test_data = np.array(
    [
        [
            67.66666666666667,
            25.32455988429677,
            45.0,
            95.0,
            54.0,
            63.0,
            79.0,
            24.25,
            17.192537140670463,
            3.0,
            45.0,
            18.0,
            24.5,
            30.75,
            1092.857142857143,
            92.96133348769006,
            900.0,
            1193.0,
            1092.5,
            1107.0,
            1132.5,
        ],
        [
            266.0,
            127.01181047445942,
            140.0,
            394.0,
            202.0,
            264.0,
            329.0,
            104.0,
            53.7649204097492,
            28.0,
            144.0,
            85.0,
            122.0,
            141.0,
            1136.142857142857,
            166.86164785177428,
            791.0,
            1290.0,
            1123.0,
            1137.0,
            1244.5,
        ],
        [
            75.33333333333333,
            21.77919496522618,
            51.0,
            93.0,
            66.5,
            82.0,
            87.5,
            33.75,
            14.591664287073858,
            17.0,
            51.0,
            25.25,
            33.5,
            42.0,
            869.2857142857143,
            74.94156453689831,
            730.0,
            954.0,
            844.0,
            871.0,
            921.0,
        ],
        [
            401.3333333333333,
            140.8628174265066,
            248.0,
            525.0,
            339.5,
            431.0,
            478.0,
            160.75,
            96.81382477036358,
            64.0,
            248.0,
            84.25,
            165.5,
            242.0,
            1607.7142857142858,
            194.2993517622694,
            1398.0,
            1891.0,
            1462.0,
            1563.0,
            1739.0,
        ],
        [
            79.33333333333333,
            61.74409553417504,
            21.0,
            144.0,
            47.0,
            73.0,
            108.5,
            14.75,
            4.856267428111155,
            10.0,
            21.0,
            11.5,
            14.0,
            17.25,
            1264.5714285714287,
            150.68273197113766,
            981.0,
            1461.0,
            1227.5,
            1269.0,
            1343.0,
        ],
    ]
)
random_intervals_basic_motions_data = np.array(
    [
        [
            -0.016424083333333325,
            0.6547927877406517,
            -1.001428,
            0.769715,
            -0.482736,
            0.062589,
            0.6425387499999999,
            -0.18428488461538467,
            1.595256137576266,
            -2.338441,
            2.351758,
            -1.63664225,
            -0.4993825,
            1.43555825,
            0.5066760666666666,
            0.8463066087506741,
            -0.604435,
            2.220163,
            -0.17810200000000004,
            0.50721,
            1.080491,
        ],
        [
            -0.56574475,
            5.658231830612009,
            -10.560272,
            5.505191,
            -2.40569125,
            1.2970625,
            3.60221125,
            -0.7096863461538461,
            5.894107347901109,
            -24.516344,
            8.301732,
            -2.306481,
            -0.23038200000000003,
            1.371637,
            4.007729533333333,
            4.566350914592744,
            -2.669635,
            13.075892,
            1.1285560000000001,
            4.574257,
            5.2055015000000004,
        ],
        [
            -0.00799025,
            0.06374908843002457,
            -0.135832,
            0.074574,
            -0.05859425,
            0.021307,
            0.037287,
            -0.0013316538461538537,
            0.1861669191911264,
            -0.279654,
            0.391516,
            -0.15048050000000002,
            -0.0532675,
            0.1258445,
            -0.27493380000000006,
            0.06683545473367516,
            -0.393257,
            -0.187027,
            -0.32838199999999995,
            -0.271927,
            -0.2129085,
        ],
        [
            -0.420147,
            1.6648887830804469,
            -3.052225,
            2.45563,
            -1.4482089999999999,
            -0.4394565,
            0.10986425,
            0.11708584615384582,
            6.33221568580587,
            -11.468482,
            11.026362,
            -6.066496750000001,
            0.20374799999999998,
            4.6302727500000005,
            8.5029004,
            8.987034966342021,
            -12.84577,
            17.731619,
            8.361293,
            11.698533,
            14.4014935,
        ],
        [
            0.0057705833333333125,
            0.5519217191205582,
            -1.009418,
            0.585942,
            -0.21040625000000002,
            0.203748,
            0.4094935,
            0.14085138461538463,
            1.3851363167709692,
            -1.821747,
            2.26653,
            -1.15656925,
            0.399506,
            1.15457225,
            0.7533285999999999,
            1.5515648153312285,
            -1.627442,
            3.59112,
            -0.19995000000000002,
            0.413103,
            1.785761,
        ],
    ]
)
