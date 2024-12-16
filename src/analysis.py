import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# Calculate RMSE
def calculate_rmse(original, modified):
    return np.sqrt(mean_squared_error(original, modified))

def analyze_results():
    # Load defense results
    data = pd.read_csv('results/defense_results.csv')

    # Calculate RMSE
    metrics = {
        'Breathing_Noise_RMSE': calculate_rmse(data['Breathing_Signal'], data['Breathing_Noise']),
        'Heartbeat_Noise_RMSE': calculate_rmse(data['Heartbeat_Signal'], data['Heartbeat_Noise']),
        'Breathing_Truncated_RMSE': calculate_rmse(data['Breathing_Signal'], data['Breathing_Truncated']),
        'Heartbeat_Truncated_RMSE': calculate_rmse(data['Heartbeat_Signal'], data['Heartbeat_Truncated']),
        'Breathing_Masked_RMSE': calculate_rmse(data['Breathing_Signal'], data['Breathing_Masked']),
        'Heartbeat_Masked_RMSE': calculate_rmse(data['Heartbeat_Signal'], data['Heartbeat_Masked']),
    }

    # Save metrics
    with open('results/metrics.txt', 'w') as f:
        for key, value in metrics.items():
            f.write(f"{key}: {value}\n")
    print("Analysis completed. Metrics saved to 'results/metrics.txt'.")

if __name__ == "__main__":
    analyze_results()

