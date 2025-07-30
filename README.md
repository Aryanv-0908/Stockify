# Stockify

**An Interactive Stock Price Forecasting Dashboard with LSTM Deep Learning Models**

Stockify is a dynamic web application built with Streamlit that provides animated, real-time stock price predictions using Long Short-Term Memory (LSTM) neural networks. The dashboard offers an intuitive interface for exploring historical stock data and visualizing future price forecasts for major US companies.

---

## 🚀 Features

- Interactive Stock Selection: Choose from 5 major companies (AAPL, MSFT, GOOGL, TSLA, AMZN)  
- LSTM-Powered Predictions: Pre-trained deep learning models for accurate 30-day price forecasting  
- Animated Visualizations: Day-by-day animated reveal of stock price predictions  
- Real-time Data Display: Historical price trends with forecasted overlays  
- Customizable Controls: Adjustable forecast length and animation speed  
- Responsive Design: Clean, modern UI with interactive Plotly charts  
- Comprehensive Analysis: Display of key metrics including last observed and predicted prices

---

## 🛠️ Tech Stack

- Frontend: Streamlit  
- Data Science: TensorFlow/Keras, scikit-learn, pandas, numpy  
- Visualization: Plotly, Matplotlib  
- Machine Learning: LSTM Neural Networks  
- Data Source: Yahoo Finance (via yfinance)

---

## 📊 Models & Data

- 5 Pre-trained LSTM Models: Individual models for each stock ticker  
- Historical Data: 3+ years of cleaned stock price data  
- Technical Indicators: Moving averages and other analytical features  
- Forecast Horizon: 30-day predictions with recursive forecasting

---

## 🔧 Installation

1. **Clone the repository:**

   git clone https://github.com/yourusername/Stockify.git

   cd Stockify

3. **Create a virtual environment:**

   python -m venv env


3. **Activate the virtual environment:**

- On Windows:
  ```
  env\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source env/bin/activate
  ```

4. **Install dependencies:**

   pip install -r requirements.txt


5. **Run the Streamlit application:**

   streamlit run app.py

   
6. The app will automatically open in your default web browser. Use the sidebar controls to select stocks and customize the forecast horizon.


## 🌐 Live Demo

Stockify is deployed and accessible online via Streamlit Community Cloud:

[**🔗 View the Live Application on Streamlit**]([https://stockify-your-url.streamlit.app](https://stockify-impjjtykzpkoeazeys6jlr.streamlit.app/))

---

## ⚠️ Disclaimer

This project is intended for educational and demonstration purposes only. Stock price predictions are based on historical data and modeled estimates using machine learning and should **not** be used for real investment decisions. Past performance does not guarantee future results.

---

## 🤝 Contributing

Contributions are welcome! Please submit issues or pull requests for improvements, bug fixes, or new features.

---

## 📄 License

This project is open source and available under the MIT License. See the LICENSE file for details.

---

## 📧 Contact

For questions or feedback, please open an issue or contact [your email or GitHub profile].

---









