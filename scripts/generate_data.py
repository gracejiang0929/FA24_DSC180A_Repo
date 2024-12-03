import pandas as pd
import numpy as np
import os

def generate_data():
    # Example: Simulating data based on some rules
    num_rows = 10000
    data = {
        'column1': np.random.randint(0, 100, size=num_rows),
        'column2': np.random.choice(['A', 'B', 'C', 'D'], size=num_rows),
        'column3': np.random.normal(loc=50, scale=10, size=num_rows)
    }

    df = pd.DataFrame(data)

    # Define output path
    output_dir = 'data/raw'
    output_file = f'{output_dir}/h181.csv'

    # Make sure the directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save the data to CSV
    df.to_csv(output_file, index=False)
    print(f"Data has been generated and saved to {output_file}")

if __name__ == "__main__":
    generate_data()
