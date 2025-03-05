import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Load preprocessed data
df = pd.read_csv("TSLA_data_preprocessed.csv", index_col=0)

# Convert dataframe to numpy array
data = df.values

# Define sequence length (time steps for prediction)
seq_length = 50  

# Create sequences for training
X, y = [], []
for i in range(len(data) - seq_length):
    X.append(data[i:i+seq_length])  # Past 50 days as input
    y.append(data[i+seq_length])    # Next day price as output

X, y = np.array(X), np.array(y)

# Split into training and testing sets (80% train, 20% test)
split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Build LSTM model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(seq_length, 1)),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(25),
    Dense(1)  # Output layer (predict stock price)
])

model.compile(optimizer="adam", loss="mse")

# Train the model
history = model.fit(X_train, y_train, epochs=20, batch_size=16, validation_data=(X_test, y_test))

# Plot training loss
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.title("LSTM Training Loss")
plt.show()

# Save the trained model
model.save("lstm_tsla_model.h5")
print("✅ LSTM model trained and saved as lstm_tsla_model.h5")
