from pickle import dumps

import numpy as np
import polars as pl


def calculate_model_size(
    models,
    param,
    param_values,
    fixed_samples=100,
    fixed_features=100,
    random_state=None,
):
    rng = np.random.default_rng(random_state)
    results = []

    for value in param_values:
        params = {
            "n_samples": value if param == "n_samples" else fixed_samples,
            "n_features": value if param == "n_features" else fixed_features,
        }

        X = rng.random([params["n_samples"], params["n_features"]])
        y = rng.integers(0, 3, params["n_samples"])

        row = {param: value}
        for model_name, model in models.items():
            fitted_model = model.fit(X, y)
            size = round(len(dumps(fitted_model)) / 1024, 3)
            row[model_name.replace("$", "")] = size

        results.append(row)
    return pl.DataFrame(results)
