# OLS Linear Regression on Diabetes Dataset

A beginner-friendly linear regression project using the Diabetes dataset from `scikit-learn`. This project demonstrates how to fit an Ordinary Least Squares (OLS) regression model using a single feature — Body Mass Index (BMI) — to predict disease progression in diabetic patients.

The project includes model training, evaluation, and visualization using Python libraries like `scikit-learn`, `numpy`, and `matplotlib`.

## What the Project Does

- Loads the Diabetes dataset (built into `scikit-learn`)
- Selects one feature (BMI) to train the regression model
- Splits the data into training and testing sets
- Fits an OLS linear regression model
- Predicts disease progression for the test set
- Evaluates the model using Mean Squared Error and R² score
- Visualizes the results with a scatter plot and regression line

## Skills Demonstrated

- Feature selection & model training using `scikit-learn`
- Model evaluation (MSE, R²)
- Data visualization with `matplotlib`
- Saving plots to a file

## Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

**requirements.txt:**

```
scikit-learn
matplotlib
numpy
```

## How to Run the Project

1. Clone this repository or navigate to the project folder:

```
git clone https://github.com/yourusername/ml-projects.git
cd ml-projects/ols-diabetes-regression
```

2. (Optional but recommended) Create and activate a virtual environment:

```
python -m venv venv
.\env\Script\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Run the script:

```
python ols_diabetes.py
```

This will:
- Train the model
- Print metrics to the console
- Generate and save `plot.png`
- Display a scatter plot + regression line

## Sample Output (Terminal)

```
Mean squared error: 2548.07
Coefficient (slope): [941.43]
Intercept: 153.40
R² score: 0.47
```

## Dataset

This project uses the **Diabetes dataset** built into `scikit-learn`. It includes:
- 10 baseline medical features (age, sex, BMI, etc.)
- A target value indicating disease progression one year later
- 442 total patient records

Only one feature (BMI) is used in this univariate regression example.

## Folder Structure

```
ols-diabetes-regression/
├── ols_diabetes.py        # Python script
├── requirements.txt       # Dependencies
├── plot.png               # Output plot (created on run)
└── README.md              # Project documentation
```

## Future Enhancements

- Add multivariate regression using all features
- Compare with Ridge/Lasso regression
- Add residual plots and confidence intervals
- Deploy using Streamlit

---

