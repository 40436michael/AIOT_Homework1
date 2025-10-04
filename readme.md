# Simple Linear Regression Web App

## Live Demo

[https://aiothomework1-u6eygc2ddkkvuesvuv7mkx.streamlit.app/](https://aiothomework1-u6eygc2ddkkvuesvuv7mkx.streamlit.app/)

---

This project is a simple web application that demonstrates a linear regression model. It is built using Python and Streamlit, and it follows the CRISP-DM methodology.

## Description

The application allows users to interactively explore the effect of different parameters on a simple linear regression model. Users can adjust the slope of the underlying line, the amount of noise in the data, and the number of data points, and see how the model's fit and performance change in real-time.

## Features

-   Interactive sliders for adjusting model parameters:
    -   Slope (`a`)
    -   Noise
    -   Number of data points
-   Real-time visualization of:
    -   The generated data points
    -   The "true" underlying line
    -   The fitted linear regression line
-   Display of model evaluation metrics:
    -   Mean Squared Error (MSE)
    -   Fitted slope and intercept

## Running Locally

1.  **Prerequisites:** Make sure you have Python installed.
2.  **Installation:** Clone the repository and install the dependencies:

    ```bash
    git clone <your-repo-url>
    cd <repo-folder>
    pip install -r requirements.txt
    ```

3.  **Execution:** To run the application, execute the following command in your terminal:

    ```bash
    streamlit run app.py
    ```

## Deployment on Streamlit Share

This application is ready to be deployed on Streamlit Share.

1.  **Upload to GitHub:** Create a new public repository on GitHub and upload `app.py` and `requirements.txt`.

2.  **Deploy on Streamlit:**
    -   Go to [share.streamlit.io](https://share.streamlit.io/).
    -   Click on "Deploy an app" and connect your GitHub account.
    -   Select the repository and the `app.py` file.
    -   Click "Deploy".

## CRISP-DM Process

This project was developed following the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology. The detailed process, from business understanding to deployment, is documented in the `log.md` file.

## Technologies Used

-   Python
-   Streamlit
-   scikit-learn
-   NumPy
-   Matplotlib
