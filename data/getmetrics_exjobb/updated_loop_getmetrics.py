
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
