import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Load TSLA dataset
# df = pd.read_csv("TSLA_data.csv", index_col="Date", parse_dates=True)
df = pd.read_csv("TSLA_data.csv", skiprows=1)  # Skip first row if it's an extra header
print(df.columns)  # Print first 5 rows to verify structure


# Keep only 'Close' price for prediction
df = df[['TSLA.4']].astype(float)  # Replace 'TSLA.4' with the actual column name
df.rename(columns={'TSLA.4': 'Close'}, inplace=True)  # Rename it to 'Close' for consistency



# Normalize data for LSTM (scale values between 0 and 1)
scaler = MinMaxScaler(feature_range=(0,1))
df_scaled = scaler.fit_transform(df)

# Convert back to DataFrame
df_scaled = pd.DataFrame(df_scaled, index=df.index, columns=["Close"])

# Plot the normalized closing price
plt.figure(figsize=(12, 6))
plt.plot(df_scaled, label="Normalized TSLA Closing Price", color="blue")
plt.title("Normalized TSLA Stock Price")
plt.xlabel("Date")
plt.ylabel("Scaled Price")
plt.legend()
plt.show()

# Save the preprocessed data
df_scaled.to_csv("TSLA_data_preprocessed.csv")
print("✅ Data preprocessed and saved as TSLA_data_preprocessed.csv")
