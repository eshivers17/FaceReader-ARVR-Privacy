# FaceReader-ARVR-Privacy
Overview

This project evaluates privacy risks posed by AR/VR motion sensor data and explores defenses like noise injection, truncation, and encryption. It extends the FaceReader attack by testing motion-intensive scenarios and proposing solutions to mitigate sensitive data extraction.
Deliverables

    Source Code: Code for generating synthetic data, filtering signals, applying defenses, and analyzing results.
    Datasets: Synthetic motion sensor datasets (accelerometer, gyroscope) used for experimentation.
    Experiment Results: Graphs, RMSE comparisons, and detailed results from all defense mechanisms.
    Presentation Slides: Link to final presentation slides.
    Project Overview: This README file.

Instructions

    Setup:
    Clone the repository and install dependencies:

git clone <repo-link>  
cd project-name  
pip install -r requirements.txt  

Data Generation:
Run the following script to generate synthetic AR/VR motion sensor data:

python src/data_generation.py  

Signal Processing:
Apply bandpass filtering to extract breathing and heartbeat signals:

python src/signal_filtering.py  

Apply Defenses:
Run noise injection, truncation, and encryption:

python src/defenses.py  

Analyze Results:
Generate graphs and calculate RMSE values:

    python src/analysis.py  

Results

    Noise injection increased RMSE to ~0.50.
    Encryption resulted in significant RMSE (~49.31 for breathing), proving effective in obscuring signals.
    Truncation had minimal impact, with RMSE ~0.03.
