import pandas as pd
import matplotlib.pyplot as plt

def plot_csv_data(file_path, y_column, y_data, plot_title, output_file):
    # Load the data from CSV file
    data = pd.read_csv(file_path)
    
    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data[y_data], marker='', linestyle='-')
    plt.title(plot_title)
    plt.xlabel('Time (Seconds)')
    plt.ylabel(y_column)
    plt.grid(True)
    
    # Save the plot to a file
    plt.savefig(output_file)
    plt.close()  # Close the plot to free up memory


plot_csv_data("e.csv",'error rate', 'Average','Average error rate per rollout second - RED','error_plot.png')

plot_csv_data("d.csv",'ms', 'Average','Average Duration per rollout second - RED','duration_plot.png')

plot_csv_data("r.csv",'Requests', 'Average','Average Rate of traffic per second - RED','rate_plot.png')


#plot_csv_data("duration_normal.csv",'error rate', 'Average','Average error rate per rollout second','error_plot.png')
#
#plot_csv_data("duration_normal.csv",'ms', 'Average','Average duration per rollout second','duration_plot.png')
#
#plot_csv_data("latencyhttp-saturation-golden.csv",'CPU seconds', 'Average','Average cpu seconds per second','saturation_plot.png')
#
##plot_csv_data("latencyhttp-traffic-golden.csv",'Traffic', 'Average','Average requests per second','traffic_plot.png')


