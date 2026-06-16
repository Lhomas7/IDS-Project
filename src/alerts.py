#This file will contain code necessary for generating alerts depending on the type of traffic

def generate_alert(prediction, confidence):
    if prediction == 1:
        print(f"[ALERT] Malicious traffic detected | Confidence: {confidence:.2f}")
    else:
        print("[INFO] Normal traffic")
