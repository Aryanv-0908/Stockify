import streamlit as st
import pandas as pd
import time
import plotly.graph_objs as go

st.set_page_config(page_title="Stockify – 1-Month LSTM Stock Forecast", layout="wide")
st.markdown(
    """
    <style>
    .big-font {
        font-size:32px !important;
        font-weight: bold;
    }
    .small-font {
        font-size:18px !important;
        color: #666;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='big-font'>📈 Stockify: 1-Month LSTM Stock Forecast 🚀</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='small-font'>Compare and interact with LSTM-powered stock forecasts for top US companies.</div>",
    unsafe_allow_html=True,
)

st.sidebar.header("Stock Selection & Settings")
stocks = ["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN"]
forecast_files = {
    "AAPL": "AAPL_1_month_forecast.csv",
    "MSFT": "MSFT_1_month_forecast.csv",
    "GOOGL": "GOOGL_1_month_forecast.csv",
    "TSLA": "TSLA_1_month_forecast.csv",
    "AMZN": "AMZN_1_month_forecast.csv",
}
stock = st.sidebar.selectbox("Choose a stock:", stocks, index=0)
forecast_df = pd.read_csv(forecast_files[stock], parse_dates=["Date"])

hist = pd.read_csv("cleaned_stock_data.csv", header=[0, 1], index_col=0, parse_dates=True)
close = hist[("Close", stock)].dropna()
dates = close.index
prices = close.values

default_steps = 15 if len(forecast_df) > 15 else len(forecast_df)
forecast_days = st.sidebar.slider("Forecast length (days):", 1, len(forecast_df), default_steps, 1)

col1, col2 = st.columns(2)
with col1:
    st.metric("Last Observed Price", f"${round(prices[-1], 2)}")
with col2:
    st.metric(
        "Last Forecasted Price",
        f"${round(forecast_df['Predicted_Close'].iloc[:forecast_days].values[-1], 2)}",
    )

st.subheader(f"{stock}: Historical & 1-Month Forecast")
animation_speed = st.slider("Animation speed (seconds):", 0.05, 0.5, 0.15, 0.01)

plot_placeholder = st.empty()

for reveal in range(1, forecast_days + 1):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=dates,
            y=prices,
            name="Historical Close",
            mode="lines",
            line=dict(color="deepskyblue", width=2),
            hoverinfo="x+y",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=forecast_df["Date"][:reveal],
            y=forecast_df["Predicted_Close"][:reveal],
            name=f"Forecast (Days 1-{reveal})",
            mode="lines+markers",
            line=dict(dash="dash", color="red", width=2.5),
            marker=dict(size=7, color="red"),
            hoverinfo="x+y",
        )
    )
    fig.update_layout(
        height=500,
        template="plotly_white",
        xaxis=dict(title="Date"),
        yaxis=dict(title="Price (USD)"),
        legend=dict(x=0.01, y=0.99, bgcolor="rgba(0,0,0,0)"),
        showlegend=True,
        margin=dict(l=30, r=30, t=60, b=40),
    )
    plot_placeholder.plotly_chart(fig, use_container_width=True)
    time.sleep(animation_speed)

st.markdown(
    f"### 📊 Predicted Closing Prices for <span style='color:crimson'>{stock}</span>:",
    unsafe_allow_html=True,
)
st.dataframe(
    forecast_df.loc[: forecast_days - 1][["Date", "Predicted_Close"]].style.format(
        {"Predicted_Close": "${:.2f}"}
    ),
    use_container_width=True,
    hide_index=True,
)

st.markdown(
    """
    <hr>
    <div style='color:#888;font-size:16px'>
        Built with ❤️ by <b>Stockify</b><br>
        <i>All prices and forecasts are for educational & demo purposes.</i>
    </div>
    """,
    unsafe_allow_html=True,
)
