# Replication Project (Classification ML with Bias Mitigation using Medical Expenditure data)

## Overview
This dataset provides insights into mental and physical health across different ages. By analyzing the results, we can better target specific groups based on their health scores. For example, if there is a correlation between age/demographics and physical health, we can focus efforts on improving decisions for those groups. This could lead to more efficient resource allocation, like reducing wait times. However, errors in the data/models could have significant real-world impacts, affecting patients, providers, insurers, and policymakers. It is crucial the predictions are accurate to properly direct resources and support.

## Requirements
- Packages: Python 3.6+, `aif360`, `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `tensorflow (if using Adversarial Debiasing)`, `cvxpy (if using Optimized Preprocessing)`, `Docker (optional, but recommended)`

## Setup Instructions
You can set up the project using either a pre-built Docker image or by running the code directly on your local machine.

## Data Setup
The file `h181.csv` is required to run the project but is too large to include in the repository.

You can download the file from [https://drive.google.com/file/d/1GESPjTTEgwczg4AJVGqvzLJsFhBZky7f/view?usp=drive_link] and place it in the `data/raw/` directory, or you can generate it using the `generate_data.py` script by running:


## Option 1: Using the Pre-Built Docker Image
To simplify the setup process, you can use the pre-built Docker image available in the GitHub Container Registry.

1. **Pull the Pre-Built Docker Image:**
   ```bash
   docker pull ghcr.io/gracejiang0929/ridehailing-bias-image:latest

2. **Run the Docker Container:**
   ```bash
   docker run -it --rm -v $(pwd):/app ghcr.io/gracejiang0929/ridehailing-bias-image:latest

- This command:
   - Starts the container.
   - Mounts your current project directory ($(pwd)) to the /app directory in the container.
   - Automatically removes the container after it stops (--rm).

3. **Run the Project Inside the Container:** Once the container is running, you can execute scripts inside it. For example:
   ```bash
   python run.py
   
4. **Start Jupyter Notebook (if needed):**
   ```bash
   jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

Access it in your browser at http://localhost:8888.

## Option 2: Build and Run Locally
If you'd like to run the project directly on your local machine:

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
     ```
   - If you plan to use the Optimized Preprocessing algorithm:
     ```bash
     pip install cvxpy
     ```
5. Launch Jupyter Notebook:
   ```bash
   jupyter notebook

6. Open the Notebook:
   In the Jupyter interface, navigate to `pt3-bias-mitigation.ipynb` and open it.

7. Run the Notebook:
   Execute the cells sequentially to perform bias mitigation analysis.


## Running the Notebook
1. Start Jupyter Notebook: If you're running the project locally or inside Docker, start Jupyter Notebook:
   ```bash
   jupyter notebook

2. Open `pt3-bias-mitigation.ipynb`:
- Navigate to the file `pt3-bias-mitigation.ipynb` in the Jupyter interface and open it.

3. Execute Cells Sequentially:
- Run each cell step by step by pressing `Shift + Enter`. Follow the outputs to perform bias mitigation analysis.

   
