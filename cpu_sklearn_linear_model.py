from sklearn.linear_model import LinearRegression

# 读入数据
from sklearn.metrics import mean_squared_error, r2_score
import datetime
import time
from pprint import pprint
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


# Prometheus API地址
from cpu_machine_leanring import kmeans

url = "http://localhost:9090/api/v1/query_range"

# 查询语句
query = "100 - (avg by (instance) (rate(node_cpu_seconds_total{job='linux-node',mode='idle'}[1m])) * 100)"

# 中国时间字符串
china_start_time_str = '2023-05-21 10:00:00'
china_end_time_str = '2023-05-21 22:00:00'

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
series = json.loads(response.text)['data']['result']

#将Series转换为DataFrame
data = pd.DataFrame(columns=['timestamp', 'value'])
for s in series:
    df_temp = pd.DataFrame(s['values'], columns=['timestamp', 'value'])
    df_temp['instance'] = s['metric']['instance']
    """
    pd.concat用于将多个Pandas数据帧（DataFrame）或序列（Series）沿着指定的轴（axis）连接在一起，生成一个新的数据帧或序列。它可以用于数据的合并、拼接和连接，常用于数据清洗、数据预处理和数据分析等领域。其中，axis参数默认为0，表示沿着行方向进行连接，如果设置为1，则表示沿着列方向进行连接。
    """
    data = pd.concat([data, df_temp])
    print(data)

# 按实例分组
grouped = data.groupby('instance')

# 定义ARIMA模型参数
p = 1
d = 1
q = 1

# 预测未来10个时间步长的值
n_steps = 10

# 针对每个实例进行预测
for instance, group in grouped:
    # 获取时间序列数据
    ts = group['value']

    # 拟合ARIMA模型
    model = ARIMA(ts, order=(p, d, q))
    model_fit = model.fit()

    # 进行未来10个时间步长的预测
    forecast = model_fit.forecast(steps=n_steps)

    # 打印预测结果
    print(f'Instance: {instance}')
    print(forecast)
