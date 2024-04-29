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
       #------------Normal no injection ----------------
        #"error_rate_20240425144957_20240425145427.csv",
        #"error_rate_20240425162756_20240425163226.csv",
        #"error_rate_20240425163653_20240425164123.csv",
        #"error_rate_20240425171914_20240425172344.csv",
        #"error_rate_20240426094547_20240426095017.csv",
        #"error_rate_20240426095510_20240426095940.csv",
        #"error_rate_20240426102826_20240426103256.csv"
        #"http_traffic_20240425144957_20240425145427.csv",
        #"http_traffic_20240425162756_20240425163226.csv",
        #"http_traffic_20240425163653_20240425164123.csv",
        #"http_traffic_20240425171914_20240425172344.csv",
        #"http_traffic_20240426094547_20240426095017.csv",
        #"http_traffic_20240426095510_20240426095940.csv",
        #"http_traffic_20240426102826_20240426103256.csv"
        #"latency_20240425144957_20240425145427.csv",
        #"latency_20240425162756_20240425163226.csv",
        #"latency_20240425163653_20240425164123.csv",
        #"latency_20240425171914_20240425172344.csv",
        #"latency_20240426094547_20240426095017.csv",
        #"latency_20240426095510_20240426095940.csv",
        #"latency_20240426102826_20240426103256.csv"
        #"saturation_20240426102826_20240426103256.csv",
        #"saturation_20240426095510_20240426095940.csv",
        #"saturation_20240426094547_20240426095017.csv",
        #"saturation_20240425171914_20240425172344.csv",
        #"saturation_20240425163653_20240425164123.csv",
        #"saturation_20240425162756_20240425163226.csv",
        #"saturation_20240425144957_20240425145427.csv"

        #--------- httpfault---------------
        #"error_rate_20240427161231_20240427161500.csv",
        #"error_rate_20240427161623_20240427161837.csv",
        #"error_rate_20240427162116_20240427162302.csv",
        #"error_rate_20240427163928_20240427164142.csv",
        #"error_rate_20240427164240_20240427164450.csv",
        #"error_rate_20240427164702_20240427164929.csv",
        #"error_rate_20240427165331_20240427165537.csv"
        #"http_traffic_20240427161231_20240427161500.csv",
        #"http_traffic_20240427161623_20240427161837.csv",
        #"http_traffic_20240427162116_20240427162302.csv",
        #"http_traffic_20240427163928_20240427164142.csv",
        #"http_traffic_20240427164240_20240427164450.csv",
        #"http_traffic_20240427164702_20240427164929.csv",
        #"http_traffic_20240427165331_20240427165537.csv"

        #"latency_20240427165331_20240427165537.csv",
        #"latency_20240427161231_20240427161500.csv",
        #"latency_20240427161623_20240427161837.csv",
        #"latency_20240427162116_20240427162302.csv",
        #"latency_20240427163928_20240427164142.csv",
        #"latency_20240427164240_20240427164450.csv",
        #"latency_20240427164702_20240427164929.csv"

        #"saturation_20240427165331_20240427165537.csv",
        #"saturation_20240427161231_20240427161500.csv",
        #"saturation_20240427161623_20240427161837.csv",
        #"saturation_20240427162116_20240427162302.csv",
        #"saturation_20240427163928_20240427164142.csv",
        #"saturation_20240427164240_20240427164450.csv",
        #"saturation_20240427164702_20240427164929.csv"

        #----------Latency data
        #"error_rate_20240427232044_20240427232452.csv",
        #"error_rate_20240427233142_20240427233518.csv",
        #"error_rate_20240427232550_20240427232956.csv",
        #"error_rate_20240427231524_20240427231932.csv",
        #"error_rate_20240427233630_20240427234038.csv",
        #"error_rate_20240427234142_20240427234550.csv",
        #"error_rate_20240427234726_20240427235134.csv"

        #"http_traffic_20240427232044_20240427232452.csv",
        #"http_traffic_20240427232550_20240427232956.csv",
        #"http_traffic_20240427231524_20240427231932.csv",
        #"http_traffic_20240427233142_20240427233518.csv",
        #"http_traffic_20240427233630_20240427234038.csv",
        #"http_traffic_20240427234142_20240427234550.csv",
        #"http_traffic_20240427234726_20240427235134.csv"
        #"latency_20240427232044_20240427232452.csv",
        #"latency_20240427231524_20240427231932.csv",
        #"latency_20240427232550_20240427232956.csv",
        #"latency_20240427233142_20240427233518.csv",
        #"latency_20240427233630_20240427234038.csv",
        #"latency_20240427234142_20240427234550.csv",
        #"latency_20240427234726_20240427235134.csv"
        #"saturation_20240427231524_20240427231932.csv",
        #"saturation_20240427232044_20240427232452.csv",
        #"saturation_20240427232550_20240427232956.csv",
        #"saturation_20240427233142_20240427233518.csv",
        #"saturation_20240427233630_20240427234038.csv",
        #"saturation_20240427234142_20240427234550.csv",
        #"saturation_20240427234726_20240427235134.csv"
        #--------- latency / http 
        #"error_rate_20240428104101_20240428104309.csv",
        #"error_rate_20240428104533_20240428104749.csv",
        #"error_rate_20240428104853_20240428105029.csv",
        #"error_rate_20240428105525_20240428105733.csv",
        #"error_rate_20240428105949_20240428110149.csv",
        #"error_rate_20240428110317_20240428110541.csv",
        #"error_rate_20240428111133_20240428111311.csv"
        #"http_traffic_20240428104101_20240428104309.csv",
        #"http_traffic_20240428104533_20240428104749.csv",
        #"http_traffic_20240428104853_20240428105029.csv",
        #"http_traffic_20240428105525_20240428105733.csv",
        #"http_traffic_20240428105949_20240428110149.csv",
        #"http_traffic_20240428110317_20240428110541.csv",
        #"http_traffic_20240428111133_20240428111311.csv"
        #"latency_20240428104101_20240428104309.csv",
        #"latency_20240428104533_20240428104749.csv",
        #"latency_20240428104853_20240428105029.csv",
        #"latency_20240428105525_20240428105733.csv",
        #"latency_20240428105949_20240428110149.csv",
        #"latency_20240428110317_20240428110541.csv",
        #"latency_20240428111133_20240428111311.csv"
        #"saturation_20240428104101_20240428104309.csv",
        #"saturation_20240428104533_20240428104749.csv",
        #"saturation_20240428104853_20240428105029.csv",
        #"saturation_20240428105525_20240428105733.csv",
        #"saturation_20240428105949_20240428110149.csv",
        #"saturation_20240428110317_20240428110541.csv",
        #"saturation_20240428111133_20240428111311.csv"

        #RED
        #"red_duration_20240426102826_20240426103256.csv",
        #"red_duration_20240426095510_20240426095940.csv",
        #"red_duration_20240426094547_20240426095017.csv",
        #"red_duration_20240425171914_20240425172344.csv",
        #"red_duration_20240425163653_20240425164123.csv",
        #"red_duration_20240425162756_20240425163226.csv",
        #"red_duration_20240425144957_20240425145427.csv"

        # HTTP FAULT RED
        #"red_duration_20240429105105_20240429105317.csv",
        #"red_duration_20240429105405_20240429105617.csv",
        #"red_duration_20240429105726_20240429105923.csv",
        #"red_duration_20240429110029_20240429110226.csv",
        #"red_duration_20240429110311_20240429110523.csv",
        #"red_duration_20240429110611_20240429110838.csv",
        #"red_duration_20240429111348_20240429111617.csv"

        #"red_error_rate_20240429105405_20240429105617.csv",
        #"red_error_rate_20240429105726_20240429105923.csv",
        #"red_error_rate_20240429110029_20240429110226.csv",
        #"red_error_rate_20240429105105_20240429105317.csv",
        #"red_error_rate_20240429110311_20240429110523.csv",
        #"red_error_rate_20240429110611_20240429110838.csv",
        #"red_error_rate_20240429111348_20240429111617.csv"

        #"red_http_traffic_20240429105105_20240429105317.csv",
        #"red_http_traffic_20240429105405_20240429105617.csv",
        #"red_http_traffic_20240429105726_20240429105923.csv",
        #"red_http_traffic_20240429110029_20240429110226.csv",
        #"red_http_traffic_20240429110311_20240429110523.csv",
        #"red_http_traffic_20240429110611_20240429110838.csv",
        #"red_http_traffic_20240429111348_20240429111617.csv"

        # duration RED
       # "red_duration_20240429112020_20240429112432.csv",
       # "red_duration_20240429112538_20240429113005.csv",
       # "red_duration_20240429113412_20240429113826.csv",
       # "red_duration_20240429113908_20240429114320.csv",
       # "red_duration_20240429114402_20240429114829.csv",
       # "red_duration_20240429114941_20240429115353.csv",
       # "red_duration_20240429115508_20240429115902.csv",
        #"red_error_rate_20240429112020_20240429112432.csv",
        #"red_error_rate_20240429112538_20240429113005.csv",
        #"red_error_rate_20240429113412_20240429113826.csv",
        #"red_error_rate_20240429113908_20240429114320.csv",
        #"red_error_rate_20240429114402_20240429114829.csv",
        #"red_error_rate_20240429114941_20240429115353.csv",
        #"red_error_rate_20240429115508_20240429115902.csv",
        #"red_http_traffic_20240429112020_20240429112432.csv",
        #"red_http_traffic_20240429112538_20240429113005.csv",
        #"red_http_traffic_20240429113412_20240429113826.csv",
        #"red_http_traffic_20240429113908_20240429114320.csv",
        #"red_http_traffic_20240429114402_20240429114829.csv",
        #"red_http_traffic_20240429114941_20240429115353.csv",
        #"red_http_traffic_20240429115508_20240429115902.csv"


        # DURATION AND HTTP
        #"red_duration_20240429122008_20240429122220.csv",
        #"red_duration_20240429122956_20240429123153.csv",
        #"red_duration_20240429123250_20240429123447.csv",
        #"red_duration_20240429123608_20240429123850.csv",
        #"red_duration_20240429123941_20240429124138.csv",
        #"red_duration_20240429124226_20240429124508.csv",
        #"red_duration_20240429124605_20240429124802.csv",

       # "red_error_rate_20240429122008_20240429122220.csv",
       # "red_error_rate_20240429122956_20240429123153.csv",
       # "red_error_rate_20240429123250_20240429123447.csv",
       # "red_error_rate_20240429123608_20240429123850.csv",
       # "red_error_rate_20240429123941_20240429124138.csv",
       # "red_error_rate_20240429124226_20240429124508.csv",
       # "red_error_rate_20240429124605_20240429124802.csv",

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