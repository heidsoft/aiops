from datetime import datetime

from prometheus_api_client import PrometheusConnect, MetricsList, Metric, MetricSnapshotDataFrame, MetricRangeDataFrame
from prometheus_api_client.utils import parse_datetime

# Constants
# Embrace prometheus public URL
embrace_public_url='http://localhost:9090/metrics'


# Connect library to Embrace prometheus host
prom = PrometheusConnect(url=embrace_public_url)

# Get the list of all available metrics
# metrics = prom.all_metrics()
# print(metrics)

# Define start and end time
start_time = parse_datetime('1d')
end_time = parse_datetime('now')
# Define step in seconds
step_in_sec = 60 * 60;

# Query data
query = "100 - (avg by (instance) (rate(node_cpu_seconds_total{job='linux-node',mode='idle'}[1m])) * 100)"

metric_data = prom.custom_query_range(
    query,
    start_time=start_time,
    end_time=end_time,
    step=step_in_sec
)
print(metric_data)
print(len(metric_data))

# Use library to plot results
metric_object_list = MetricsList(metric_data)
my_metric_object = metric_object_list[1] # one of the metrics from the list
print(my_metric_object)
print(my_metric_object.metric_name)