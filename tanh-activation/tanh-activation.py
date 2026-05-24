import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)

    func = (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))
    return func