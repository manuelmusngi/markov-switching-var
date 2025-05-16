# visualization.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_regime_probabilities(msvar_results, data_index):
    """
    Plots the smoothed probabilities of each regime over time.

    Args:
        msvar_results: The results object from the MS-VAR model.
        data_index (pd.DatetimeIndex): The time index for the data.
    """
    if msvar_results is None:
        raise ValueError("Model results are not available.")

    smoothed_probs = msvar_results.smoothed_marginal_probabilities
    plt.figure(figsize=(12, 6))
    for i in range(msvar_results.model.k_regimes):
        plt.plot(data_index, smoothed_probs[:, i], label=f'Regime {i + 1}')
    plt.title('Smoothed Regime Probabilities')
    plt.xlabel('Time')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_impulse_responses(irfs, variables: list, impulse_var: str, response_var: str):
    """
    Plots impulse response functions for each regime.

    Args:
        irfs (list): List of impulse response functions (one for each regime).
        variables (list): List of all variables in the model.
        impulse_var (str): The variable that receives the shock.
        response_var (str): The variable responding to the shock.
    """

    num_regimes = len(irfs)
    time_periods = np.arange(1, irfs[0].shape[0] + 1)  # Assuming irfs are numpy arrays

    plt.figure(figsize=(12, 6))
    for i, irf in enumerate(irfs):
        plt.plot(time_periods, irf, label=f'Regime {i + 1}')

    plt.title(f'Impulse Response of {response_var} to {impulse_var} Shock')
    plt.xlabel('Periods')
    plt.ylabel('Response')
    plt.legend()
    plt.grid(True)
    plt.show()
