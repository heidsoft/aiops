import pandas as pd
from sklearn.cluster import KMeans

# 模拟数据
data = {'Instance': ['instance1', 'instance2', 'instance3', 'instance4', 'instance5',
                     'instance6', 'instance7', 'instance8', 'instance9', 'instance10'],
        'CPU Usage (%)': [80, 50, 20, 90, 60, 30, 70, 40, 10, 85]}
"""
pandas DataFrame是一种二维的表格型数据结构，类似于电子表格或SQL表。
它可以存储不同类型的数据，并且可以对数据进行处理和操作，如筛选、排序、分组、聚合等。
DataFrame通常用于数据分析和数据科学中，特别是在处理结构化数据时非常有用
DataFrame由行和列组成，每列具有唯一的名称。
数据存储在行和列的交叉位置上。pandas提供了许多函数和方法来操作DataFrame，
如读取和写入数据、索引、重塑、合并、连接等。
pandas DataFrame是一个非常强大和灵活的工具，
广泛应用于数据分析、机器学习、深度学习、自然语言处理和其他数据科学领域。
"""
df = pd.DataFrame(data)

"""
KMeans是一种聚类算法，其目的是将一组点分成K个聚类。
该算法通过迭代将每个点分配到最近的聚类中心（基于欧几里得距离），
然后基于新的分配重新计算聚类中心。
该过程一直持续到聚类分配不再改变或达到最大迭代次数。

参数“n_clusters = 3”指定我们要将点分成3个聚类。
选择聚类数通常基于领域知识或使用诸如肘部法或轮廓分析等技术来找到最优聚类数。
"""
kmeans = KMeans(n_clusters=3)
"""
kmeans.fit()是KMeans算法中的一个方法，用于拟合模型并对数据进行聚类。
在使用KMeans算法进行聚类时，需要先实例化一个KMeans类，然后调用fit()方法对数据进行聚类。
fit()方法将根据指定的参数在数据上训练KMeans模型，以确定数据的聚类中心和分配到每个聚类的数据点。

具体来说，kmeans.fit()方法将执行以下操作：
1. 初始化KMeans算法的聚类中心。
2. 将数据点分配到最近的聚类中心。
3. 重新计算每个聚类的中心点。
4. 重复步骤2和3，直到聚类中心不再变化，或者达到最大迭代次数。
在完成训练之后，可以使用其他方法（如predict()）来对新数据进行聚类，或者使用已训练的模型进行预测。
"""
kmeans.fit(df[['CPU Usage (%)']])
df['Cluster'] = kmeans.labels_

# 告警阈值调整
for cluster_id in range(3):
    cluster_df = df[df['Cluster'] == cluster_id]
    """
    mean()方法是pandas DataFrame和Series对象中的一个方法，用于计算对象中所有数值类型数据的平均值。它返回一个标量，表示所有数值数据的平均值。
    具体来说，mean()方法计算以下内容：
    1. 对于DataFrame对象，计算每列数据的平均值。
    2. 对于Series对象，计算所有数据的平均值。
    mean()方法可用于DataFrame和Series对象，其语法如下：
    DataFrame.mean(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
    Series.mean(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
    其中，axis参数指定计算的轴方向，skipna参数指定是否跳过缺失值，level参数指定多级索引的级别，numeric_only参数指定是否仅计算数值数据，**kwargs参数为其他可选参数。
    总之，mean()方法用于计算DataFrame和Series对象中数值数据的平均值，是pandas中一个常用的统计函数之一。
    """
    mean_usage = cluster_df['CPU Usage (%)'].mean()
    if mean_usage >= 80:
        threshold = 90
    elif mean_usage >= 50:
        threshold = 70
    else:
        threshold = 50
    print(f"Cluster {cluster_id}: Mean CPU usage = {mean_usage}%, Threshold = {threshold}%")

"""
pandas Series是一种一维的标签型数组数据结构，类似于Python中的列表或数组。每个Series对象都由两个数组组成，一个数组存储数据值，另一个数组存储标签（索引）。Series对象可以存储任何类型的数据，包括数值、字符串、布尔值等。

Series对象的索引可以是整数、标签或多级索引。pandas提供了许多函数和方法来操作Series对象，如索引、切片、过滤、排序、分组、聚合等。Series对象还可以用于与NumPy数组和其他pandas数据结构进行交互。

创建Series对象的方式包括从Python列表、NumPy数组、Python字典等对象中创建，或者使用pandas提供的一些函数和方法来创建。pandas Series是一个非常灵活和方便的数据结构，广泛应用于数据分析、机器学习、深度学习、自然语言处理和其他数据科学领域。
"""

"""
Prometheus中的Series是一种时间序列数据，由时间戳和相应的值组成。在Prometheus中，Series是数据模型的核心概念之一，用于表示一段时间内某个指标的变化情况。可以通过PromQL查询语言来查询和操作Series。

Prometheus中的Series对象具有以下特点：

1. 时间序列数据：Series表示一段时间内某个指标的变化情况，其中时间戳是Series的一个重要组成部分。
2. 多维标签：Series可以通过多维标签来区分不同的指标和其它维度，例如服务名、实例名、端口号等，这使得查询和过滤数据变得更加灵活和方便。
3. 持久化存储：Prometheus会将采集到的时间序列数据存储在本地磁盘上，以便后续查询和分析。

使用Prometheus中的Series，可以通过PromQL查询语言来进行数据查询、过滤、聚合和可视化等操作。
同时，Prometheus还提供了一些API和CLI工具，使得在应用程序中使用Series也变得更加便捷。
例如，可以使用Prometheus的Python客户端库来访问和操作Series数据。
"""