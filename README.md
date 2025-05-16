#### Markov-Switching-VAR
This application, inspired by the research paper "Understanding the US Natural Gas Market: A Markov Switching VAR Approach," aims to model and analyze the dynamic behavior of the US natural gas market. [cite: 1] Utilizing the methodology of the paper, the application will employ a Markov Switching Vector Autoregressive (MS-VAR) model to identify distinct periods or "regimes" within the market's history. [cite: 1]

The core functionality will involve:

- Identifying market regimes: Based on statistical modeling, the application will attempt to delineate different states the natural gas market has experienced over time, similar to the four regimes identified in the paper using Bayesian model comparison. [cite: 1]
- Analyzing regime-dependent responses: Once regimes are identified, the application will analyze how key variables in the natural gas market (such as production, price, and potentially demand) respond to fundamental shocks (like supply or demand shifts) differently in each regime. This echoes the paper's finding that the market's sensitivity to shocks changed after the 1989 Decontrol Act. [cite: 1]
- Investigating the role of specific shocks: Following the paper's findings, the application will explore the impact of natural gas demand and price shocks on production, and the extent to which natural gas prices are driven by specific demand factors. [cite: 1]
- Assessing the influence of oil prices: If augmented with oil price data (as done in the paper), the application will also analyze the regime-dependent impact of crude oil price shocks on natural gas prices. [cite: 1, 32, 34]

In essence, this application seeks to replicate and potentially extend the analysis of the provided research paper by building a computational tool to understand the shifting dynamics and shock responses within the US natural gas market across different identified regimes.

#### Project structure
NaturalGasMSVAR/\
├── data/\
│ └── natural_gas_data.csv\
├── src/\
│ ├── __init__.py\
│ ├── [data_loader.py](https://github.com/manuelmusngi/Markov-Switching-VAR/blob/main/src/data_loader.py)\
│ ├── [msvar_model.py](https://github.com/manuelmusngi/Markov-Switching-VAR/blob/main/src/msvar_model.py)\
│ ├── [analysis.py](https://github.com/manuelmusngi/Markov-Switching-VAR/blob/main/src/analysis.py)\
│ ├── [visualization.py](https://github.com/manuelmusngi/Markov-Switching-VAR/blob/main/src/visualization.py)\
│ └── [main.py](https://github.com/manuelmusngi/Markov-Switching-VAR/blob/main/src/main.py)\
├── notebooks/\
│ └── analysis_notebook.ipynb\
├── reports/\
│ └── analysis_report.txt\
└── requirements.txt

#### Dependencies
  - [requirements.txt](https://github.com/manuelmusngi/Markov-Switching-VAR/blob/main/requirements.txt)

#### References
- [Understanding the US Natural Gas Market: A Markov Switching VAR Approach](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3156000)

#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).
