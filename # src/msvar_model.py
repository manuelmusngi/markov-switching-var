# msvar_model.py
import numpy as np
import pandas as pd
from statsmodels.tsa.vector_ar.msvar import MSVAR

class NaturalGasMarketMSVAR:
    """
    A class to represent and analyze the US natural gas market using a
    Markov Switching Vector Autoregressive (MS-VAR) model.
    """

    def __init__(self, data: pd.DataFrame, variables: list, n_regimes: int, lag_order: int):
        """
        Initializes the model.

        Args:
            data (pd.DataFrame): Time series data.
            variables (list): List of variables for the model.
            n_regimes (int): Number of regimes.
            lag_order (int): Number of lags in the VAR.
        """
        self.data = data
        self.variables = variables
        self.n_regimes = n_regimes
        self.lag_order = lag_order
        self.model = None
        self.results = None

    def build_model(self):
        """Builds the MS-VAR model."""

        self.model = MSVAR(
            self.data, k_regimes=self.n_regimes, lags=self.lag_order,
            switching_vars=self.variables
        )

    def fit_model(self, **kwargs):
        """Fits the MS-VAR model."""
        if self.model is None:
            raise ValueError("Model not built. Call build_model() first.")
        self.results = self.model.fit(**kwargs)

    def analyze_regimes(self):
        """Analyzes the characteristics of the regimes."""

        if self.results is None:
            raise ValueError("Model not fitted. Call fit_model() first.")

        print("\n--- Regime Analysis ---")
        print("Transition Matrix:\n", self.results.markov_chain.P)

        for i in range(self.n_regimes):
            print(f"\nRegime {i + 1}:")
            print("Parameters:\n", self.results.params_by_regime[i])
            print("Covariance:\n", self.results.sigma_by_regime[i])

    def get_impulse_responses(self, impulse_var: str, response_var: str, periods: int = 10):
        """
        Calculates impulse response functions.

        Args:
            impulse_var (str): Variable to shock.
            response_var (str): Variable to observe the response.
            periods (int): Number of periods for the IRF.

        Returns:
            np.ndarray: The impulse response function.
        """

        if self.results is None:
            raise ValueError("Model not fitted. Call fit_model() first.")

        impulse_index = self.variables.index(impulse_var)
        response_index = self.variables.index(response_var)
        irfs = []
        for i in range(self.n_regimes):
            irf = self.results.impulse_responses(irf_periods=periods, regime=i)
            irfs.append(irf[:, response_index, impulse_index])
        return irfs
