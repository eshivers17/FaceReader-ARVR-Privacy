import pandas as pd
import numpy as np

# Noise injection
def add_noise(data, noise_level=0.5):
    return data + noise_level * np.random.randn(len(data))

# Truncation
def truncate_data(data, decimals=1):
    return np.round(data, decimals=decimals)

# Encryption simulation (masking)
def mask_data(data, mask_fraction=0.5):
    mask = np.random.choice([0, 1], size=len(data), p=[mask_fraction, 1 - mask_fraction])
    return data * mask

def apply_defenses():
    # Load processed data
    data = pd.read_csv('data/processed_data/processed_signals.csv')

    # Apply defenses
    data['Breathing_Noise'] = add_noise(data['Breathing_Signal'])
    data['Heartbeat_Noise'] = add_noise(data['Heartbeat_Signal'])
    data['Breathing_Truncated'] = truncate_data(data['Breathing_Signal'])
    data['Heartbeat_Truncated'] = truncate_data(data['Heartbeat_Signal'])
    data['Breathing_Masked'] = mask_data(data['Breathing_Signal'])
    data['Heartbeat_Masked'] = mask_data(data['Heartbeat_Signal'])

    # Save results
    data.to_csv('results/defense_results.csv', index=False)
    print("Defenses applied and saved to 'results/defense_results.csv'.")

if __name__ == "__main__":
    apply_defenses()

