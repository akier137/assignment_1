import numpy as np

class MultipleLinearRegression:
    def __init__(self):
        # Private attribute for coefficients
        self._coefficients = None  

    def train(self, X, y):
        """
        Trains the multiple linear regression model.

        Args:
            X: Input matrix as a numpy array.
            y: Target values.
        """

        # Add a column of ones to the feature matrix for the intercept term
        ones_column = np.ones((X.shape[0], 1))
        X_with_intercept = np.concatenate((ones_column, X), axis=1)
        
        # Calculate intermediate values for the normal equation
        X_transpose_dot_X = X_with_intercept.T.dot(X_with_intercept)
        inverse_X_transpose_dot_X = np.linalg.inv(X_transpose_dot_X)
        X_transpose_dot_y = X_with_intercept.T.dot(y)
        
        # Calculate the coefficients using the normal equation: w* = (((X^T)X)^-1)(X^T)y
        self._coefficients = inverse_X_transpose_dot_X.dot(X_transpose_dot_y)

    def predict(self, X):
        """
        Predicts target values based on input features.

        Args:
            X: Input feature matrix as a numpy array.

        Returns:
            Predicted target values as a numpy array, or None if no coefficients.
        """
        # Check if coefficients have been trained
        if self._coefficients is None:
            return None

        # Add a column of ones to the feature matrix for the intercept term
        ones_column = np.ones((X.shape[0], 1))
        X_with_intercept = np.concatenate((ones_column, X), axis=1)
        
        # Make predictions using the dot product of feature matrix and coefficients
        y_pred = X_with_intercept.dot(self._coefficients)
        return y_pred
