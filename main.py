import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from multiple_linear_regression import MultipleLinearRegression
from regression_plotter import RegressionPlotter

def main():
    # Generating sample data using sklearn
    X, y = make_regression(n_samples=100, n_features=2, noise=0.1, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Creating and training the MultipleLinearRegression model
    model = MultipleLinearRegression()
    model.train(X_train, y_train)

    # Creating a RegressionPlotter instance
    plotter = RegressionPlotter()

    # Testing plot_single_feature method
    print("Testing plot_single_feature:")
    try:
        plotter.plot_single_feature(X_train[:, 0], y_train, model)
        print("plot_single_feature executed successfully.")
    except Exception as e:
        print("Error occurred in plot_single_feature:", e)

    # Testing plot_two_features method
    print("\nTesting plot_two_features:")
    try:
        plotter.plot_two_features(X_train[:, 0], X_train[:, 1], y_train, model)
        print("plot_two_features executed successfully.")
    except Exception as e:
        print("Error occurred in plot_two_features:", e)

if __name__ == "__main__":
    main()