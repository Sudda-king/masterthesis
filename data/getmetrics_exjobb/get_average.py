import pandas as pd

def calculate_row_averages(file_list):
    # Load data from all files, considering only the second column
    data_frames = [pd.read_csv(file, header=None, usecols=[1]) for file in file_list]
    # Concatenate all dataframes by columns to align corresponding rows
    concatenated_data = pd.concat(data_frames, axis=1)
    # Calculate the average across all columns for each row
    row_averages = concatenated_data.mean(axis=1)
    return row_averages

def main():
    # List of file paths to your CSV files
    file_paths = [
       

        "red_http_traffic_20240429122008_20240429122220.csv",
        "red_http_traffic_20240429122956_20240429123153.csv",
        "red_http_traffic_20240429123250_20240429123447.csv",
        "red_http_traffic_20240429123608_20240429123850.csv",
        "red_http_traffic_20240429123941_20240429124138.csv",
        "red_http_traffic_20240429124226_20240429124508.csv",
        "red_http_traffic_20240429124605_20240429124802.csv"

    ]
    
    # Calculate row averages for all provided files
    row_averages = calculate_row_averages(file_paths)
    
    # Create a DataFrame from the row averages
    averages_df = pd.DataFrame({
        "Row Index": row_averages.index + 1,
        "Average": row_averages
    })
    
    # Define the output path for the averaged values CSV
    output_path = "path_to_output.csv"
    
    # Save the DataFrame to a new CSV file
    averages_df.to_csv(output_path, index=False)
    print(f"Row averages saved to {output_path}")

if __name__ == "__main__":
    main()
