
from kubernetes.client.rest import ApiException
from prometheus_api_client import PrometheusConnect
import datetime
import matplotlib.pyplot as plt
import csv  

def unix_to_readable(timestamp):
    '''Converts Unix timestamp to a readable datetime string.'''
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

def write_to_csv(data, filename):
    '''Utility function to write data to a CSV file, converting timestamps to readable format.'''
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for entry in data:
            if 'values' in entry:
                for value_pair in entry['values']:
                    readable_timestamp = unix_to_readable(value_pair[0])
                    writer.writerow([readable_timestamp, value_pair[1]])

def get_http_traffic(start, end, filename):
    prom = PrometheusConnect(url="http://35.228.163.241:32546", disable_ssl=True)
    query = 'sum(rate(istio_requests_total{role="canary",destination_service=~"istio-rollout.rollouts-demo-istio.svc.cluster.local"}[1m]))'
    result = prom.custom_query_range(query=query, start_time=start, end_time=end, step=1)
    write_to_csv(result, filename)
    return result

def get_error( start, end, filename):
    prom = PrometheusConnect(url="http://35.228.163.241:32546", disable_ssl=True)
    query = 'sum(irate(istio_requests_total{role="canary", destination_service=~"istio-rollout.rollouts-demo-istio.svc.cluster.local", response_code!~"5.*"}[40s]))/sum(irate(istio_requests_total{role="canary",destination_service=~"istio-rollout.rollouts-demo-istio.svc.cluster.local"}[40s]))'
    result = prom.custom_query_range(query=query, start_time=start, end_time=end, step=1)
    write_to_csv(result, filename)
    return result

def get_latency( start, end, filename): # duration now
    prom = PrometheusConnect(url="http://35.228.163.241:32546", disable_ssl=True)
    query = '(sum(irate(istio_request_duration_milliseconds_sum{role ="canary",destination_service=~"istio-rollout.rollouts-demo-istio.svc.cluster.local"}[1m])) / sum(irate(istio_request_duration_milliseconds_count{role ="canary",destination_service=~"istio-rollout.rollouts-demo-istio.svc.cluster.local"}[1m]))) /1000'
    result = prom.custom_query_range(query=query, start_time=start, end_time=end, step=1)
    write_to_csv(result, filename)
    return result

def get_duration( start, end, filename): # duration now
    prom = PrometheusConnect(url="http://35.228.163.241:32546", disable_ssl=True)
    query = 'histogram_quantile(0.75, sum(irate(istio_request_duration_milliseconds_bucket{role="canary", destination_service=~"istio-rollout.rollouts-demo-istio.svc.cluster.local"}[1m]))by (le)) /1000'
    result = prom.custom_query_range(query=query, start_time=start, end_time=end, step=1)
    write_to_csv(result, filename)
    return result

def get_saturation( start, end, filename):
    prom = PrometheusConnect(url="http://35.228.163.241:32546", disable_ssl=True)
    query = 'rate(container_cpu_usage_seconds_total{namespace="rollouts-demo-istio",image="docker.io/sudda/latencyargo:latest",pod=~"istio-rollout-.*"}[1m])'
    result = prom.custom_query_range(query=query, start_time=start, end_time=end, step=1)
    write_to_csv(result, filename)
    return result

