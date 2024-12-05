# Replication Project (Classification ML with Bias Mitigation using Medical Expenditure data)

## Overview
This dataset provides insights into mental and physical health across different ages. By analyzing the results, we can better target specific groups based on their health scores. For example, if there is a correlation between age/demographics and physical health, we can focus efforts on improving decisions for those groups. This could lead to more efficient resource allocation, like reducing wait times. However, errors in the data/models could have significant real-world impacts, affecting patients, providers, insurers, and policymakers. It is crucial the predictions are accurate to properly direct resources and support.

## Requirements
- Packages: Python 3.6+, `aif360`, `numpy`, `pandas`, `scikit-learn`, `matplotlib`

## Setup Instructions
You can set up the project using either a pre-built Docker image or by running the code directly on your local machine.

## Build and Run Locally
If you'd like to run the project directly on your local machine:

1. Clone the Repository
   Clone this repository to your local machine using the following command: 
   
   ```bash
   git clone https://github.com/gracejiang0929/FA24_DSC180A_Repo.git
   cd FA24_DSC180A_Repo

2. Create a Virtual Environment (Optional but Recommended):
   ```bash
   python -m venv venv
   
- Activate the Virtual Environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate

   - On Windows:
     ```bash
     venv\Scripts\activate

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt

4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook

6. Open the Notebook:
   In the Jupyter interface, navigate to `pt3-bias-mitigation.ipynb` and open it.

7. Run the Notebook:
   Execute the cells sequentially to perform bias mitigation analysis.

## Data Setup
The file `h181.csv` is required to run the project but is too large to include in the repository.

You can download the file from [https://drive.google.com/file/d/1GESPjTTEgwczg4AJVGqvzLJsFhBZky7f/view?usp=drive_link] and place it in the `data/raw/` directory.

*IMPORTANT* **In order to run Section 3. Model Development without Debiasing, you need to follow below steps:**

1. Install R:
   - If you don't have R installed, you can download it from CRAN.
   - If you're using macOS, you can install R using Homebrew:
      ```bash
      brew install R
2. Run the `generate_data.py` Script:
   - Navigate to the fold scripts where the script is located (cd scripts).
   - Run the following command to execute the R script:
      ```bash 
      Rscript generate_data.py
   - This script will download the necessary data files, extract them, and save them as CSV files (including `h181.csv`).

## Running the Notebook
1. Start Jupyter Notebook: If you're running the project locally or inside Docker, start Jupyter Notebook:
   ```bash
   jupyter notebook

2. Open `pt3-bias-mitigation.ipynb`:
- Navigate to the file `pt3-bias-mitigation.ipynb` in the Jupyter interface and open it.

3. Execute Cells Sequentially:
- Run each cell step by step by pressing `Shift + Enter`. Follow the outputs to perform bias mitigation analysis.
