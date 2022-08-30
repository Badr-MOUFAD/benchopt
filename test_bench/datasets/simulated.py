import numpy as np

from benchopt import BaseDataset
from benchopt.datasets.simulated import make_correlated_data


class Dataset(BaseDataset):
    name = "simulated"

    parameters = {
        'n_samples, n_features': [
            (100, 500)
        ],
    }

    def __init__(self, n_samples=10, n_features=50, random_state=27):
        # Store the parameters of the dataset
        self.n_samples = n_samples
        self.n_features = n_features
        self.random_state = random_state

    def get_data(self):
        rng = np.random.RandomState(self.random_state)

        X, y, _ = make_correlated_data(self.n_samples, self.n_features,
                                       random_state=rng)

        data = dict(X=X, y=y)

        return data