# Define the list of time intervals
time_intervals = [
    #------ Normal experiment golden signals--------
    #(datetime.datetime(2024, 4, 25, 14, 49, 57), datetime.datetime(2024, 4, 25, 14, 54, 27)),
    #(datetime.datetime(2024, 4, 25, 16, 27,56), datetime.datetime(2024, 4, 25, 16, 32,26)),
    #(datetime.datetime(2024, 4, 25, 16, 36,53), datetime.datetime(2024, 4, 25, 16, 41,23)),
    #(datetime.datetime(2024, 4, 25, 17, 19, 14), datetime.datetime(2024, 4, 25, 17, 23,44)),
    #(datetime.datetime(2024, 4, 26, 9, 45, 47), datetime.datetime(2024, 4, 26, 9, 50, 17)),
    #(datetime.datetime(2024, 4, 26, 9, 55, 10), datetime.datetime(2024, 4, 26, 9, 59, 40)),
    #(datetime.datetime(2024, 4, 26, 10, 28,26), datetime.datetime(2024, 4, 26, 10, 32,56))

    #-----HTTPFAULT experiment golden signals
    #(datetime.datetime(2024, 4, 27, 16, 12, 31), datetime.datetime(2024, 4, 27, 16, 15, 0)),
    #(datetime.datetime(2024, 4, 27, 16, 16, 23), datetime.datetime(2024, 4, 27, 16, 18, 37)),
    #(datetime.datetime(2024, 4, 27, 16, 21, 16), datetime.datetime(2024, 4, 27, 16, 23, 2)),
    #(datetime.datetime(2024, 4, 27, 16, 39, 28), datetime.datetime(2024, 4, 27, 16, 41,42)),
    #(datetime.datetime(2024, 4, 27, 16, 42, 40), datetime.datetime(2024, 4, 27, 16, 44, 50)),
    #(datetime.datetime(2024, 4, 27, 16, 47, 2), datetime.datetime(2024, 4, 27, 16, 49, 29)),
    #(datetime.datetime(2024, 4, 27, 16, 53,31), datetime.datetime(2024, 4, 27, 16, 55,37))

    #----------- latency experiment golden. 
    #(datetime.datetime(2024, 4, 27, 23, 15, 24), datetime.datetime(2024, 4, 27, 23, 19, 32)),
    #(datetime.datetime(2024, 4, 27, 23, 20, 44), datetime.datetime(2024, 4, 27, 23, 24, 52)),
    #(datetime.datetime(2024, 4, 27, 23, 25, 50), datetime.datetime(2024, 4, 27, 23, 29,56)),
    #(datetime.datetime(2024, 4, 27, 23, 31, 42), datetime.datetime(2024, 4, 27, 23, 35, 18)),
    #(datetime.datetime(2024, 4, 27, 23, 36, 30), datetime.datetime(2024, 4, 27, 23, 40, 38)),
    #(datetime.datetime(2024, 4, 27, 23, 41,42), datetime.datetime(2024, 4, 27, 23, 45,50)),
    #(datetime.datetime(2024, 4, 27, 23, 47, 26), datetime.datetime(2024, 4, 27, 23, 51, 34))

    # http/latency fault
    #(datetime.datetime(2024, 4, 28, 10, 41, 1), datetime.datetime(2024, 4, 28, 10, 43, 9)),
    #(datetime.datetime(2024, 4, 28, 10, 45, 33), datetime.datetime(2024, 4, 28, 10, 47, 49)),
    #(datetime.datetime(2024, 4, 28, 10, 48, 53), datetime.datetime(2024, 4, 28, 10, 50,29)),
    #(datetime.datetime(2024, 4, 28, 10, 55, 25), datetime.datetime(2024, 4, 28, 10, 57, 33)),
    #(datetime.datetime(2024, 4, 28, 10, 59, 49), datetime.datetime(2024, 4, 28, 11, 1, 49)),
    #(datetime.datetime(2024, 4, 28, 11, 3, 17), datetime.datetime(2024, 4, 28, 11, 5, 41)),
    #(datetime.datetime(2024, 4, 28, 11, 11, 33), datetime.datetime(2024, 4, 28, 11, 13, 11))
    
    # RED http fault experiment time
    #(datetime.datetime(2024, 4, 29, 10, 51, 5), datetime.datetime(2024, 4, 29, 10, 53, 17)),
    #(datetime.datetime(2024, 4, 29, 10, 54, 5), datetime.datetime(2024, 4, 29, 10, 56, 17)),
    #(datetime.datetime(2024, 4, 29, 10, 57, 26), datetime.datetime(2024, 4, 29, 10, 59, 23)),
    #(datetime.datetime(2024, 4, 29, 11, 0, 29), datetime.datetime(2024, 4, 29, 11, 2, 26)),
    #(datetime.datetime(2024, 4, 29, 11, 3, 11), datetime.datetime(2024, 4, 29, 11, 5, 23)),
    #(datetime.datetime(2024, 4, 29, 11, 6, 11), datetime.datetime(2024, 4, 29, 11, 8, 38)),
    #(datetime.datetime(2024, 4, 29, 11, 13, 48), datetime.datetime(2024, 4, 29, 11, 16,17))

    # RED LATENCY
    #(datetime.datetime(2024, 4, 29, 11, 20, 20), datetime.datetime(2024, 4, 29, 11, 24, 32)),
    #(datetime.datetime(2024, 4, 29, 11, 25, 38), datetime.datetime(2024, 4, 29, 11, 30, 5)),
    #(datetime.datetime(2024, 4, 29, 11, 34, 12), datetime.datetime(2024, 4, 29, 11, 38, 26)),
    #(datetime.datetime(2024, 4, 29, 11, 39, 8), datetime.datetime(2024, 4, 29, 11, 43, 20)),
    #(datetime.datetime(2024, 4, 29, 11, 44, 2), datetime.datetime(2024, 4, 29, 11, 48,29)),
    #(datetime.datetime(2024, 4, 29, 11, 49, 41), datetime.datetime(2024, 4, 29, 11, 53, 53)),
    #(datetime.datetime(2024, 4, 29, 11, 55, 8), datetime.datetime(2024, 4, 29, 11, 59, 2))
    
    
    #RED LATENCY and HTTP
    (datetime.datetime(2024, 4, 29, 12, 20, 8), datetime.datetime(2024, 4, 29, 12, 22, 20)),
    (datetime.datetime(2024, 4, 29, 12, 29, 56), datetime.datetime(2024, 4, 29, 12, 31, 53)),
    (datetime.datetime(2024, 4, 29, 12, 32, 50), datetime.datetime(2024, 4, 29, 12, 34, 47)),
    (datetime.datetime(2024, 4, 29, 12, 36, 8), datetime.datetime(2024, 4, 29,  12, 38, 50)),
    (datetime.datetime(2024, 4, 29, 12, 39, 41), datetime.datetime(2024, 4, 29,  12, 41,38)),
    (datetime.datetime(2024, 4, 29, 12, 42, 26), datetime.datetime(2024, 4, 29, 12, 45, 8)),
    (datetime.datetime(2024, 4, 29, 12, 46, 5), datetime.datetime(2024, 4, 29,  12, 48, 2))
]

# Loop over the defined time intervals
for index, (start_time, end_time) in enumerate(time_intervals):
    suffix = start_time.strftime('%Y%m%d%H%M%S') + "_" + end_time.strftime('%Y%m%d%H%M%S')
    
    # Call metric collection functions with unique filenames
    get_http_traffic(start_time, end_time, f'red_http_traffic_{suffix}.csv')
    get_error(start_time, end_time, f'red_error_rate_{suffix}.csv')
    get_duration(start_time, end_time, f'red_duration_{suffix}.csv')
    #get_latency(start_time, end_time, f'latency_{suffix}.csv')
    #get_saturation( start_time, end_time, f'red_saturation_{suffix}.csv')
