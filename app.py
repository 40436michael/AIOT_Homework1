import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def generate_data(a, n_points, noise):
    """
    Generates synthetic data for linear regression.

    Args:
        a (float): The slope of the line.
        n_points (int): The number of data points.
        noise (float): The amount of random noise to add.

    Returns:
        tuple: A tuple containing X and y numpy arrays.
    """
    b = 5  # Fixed intercept for simplicity
    X = np.linspace(0, 10, n_points).reshape(-1, 1)
    y_true = a * X + b
    y_noisy = y_true + np.random.normal(0, noise, n_points).reshape(-1, 1)
    return X, y_noisy

def train_model(X, y):
    """
    Trains a linear regression model.

    Args:
        X (np.ndarray): The input features.
        y (np.ndarray): The target variable.

    Returns:
        LinearRegression: The trained linear regression model.
    """
    model = LinearRegression()
    model.fit(X, y)
    return model

def evaluate_model(model, X, y):
    """
    Evaluates the linear regression model.

    Args:
        model (LinearRegression): The trained model.
        X (np.ndarray): The input features.
        y (np.ndarray): The target variable.

    Returns:
        float: The mean squared error of the model.
    """
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    return mse

st.title("Simple Linear Regression with CRISP-DM")

# CRISP-DM: Deployment
st.header("Interactive Demo")

# User inputs
st.sidebar.header("Model Parameters")
a = st.sidebar.slider("Slope (a)", -10.0, 10.0, 2.5, 0.1)
noise = st.sidebar.slider("Noise", 0.0, 10.0, 2.0, 0.1)
n_points = st.sidebar.slider("Number of Points", 50, 500, 100, 10)

# Generate data
X, y = generate_data(a, n_points, noise)

# Train model
model = train_model(X, y)

# Evaluate model
mse = evaluate_model(model, X, y)

# Get model coefficients
model_a = model.coef_[0][0]
model_b = model.intercept_[0]

# Plot results
st.header("Results")
fig, ax = plt.subplots()
ax.scatter(X, y, label="Generated Data")
ax.plot(X, a * X + 5, color='g', linestyle='--', label="True Line")
ax.plot(X, model.predict(X), color='r', label="Fitted Line")
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)

# Display evaluation metrics
st.header("Evaluation")
st.write(f"Mean Squared Error: {mse:.2f}")
st.write(f"Fitted Slope (a): {model_a:.2f} (True: {a})")
st.write(f"Fitted Intercept (b): {model_b:.2f} (True: 5)")