# src/analysis.py
import numpy as np
import pandas as pd
from src.msvar_model import NaturalGasMarketMSVAR  # Import the class

def compare_regime_means(msvar_results, variables: list):
    """
    (Example)  Compares the mean values of variables across regimes.

    Args:
        msvar_results:  The results object from the MS-VAR model.
        variables (list): List of variables to compare
    """

    if msvar_results is None:
        raise ValueError("Model results are not available.")

    print("\n--- Comparison of Regime Means ---")
    for i, var in enumerate(variables):
        print(f"\nVariable: {var}")
        for regime in range(msvar_results.model.k_regimes):
            #  Access the parameters; you might need to adjust this depending on how
            #  statsmodels stores the means. This is a placeholder.
            mean_in_regime = msvar_results.params_by_regime[regime][i]
            print(f"  Regime {regime + 1}: Mean = {mean_in_regime:.4f}")
