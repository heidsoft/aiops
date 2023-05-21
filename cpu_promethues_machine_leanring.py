import datetime
import time
from pprint import pprint

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

# Prometheus API地址
from cpu_machine_leanring import kmeans

url = "http://localhost:9090/api/v1/query_range"

# 查询语句
query = "100 - (avg by (instance) (rate(node_cpu_seconds_total{job='linux-node',mode='idle'}[1m])) * 100)"

# 中国时间字符串
china_start_time_str = '2023-05-21 10:00:00'
china_end_time_str = '2023-05-21 17:00:00'

# 将字符串转换为 datetime 对象
china_start_time = datetime.datetime.strptime(china_start_time_str, '%Y-%m-%d %H:%M:%S')
china_end_time = datetime.datetime.strptime(china_end_time_str, '%Y-%m-%d %H:%M:%S')

# 将 datetime 对象转换为 UTC 时间
utc_stat_time = china_start_time - datetime.timedelta(hours=8)
utc_end_time = china_end_time - datetime.timedelta(hours=8)
# 将 UTC 时间转换为 RFC3339 时间
rfc3339_start_time = utc_stat_time.isoformat() + 'Z'
rfc3339_end_time = utc_end_time.isoformat() + 'Z'
print(rfc3339_start_time)
print(rfc3339_end_time)


def utc2local(utc_st):
    """UTC时间转本地时间（+8:00)"""
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st


step_in_sec = 60
# 构建请求体
payload = {
    "query": query,
    "start": rfc3339_start_time,
    "end": rfc3339_end_time,
    "step": step_in_sec
}
print(payload)
# 发送请求
response = requests.get(url, params=payload)
print(response)

# 解析响应
data = json.loads(response.text)
print(data)
series = data['data']['result']
pprint(series)
# 打印Series
for s in series:
    print(s['metric']['instance'], s['values'])

# 要使用pandas进行分析，可以将Series转换为DataFrame。以下是一个示例代码片段，用于将Prometheus中的CPU使用率Series转换为DataFrame并计算平均值和标准差：


#
# # 将Series转换为DataFrame
df = pd.DataFrame(columns=['timestamp', 'value'])
for s in series:
    df_temp = pd.DataFrame(s['values'], columns=['timestamp', 'value'])
    df_temp['instance'] = s['metric']['instance']
    """
    pd.concat用于将多个Pandas数据帧（DataFrame）或序列（Series）沿着指定的轴（axis）连接在一起，生成一个新的数据帧或序列。它可以用于数据的合并、拼接和连接，常用于数据清洗、数据预处理和数据分析等领域。其中，axis参数默认为0，表示沿着行方向进行连接，如果设置为1，则表示沿着列方向进行连接。
    """
    df = pd.concat([df, df_temp])
print(df)

kmeans.fit(df[['value']])
labels = kmeans.labels_
print(labels)
for cluster_id in range(3):
    cluster_df = df[df['value'] == cluster_id]
    mean_usage = cluster_df['value'].mean()
    if mean_usage >= 80:
        threshold = 90
    elif mean_usage >= 50:
        threshold = 70
    else:
        threshold = 50
    print(threshold)

plt.scatter(df['timestamp'],df['instance'], c=labels)
plt.title('KMeans Clustering')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

