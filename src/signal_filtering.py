import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt

# Bandpass filter function
def bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data)

def process_signals():
    # Load synthetic data
    data = pd.read_csv('data/raw_data/synthetic_motion_data.csv')

    # Apply bandpass filters
    fs = 100  # Sampling frequency
    data['Breathing_Signal'] = bandpass_filter(data['Accel_Z (m/s^2)'], 0.1, 0.5, fs)
    data['Heartbeat_Signal'] = bandpass_filter(data['Accel_Z (m/s^2)'], 0.8, 3.0, fs)

    # Save processed signals
    data.to_csv('data/processed_data/processed_signals.csv', index=False)
    print("Signals processed and saved to 'data/processed_data/processed_signals.csv'.")

if __name__ == "__main__":
    process_signals()

