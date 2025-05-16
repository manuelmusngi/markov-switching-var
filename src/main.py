# main.py
import pandas as pd
from src.data_loader import load_natural_gas_data, preprocess_data
from src.msvar_model import NaturalGasMarketMSVAR
from src.visualization import plot_regime_probabilities, plot_impulse_responses
from src.analysis import compare_regime_means

# Main execution block
if __name__ == "__main__":
    # 1. Load and Preprocess Data
    data_file = 'data/natural_gas_data.csv'  # Adjust if needed
    raw_data = load_natural_gas_data(data_file)

    if raw_data is not None:
        variables_to_analyze = ['production', 'price', 'demand']  # Adjust
        processed_data = preprocess_data(raw_data, variables_to_analyze)

        # 2.  Instantiate and Build the MS-VAR Model
        n_regimes = 4  # Based on the paper's findings
        lag_order = 2  # Example lag order
        msvar_model = NaturalGasMarketMSVAR(processed_data, variables_to_analyze, n_regimes, lag_order)
        msvar_model.build_model()

        # 3. Fit the Model
        try:
            msvar_model.fit_model(max_iter=200, disp=True)  # Adjust fitting parameters

            # 4. Analyze Results
            msvar_model.analyze_regimes()

            # 5. Visualize Results
            plot_regime_probabilities(msvar_model.results, processed_data.index)

            # Impulse Response Analysis
            for imp_var in variables_to_analyze:
                for resp_var in variables_to_analyze:
                    if imp_var != resp_var:
                        irfs = msvar_model.get_impulse_responses(imp_var, resp_var, periods=15)
                        plot_impulse_responses(irfs, variables_to_analyze, imp_var, resp_var)

            compare_regime_means(msvar_model.results, variables_to_analyze)

        except Exception as e:
            print(f"Error during model execution: {e}")
