**Investment Prediction With GUI**
**Project Overview**
This project aims to predict stock prices using historical data and visualize the trends using a graphical user interface (GUI). The project involves data collection, preprocessing, model training, prediction, and visualization. The machine learning model is built using LSTM (Long Short-Term Memory) networks, and the GUI is created using Streamlit.

**Table of Contents**
Introduction
Installation
Usage
Project Structure
Model Training
GUI
Contributing
License
**Introduction**
The goal of this project is to predict the closing prices of a given stock based on historical data. We utilize LSTM, a type of recurrent neural network, to capture the temporal dependencies in the stock price data. The project also includes a GUI for easy interaction with the model and visualization of the results.

**Installation**
To run this project, you need to have Python installed on your machine. Follow the steps below to set up the project:

Clone the repository:
git clone https://github.com/AkshayGarude/Investment_Prediction_With-GUI.git
cd Investment_Prediction_With-GUI

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required dependencies:
pip install -r requirements.txt

Usage
Follow the steps below to run the project:

Data Collection and Preprocessing:

The main code for data collection and preprocessing is in Stock_Test.ipynb. This script downloads historical stock data using the Yahoo Finance API, preprocesses it, and trains an LSTM model.

Model Training:

Run the Jupyter Notebook to train the model. The trained model will be saved as keras_model.h5.

Running the GUI:

To launch the GUI, run the following command:
streamlit run app.py

This will start a Streamlit server and open the GUI in your web browser.

Project Structure :
Investment_Prediction_With-GUI/
├── Stock_Test.ipynb         # Jupyter Notebook for data processing and model training
├── app.py                   # Streamlit application for the GUI
├── requirements.txt         # List of dependencies
└── keras_model.h5           # Saved model

Model Training
The model training is done using the following steps:

Download Historical Data: Download historical stock data using the Yahoo Finance API.
Data Preprocessing: Normalize the data and create sequences for training the LSTM model.
Train LSTM Model: Train the LSTM model using the training data.
Save the Model: Save the trained model to a file for later use.
GUI
The GUI is built using Streamlit. It allows users to input a stock ticker symbol, fetch historical data, calculate moving averages, and visualize the stock price trends. The GUI also displays the real-time stock price.

Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss changes or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
