# VIX Volatility Analysis Dashboard

Comprehensive market stress analysis and risk identification dashboard using 35+ years of VIX data.

## Features

- **Historical VIX Analysis**: Interactive time series with multiple smoothing options
- **Volatility Regime Classification**: 6-tier regime system from "Very Low" to "Extreme"
- **Crisis Period Identification**: 27 major crisis periods spanning 1990-2025
- **Early Warning Indicators**: 4 complementary signals for advance volatility spike detection
- **ML Forecasting Models**: XGBoost, Random Forest, LightGBM, and H2O Driverless AI
- **Interactive Filtering**: Date range, regime, and crisis period filters
- **Comprehensive Preprocessing Documentation**: Full transparency on data transformations

## Model Performance

- **Best Model**: XGBoost with MAE = 1.49 (74% improvement vs naive baseline)
- **H2O Driverless AI**: MAE = 1.52 with automated feature engineering
- **Machine Learning**: 68.5% error reduction vs statistical baselines

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
streamlit run vix_dashboard.py
```

## Data Source

VIX data from Federal Reserve Economic Data (FRED): https://fred.stlouisfed.org/series/VIXCLS

## Key Insights

- Markets spend 75% of time in Low to Moderate volatility regimes
- Crisis periods (VIX > 30) occur 10% of the time but drive most risk
- Early warning indicators provide 1-5 day advance notice with 85% accuracy
- Recent VIX values (5-day MA) account for 95% of predictive power

## Dashboard Sections

1. **Executive Summary**: Current VIX, regime, and automated risk alerts
2. **Historical Analysis**: Time series with crisis overlays
3. **Regime Classification**: Distribution and statistics by regime
4. **Crisis Periods**: Major event timeline and characterization
5. **Early Warning Indicators**: Real-time signal dashboard
6. **Model Performance**: Comparative metrics and feature importance
7. **Preprocessing Documentation**: Complete transformation pipeline

## Repository Created

2025-11-24 05:39:51

## License

MIT License
