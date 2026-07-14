# Neural Network Intrusion Detection System (IDS)

This project implements a machine learning-based Intrusion Detection System (IDS) using a neural network to identify malicious network activity. The system is trained on the NSL-KDD dataset, a benchmark cybersecurity dataset containing both normal and attack-related network traffic records.

The project preprocesses network traffic data, encodes categorical network features, normalizes numerical features, and trains a neural network classifier to distinguish between normal and malicious traffic. Once trained, the model evaluates unseen traffic and generates alerts when suspicious activity is detected.

Key Features:

* Data preprocessing and feature engineering
* One-hot encoding of categorical network features
* Feature normalization using StandardScaler
* Binary classification of network traffic (normal vs. attack)
* Neural network implementation using TensorFlow/Keras
* Performance evaluation using precision, recall, F1-score, and confusion matrix
* Simulated alert generation for detected malicious traffic

Technologies Used:

* Python
* TensorFlow/Keras
* Pandas
* NumPy
* Scikit-Learn

Results:
The model achieved approximately 99% accuracy, precision, recall, and F1-score on the NSL-KDD test dataset while maintaining low false positive and false negative rates.

This project demonstrates the application of machine learning techniques to cybersecurity problems and provides a foundation for more advanced IDS systems and Security Operations Center (SOC) workflows.

# Commends
The dataset was provided from the github repository at: https://github.com/jmnwong/NSL-KDD-Dataset.
Lots of concepts and code help came from GeeksForGeeks and some help from ChatGPT.