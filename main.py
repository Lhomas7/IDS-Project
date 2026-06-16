from src.preprocess import load_and_preprocess
from src.model import build_model
from src.train import train_model
from src.evaluate import evaluate_model
from src.alerts import generate_alert

def main():
    # Load and preprocess data
    X_train, X_test, y_train, y_test = load_and_preprocess("data/KDDTrain+.txt")

    # Build model
    model = build_model(X_train.shape[1])

    # Train model
    history = train_model(model, X_train, y_train)

    # Evaluate model
    y_pred = evaluate_model(model, X_test, y_test)

    # Generate alerts for first 10 samples
    print("\n--- Sample Alerts ---")
    probs = model.predict(X_test[:10])

    """for p in probs:
        pred = int(p > 0.5)
        generate_alert(pred, float(p))"""
    for confidence in probs.flatten():
        pred = int(confidence > 0.5)
        generate_alert(pred, confidence)

if __name__ == "__main__":
    main()