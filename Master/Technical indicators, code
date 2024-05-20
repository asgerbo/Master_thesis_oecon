import pandas as pd
import ta

#load csv and name value variable
df = pd.read_csv('/Users/Danni/Downloads/usd_eur_exchange.csv')

exchange_rate_column = 'Close'


#convert "." values to NaN by making it nummeric
df[exchange_rate_column] = pd.to_numeric(df[exchange_rate_column], errors='coerce')

#interpolating NaNs from previous and next value
df[exchange_rate_column].interpolate(method='linear', inplace=True)

#Simple Moving Averages, 10, 20, 50.
df['SMA_10'] = ta.trend.sma_indicator(df[exchange_rate_column], window=10)
df['SMA_20'] = ta.trend.sma_indicator(df[exchange_rate_column], window=20)
df['SMA_50'] = ta.trend.sma_indicator(df[exchange_rate_column], window=50)

#Exponential Moving Average, 20
df['EMA_20'] = ta.trend.ema_indicator(df[exchange_rate_column], window=20)

#Relative Strength Index
df['RSI'] = ta.momentum.rsi(df[exchange_rate_column], window=14)

#Bollinger Bands
bb_indicator = ta.volatility.BollingerBands(df[exchange_rate_column], window=20, window_dev=2)
df['BB_High'] = bb_indicator.bollinger_hband()
df['BB_Low'] = bb_indicator.bollinger_lband()
df['BB_Middle'] = bb_indicator.bollinger_mavg()

#MACD, 12 and 24
df['MACD_12'] = ta.trend.macd(df[exchange_rate_column], window_slow=26, window_fast=12)
df['MACD_Signal_12'] = ta.trend.macd_signal(df[exchange_rate_column], window_slow=26, window_fast=12)
df['MACD_Diff_12'] = ta.trend.macd_diff(df[exchange_rate_column], window_slow=26, window_fast=12)

df['MACD_24'] = ta.trend.macd(df[exchange_rate_column], window_slow=52, window_fast=24)
df['MACD_Signal_24'] = ta.trend.macd_signal(df[exchange_rate_column], window_slow=52, window_fast=24)
df['MACD_Diff_24'] = ta.trend.macd_diff(df[exchange_rate_column], window_slow=52, window_fast=24)



#manually calculate Fibonacci (den her fungerer først hvis vi highs of lows values)
def calculate_fibonacci_levels(df, exchange_rate_column):
    max_price = df[exchange_rate_column].max()
    min_price = df[exchange_rate_column].min()
    diff = max_price - min_price
    
    level1 = max_price - 0.236 * diff
    level2 = max_price - 0.382 * diff
    level3 = max_price - 0.618 * diff

    return level1, level2, level3

level1, level2, level3 = calculate_fibonacci_levels(df, exchange_rate_column)
df['Fib_23.6'] = level1
df['Fib_38.2'] = level2
df['Fib_61.8'] = level3

#show dataframe
print(df.head())

#saving file
df.to_csv('/Users/Danni/Downloads/usd_eur_exchange_with1_indicators.csv', index=False)



#Average True Range - kræver high og lows igen
df['ATR'] = ta.volatility.average_true_range(df['High'], df['Low'], df[exchange_rate_column], window=14)

#Stochastic Oscillator - kræver high og lows igen
df['Stoch'] = ta.momentum.stoch(df['High'], df['Low'], df[exchange_rate_column], window=14, smooth_window=3)
df['Stoch_Signal'] = ta.momentum.stoch_signal(df['High'], df['Low'], df[exchange_rate_column], window=14, smooth_window=3)

#Parabolic SAR - kræver high og lows igen
df['Parabolic_SAR'] = ta.trend.psar(df['High'], df['Low'], df[exchange_rate_column])
