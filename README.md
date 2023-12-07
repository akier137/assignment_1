# OOP - 2023/24 - Assignment 1

This is the base repository for assignment 1.
Please follow the instructions given in the [PDF](https://brightspace.rug.nl/content/enforced/243046-WBAI045-05.2023-2024.1/2023_24_OOP.pdf) for the content of the exercise.

## How to carry out your assignment

Fork this repo on your private github account.
You can do so by clicking this button on the top-right panel:
![](fork.png) 

The assignment is divided into 4 blocks.
Block 1, 2, and 3 all define different classes.

Put the three classes in three separate files in the `src` folder, with the names specified in the PDF.
**Leave the __init__.py file untouched**.

Put the **main.py** script **outside** of the `src` folder, in the root of this repo.

Below this line, you can write your report to motivate your design choices.

## Submission

The code should be submitted on GitHub by opening a Pull Request from the branch you were working on to the `submission` branch.

There are automated checks that verify that your submission is correct:

1. Deadline - checks that the last commit in a PR was made before the deadline
2. Reproducibility - downloads libraries included in `requirements.txt` and runs `python3 src/main.py`. If your code does not throw any errors, it will be marked as reproducible.
3. Style - runs `flake8` on your code to ensure adherence to style guides.

---

## Your report
# Regression Analysis Project Report

## Design Choices Explanation

### `MultipleLinearRegression` Class:

- **Private Coefficients Attribute (`self._coefficients`):** This attribute is designated as private (`self._coefficients`) to encapsulate it within the class. Making it private prevents direct modification from external sources and ensures that it's accessed or modified only through class methods.

- **Train Method:** The `train` method computes the coefficients for the linear regression model using the normal equation. It prepares the input data by adding an intercept term, calculates intermediate values, and finally computes the coefficients.

- **Predict Method:** The `predict` method uses the trained coefficients to make predictions on new input data. It checks if coefficients exist before making predictions to prevent errors.

### `RegressionPlotter` Class:

- **Plot Single Feature Method:** This method visualizes a single feature against the target variable along with the regression line. It utilizes the coefficients from the trained model (`model._coefficients`) to plot the regression line.

## Usage and Execution:

The provided Python scripts demonstrate the following functionality:

- Generating sample data using `make_regression`.
- Training a `MultipleLinearRegression` model on the generated data.
- Showcasing prediction functionality and comparison with ground truth values.
- Using `RegressionPlotter` to visualize the regression line against a single feature.

## Conclusion:

The design choices prioritize encapsulation and modularity, allowing for easy extension or modification of functionality. The clear separation of concerns between the regression model, plotting, and data handling enhances code readability and maintainability.

