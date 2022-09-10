import pandas as pd # 导入pandas 
from sklearn.model_selection import train_test_split # 导入sklearn 工具箱
from sklearn.linear_model import LinearRegression # 导入线性回归算法模型
df_housing = pd.read_csv("https://raw.githubusercontent.com/huangjia2019/house/master/house.csv")
df_housing.head # 显示加州房价数据
X = df_housing.drop("median_house_value",axis=1) # 删除最后一个字段，作为数据集合
y = df_housing.median_house_value # 构建标签数据
#from sklearn.model_selection import train_test_split # 导入sklearn 工具箱
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0) # 以80%/20%比例进行数据集的拆分
#from sklearn.linear_model import LinearRegression # 导入线性回归算法模型
model = LinearRegression() # 确定线性回归算法
model.fit(X_train,y_train) # 根据训练集数据，训练数据，拟合函数
y_pred = model.predict(X_test) # 预测验证集的y值
print("房价的真值（测试集）",y_test);
print("预测的房价（测试集）",y_pred);
print("给预测评分",model.score(X_test,y_test)); # 评估预测结果