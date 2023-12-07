import matplotlib.pyplot as plt
import numpy as np

class RegressionPlotter:
    def __init__(self):
        pass
    
    def plot_single_feature(self, X, y, model):

        """
        Plot a single feature against the target variable along with the regression line.

        Args:
        - X: Input feature data
        - y: Target variable data
        - model: Trained linear regression model

        Returns:
        - None or Plot: Depending on the availability of coefficients.
        """

        # Check if the model has been trained
        if model._coefficients is None:
            return None
        
        # Scatterplot
        plt.scatter(X, y, color='blue', label='Data')
        
        # Generate points for the regression line
        x_vals = np.linspace(min(X), max(X), 100)
        # The equation of a line
        y_vals = model._coefficients[1] * x_vals + model._coefficients[0] 
        
        # Plot the regression line
        plt.plot(x_vals, y_vals, color='red', label='Regression Line')
        
        # Labels and legend
        plt.xlabel('Feature')
        plt.ylabel('Target')
        plt.legend()
        
        # Show plot
        plt.show()
