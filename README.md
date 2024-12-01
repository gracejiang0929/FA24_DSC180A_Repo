# Replication Project (Classification ML with Bias Mitigation using Medical Expenditure data)

## Overview
This dataset provides insights into mental and physical health across different ages. By analyzing the results, we can better target specific groups based on their health scores. For example, if there is a correlation between age/demographics and physical health, we can focus efforts on improving decisions for those groups. This could lead to more efficient resource allocation, like reducing wait times. However, errors in the data/models could have significant real-world impacts, affecting patients, providers, insurers, and policymakers. It is crucial the predictions are accurate to properly direct resources and support.

## Requirements
- Packages:
  - aif360
  - numpy
  - pandas
  - scikit-learn
  - matplotlib
  - jupyter
  - tensorflow (if using Adversarial Debiasing)
  - cvxpy (if using Optimized Preprocessing)
   - Python 3.9+
   - Docker (optional, but recommended)

## Setup Instructions

To get started with the project, follow these steps:

1. Clone the Repository
   Clone this repository to your local machine using the following command: 
   
   ```bash
   git clone https://github.com/gracejiang0929/FA24_DSC180A_Repo.git
   cd FA24_DSC180A_Repo

2. Create a Virtual Environment (Optional but Recommended):
   ```bash
   python -m venv venv
   # Activate the virtual environment:
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt

4. Additional Dependencies:
   - If you plan to use the Adversarial Debiasing algorithm:
   ```bash
   pip install tensorflow
   
  - If you plan to use the Optimized Preprocessing algorithm:
   ```bash
   pip install cvxpy

5. Launch Jupyter Notebook:
   ```bash
   jupyter notebook

6. Open the Notebook:
   In the Jupyter interface, navigate to `pt3-bias-mitigation.ipynb` and open it.

7. Run the Notebook:
   Execute the cells sequentially to perform bias mitigation analysis.
   
