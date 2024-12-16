import numpy as np
import pandas as pd

# Generate synthetic AR/VR motion sensor data
def generate_data():
    time = np.linspace(0, 20, 2000)  # 20 seconds of data at 100 Hz
    acc_x = 2 * np.sin(2 * np.pi * 0.5 * time) + 0.5 * np.random.randn(2000)
    acc_y = 2 * np.cos(2 * np.pi * 0.5 * time) + 0.5 * np.random.randn(2000)
    acc_z = 3 * np.random.randn(2000)
    gyro_x = 1 * np.random.randn(2000)
    gyro_y = 1.5 * np.random.randn(2000)
    gyro_z = 2 * np.random.randn(2000)

    # Create DataFrame
    data = pd.DataFrame({
        'Time (s)': time,
        'Accel_X (m/s^2)': acc_x,
        'Accel_Y (m/s^2)': acc_y,
        'Accel_Z (m/s^2)': acc_z,
        'Gyro_X (rad/s)': gyro_x,
        'Gyro_Y (rad/s)': gyro_y,
        'Gyro_Z (rad/s)': gyro_z
    })

    # Save to CSV
    data.to_csv('data/raw_data/synthetic_motion_data.csv', index=False)
    print("Synthetic data generated and saved to 'data/raw_data/synthetic_motion_data.csv'.")

if __name__ == "__main__":
    generate_data()

