import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:
    b = np.arange(len(predicted_probs))
    true_class = np.argmax(true_labels, axis=1)
    target_pred = predicted_probs[b, true_class]
    target_pred = np.clip(target_pred, epsilon, 1.0)
    loss = -np.log(target_pred)

    return np.mean(loss)