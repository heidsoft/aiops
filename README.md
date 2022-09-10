# aiops

将机器学习应用于工程实践

## 特征值与特征向量

1. 特征值与特征向量是线性代数的核心内容，也是方阵的属性之一。可以用于降噪，特征提取，图形压缩
2. 特征值
3. 特征向量


## 特征值与特征向量的求解

1. 特征值就是特征方程的解
2. 求解特征值就是求特征方程的解
3. 求出特征值后，再求对应特征向量

## SVD奇异值分解

1. 将任意较为复杂的矩阵用更小，更简单的3个子矩阵相乘表示

## 机器学习关心的问题

1. 捕捉函数的变化趋势
2. 研究y 如何随着x而变
3. 趋势是通过求导和微分来实现的

### 导数

1. 导数是定义在连续函数的基础上 
2. 想要对函数求导，函数至少要有一段是连续的
3. “导数” 到是引导，导航到意思，它与函数上连续两个点之间的变化趋势，也就是变化的方向相关.
4. 通过导数在机器学习领域，可以得到标签y随特征x而变化的方向
5. 导数是针对一个变量而言的函数变化趋向
6. 多云（即多变量）的函数，它关于其中一个变量的导数为偏导数，此时保持其他变量恒定

### 梯度下降

1. 梯度下降已存在200多年，是机器学习的基础算法
2. 对多元函数的各参数求偏导数，然后把所求得的各个参数的偏导数以向量的形式写出来，就是“梯度”
3. 梯度下降的作用
- 3.1 机器学习的本质是找到最优的函数
- 3.2 如何衡量函数是最优解：尽量减小预测值和真值间的误差，也可以叫“损失值”
- 3.3 可以建立误差和模型参数之间的函数（最好是凸函数）
- 3.4 梯度下降能够引导我们走到凸函数的全局最低点，找到误差最小的参数


### 张量

1. 在机器学习中，把用于存储数据的结构叫张量，矩阵是二维数组，机器学习中就叫做2D张量
2. 张量是机器学习程序中的数字容器
3. 张量的维度称为轴（axis）
4. 轴的个数称为阶(rank)