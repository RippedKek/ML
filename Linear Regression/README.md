# Linear Regression

Linear Regression is a **supervised learning** algorithm used to predict a **continuous dependent variable** (output) based on one or more independent variables (features). The goal is to find the best-fit line (also known as the regression line) that minimizes the differences between the predicted values and the actual values.

## Types of Linear Regression
1. **Simple Linear Regression**: When there is only one independent variable.
2. **Multiple Linear Regression**: When there are two or more independent variables.

## Simple Linear Regression
In simple linear regression, we assume a linear relationship between the input variable `X` and the output `Y`. The model is represented by the following equation:

\[
Y = b_0 + b_1 \cdot X
\]

Where:
- `Y`: Dependent variable (output).
- `X`: Independent variable (input).
- `b_0`: Intercept (the value of `Y` when `X = 0`).
- `b_1`: Slope (how much `Y` changes for a one-unit change in `X`).

### Example:
Suppose we want to predict house prices (`Y`) based on their size (`X`). The regression line will help determine the price of a house for any given size.

## Multiple Linear Regression
In multiple linear regression, we have more than one input variable (features). The model is represented by the following equation:

\[
Y = b_0 + b_1 \cdot X_1 + b_2 \cdot X_2 + ... + b_n \cdot X_n
\]

Where:
- `X_1, X_2, ..., X_n`: Independent variables (features).
- `b_0`: Intercept.
- `b_1, b_2, ..., b_n`: Coefficients (how each feature affects the target).

### Example:
In predicting house prices, the independent variables can include house size (`X1`), the number of bedrooms (`X2`), and the age of the house (`X3`).

## Assumptions of Linear Regression
For linear regression to work well, the following assumptions should hold:
1. **Linearity**: The relationship between the independent and dependent variables is linear.
2. **Independence**: The observations in the dataset are independent of each other.
3. **Homoscedasticity**: The variance of residuals (errors) is constant across all levels of the independent variable.
4. **No Multicollinearity**: In multiple linear regression, the independent variables should not be too highly correlated with each other.
5. **Normality**: The residuals (differences between observed and predicted values) are normally distributed.

## Cost Function
The **cost function** for linear regression is the **Mean Squared Error (MSE)**, which measures the average of the squared differences between the predicted and actual values:

\[
MSE = \frac{1}{n} \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2
\]

Where:
- `n`: Number of observations.
- `Y_i`: Actual value of the dependent variable.
- `\hat{Y}_i`: Predicted value from the linear model.

## Gradient Descent
To minimize the cost function and find the optimal values of the coefficients (`b_0`, `b_1`, ..., `b_n`), we can use **gradient descent**. The idea is to adjust the parameters in the direction that reduces the error, updating them iteratively as follows:

\[
b_j = b_j - \alpha \cdot \frac{\partial}{\partial b_j} MSE
\]

Where:
- `\alpha`: Learning rate (controls how large the steps are during each iteration).
- `\frac{\partial}{\partial b_j} MSE`: The gradient of the cost function with respect to `b_j`.

## Evaluation Metrics
Once the model is trained, we can evaluate its performance using various metrics:
1. **R-squared (R²)**: Indicates the proportion of the variance in the dependent variable that is predictable from the independent variables. Ranges from 0 to 1, with values closer to 1 indicating a better fit.
   
   \[
   R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
   \]
   Where:
   - `SS_{res}`: Sum of squared residuals (errors).
   - `SS_{tot}`: Total sum of squares (variation in `Y`).
   
2. **Mean Absolute Error (MAE)**: Measures the average of the absolute differences between the predicted and actual values.
   
   \[
   MAE = \frac{1}{n} \sum_{i=1}^{n} |Y_i - \hat{Y}_i|
   \]

3. **Root Mean Squared Error (RMSE)**: The square root of the MSE, which penalizes larger errors more than MAE.

   \[
   RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2}
   \]

## Advantages of Linear Regression
- Simple and easy to implement.
- Interpretable, as coefficients show the relationship between variables.
- Works well when the relationship between input and output is linear.

## Disadvantages of Linear Regression
- Assumes a linear relationship, which may not always hold in real-world scenarios.
- Sensitive to outliers, which can skew the regression line.
- Not suitable for complex relationships or datasets with many features.

## Use Cases
- Predicting housing prices based on size, number of rooms, and location.
- Estimating sales revenue based on advertising expenditure.
- Predicting the salary of employees based on years of experience, education level, etc.
