import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_pred = np.array(y_pred, dtype=float)
    y_true = np.array(y_true, dtype=float)
    
    func = np.sum((y_pred - y_true) ** 2) / len(y_true)

    return float(func)
