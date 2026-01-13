import matplotlib.pyplot as plt
from graphviz import Source
from IPython.display import Image, display
from matplotlib.axes import Axes
from matplotlib.colors import ListedColormap, rgb2hex
from numpy import concatenate, number, unique, vstack
from numpy.typing import NDArray
from sklearn.base import ClassifierMixin
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def plot_boundary(
    classifier: ClassifierMixin,
    X_train: NDArray[number],
    X_test: NDArray[number],
    y_train: NDArray[number],
    y_test: NDArray[number],
    title: str = "Decision Boundary For Classifier",
    ax: Axes | None = None,
) -> Axes | None:
    n_classes = len(unique(concatenate([y_train, y_test])))

    if n_classes == 2:
        colors = ["#FF0000", "#0000FF"]
    elif n_classes == 3:
        colors = ["tab:blue", "tab:green", "tab:orange"]
    else:
        colors = [rgb2hex(plt.get_cmap("tab10")(i)) for i in range(n_classes)]

    if ax is None:
        _, ax = plt.subplots()

    kwargs = {
        "xlabel": r"$x_1$",
        "ylabel": r"$x_2$",
        "alpha": 0.8,
        "ax": ax,
    }

    if n_classes == 2:
        kwargs["cmap"] = plt.get_cmap("RdBu")
    else:
        kwargs["multiclass_colors"] = colors

    DecisionBoundaryDisplay.from_estimator(
        classifier, vstack([X_train, X_test]), **kwargs
    )

    cm_bright = ListedColormap(colors)
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolor="k")
    ax.scatter(
        X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, edgecolor="k", alpha=0.6
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


def plot_model_size(df, column, models, ax=None, markers=None, colors=None):
    if markers is None:
        markers = ["o", "s", "^", "D", "v", "<", ">", "p"]
    if colors is None:
        colors = ["blue", "red", "green", "orange", "purple", "brown", "pink", "gray"]

    if ax is None:
        _, ax = plt.subplots(figsize=(8, 6))

    for i, model_name in enumerate(models.keys()):
        ax.plot(
            df[column],
            df[model_name.replace("$", "")],
            f"{markers[i % len(markers)]}--",
            color=colors[i % len(colors)],
            label=model_name,
        )
    ax.set_xlabel(f"Number of {column.strip('n_').capitalize()}")
    ax.set_ylabel("Model Size (KB)")
    ax.set_title("Model Size Comparison")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.legend(loc="upper left")

    if ax is None:
        plt.tight_layout()
        plt.show()
