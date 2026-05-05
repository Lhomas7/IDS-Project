#This file will contain code necessary for generating alerts depending on the type of traffic

def generate_alert(prediction, confidence):
    if prediction == 1:
        print(f"[ALERT] Malicious traffic detected | Confidence: {confidence:.2f}")
    else:
        print("[INFO] Normal traffic")

#run and test 
probs = model.predict(X_test[:10])

for p in probs:
    pred = int(p > 0.5)
    generate_alert(pred, float(p))