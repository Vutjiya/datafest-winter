from pickle import dumps

import matplotlib.pyplot as plt
import numpy as np
import polars as pl
from graphviz import Source
from IPython.display import Image, display
from matplotlib.axes import Axes
from matplotlib.colors import ListedColormap, rgb2hex
from numpy import concatenate, linspace, number, unique, vstack
from numpy.typing import NDArray
from sklearn.base import ClassifierMixin
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def view_boundary(
    classifier: ClassifierMixin,
    X_train: NDArray[number],
    X_test: NDArray[number],
    y_train: NDArray[number],
    y_test: NDArray[number],
    title: str = "Decision Boundary For Classifier",
    ax: Axes | None = None,
) -> Axes | None:
    n_classes = len(unique(concatenate([y_train, y_test])))
    base_colors = ["#FF0000", "#0000FF", "#FFFF00"]

    if n_classes <= len(base_colors):
        colors = base_colors[:n_classes]
    else:
        cmap = plt.get_cmap("tab10")
        extra_colors = cmap(linspace(0, 1, n_classes - len(base_colors)))
        colors = base_colors + [rgb2hex(c) for c in extra_colors]

    cm_bright = ListedColormap(colors)

    if ax is None:
        _, ax = plt.subplots()

    disp = DecisionBoundaryDisplay.from_estimator(
        classifier,
        vstack([X_train, X_test]),
        xlabel=r"$x_1$",
        ylabel=r"$x_2$",
        cmap=plt.get_cmap("RdBu"),
        alpha=0.8,
        ax=ax,
    )
    disp.ax_.scatter(
        X_train[:, 0],
        X_train[:, 1],
        c=y_train,
        cmap=cm_bright,
        edgecolor="k",
    )
    disp.ax_.scatter(
        X_test[:, 0],
        X_test[:, 1],
        c=y_test,
        cmap=cm_bright,
        edgecolor="k",
        alpha=0.6,
    )
    ax.set_title(title)

    if ax is None:
        plt.show()

    return ax


def print_decision_tree(decision_tree: DecisionTreeClassifier) -> None:
    dot_data = export_graphviz(
        decision_tree,
        feature_names=decision_tree.feature_names_in_.tolist(),
        class_names=[str(cls) for cls in decision_tree.classes_],
        filled=True,
        impurity=False,
        rounded=True,
        special_characters=True,
    )
    display(Image(Source(dot_data).pipe(format="png")))


def _calculate_model_size(
    models, varying_param, param_values, fixed_samples, fixed_features, rng
):
    results = []
    for value in param_values:
        n_samples = value if varying_param == "n_samples" else fixed_samples
        n_features = value if varying_param == "n_features" else fixed_features

        X = rng.random([n_samples, n_features])
        y = rng.integers(0, 3, n_samples)

        row = {varying_param: value}
        for model_name, model in models.items():
            fitted_model = model.fit(X, y)
            size_kb = round(len(dumps(fitted_model)) / 1024, 3)
            row[model_name.replace("$", "")] = size_kb

        results.append(row)
    return pl.DataFrame(results)


def _plot_model_size(ax, df, x_column, models, markers, colors):
    for i, model_name in enumerate(models.keys()):
        ax.plot(
            df[x_column],
            df[model_name.replace("$", "")],
            f"{markers[i % len(markers)]}--",
            color=colors[i % len(colors)],
            label=model_name,
        )
    ax.set_xlabel(f"Number of {x_column.strip('n_').capitalize()}")
    ax.set_ylabel("Model Size (KB)")
    ax.set_title("Model Size Comparison")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.legend(loc="upper left")


def view_model_size(
    models,
    param_values,
    n_samples=100,
    n_features=100,
    random_state=None,
):
    rng = np.random.default_rng(random_state)

    df_samples = _calculate_model_size(
        models, "n_samples", param_values, n_samples, n_features, rng
    )
    df_features = _calculate_model_size(
        models, "n_features", param_values, n_samples, n_features, rng
    )

    _, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    markers = ["o", "s", "^", "D", "v", "<", ">", "p"]
    colors = ["blue", "red", "green", "orange", "purple", "brown", "pink", "gray"]

    _plot_model_size(ax1, df_samples, "n_samples", models, markers, colors)
    _plot_model_size(ax2, df_features, "n_features", models, markers, colors)

    plt.tight_layout()
    plt.show()

    return df_samples, df_features
