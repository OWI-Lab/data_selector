import matplotlib.pyplot as plt
import numpy as np


def generate_noisy_sinusoidal(num_samples=10000, frequency=5, noise_level=0.5, x_end = 2 * np.pi):
    """
    Generate a noisy sinusoidal dataset.

    Parameters:
    num_samples (int): Number of samples in the dataset.
    frequency (float): Frequency of the sinusoidal signal.
    noise_level (float): Standard deviation of the Gaussian noise added to the signal.

    Returns:
    tuple: (x, y_noisy) where x is the array of x values and y_noisy is the array of noisy y values.
    """
    x = np.linspace(0, x_end, num_samples)  # X values
    y_true = np.sin(frequency * x)  # True sinusoidal values
    noise = np.random.normal(0, noise_level, num_samples)  # Gaussian noise
    y_noisy = y_true + noise  # Sinusoidal data with noise

    return x, y_noisy

def flatten_signal(signal, start_flatten, end_flatten, noise_level=0.1):
    """
    Flatten the signal between start_flatten and end_flatten.

    Parameters:
    signal (np.ndarray): Array of signal values.
    start_flatten (int): Index of the starting point of the signal to flatten.
    end_flatten (int): Index of the ending point of the signal to flatten.

    Returns:
    np.ndarray: Flattened signal.
    """
    num_samples = len(signal)
    signal_flat = signal.copy()
    noise = np.random.normal(0, noise_level, num_samples)  # Gaussian noise
    signal_flat[start_flatten:end_flatten] = signal[start_flatten] + noise[start_flatten:end_flatten]
    return signal_flat