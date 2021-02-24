import numpy as np

class Cluster:
    def __init__(self, mean):
        self.data = []  # 存放这一簇下的数据
        self.mean = mean  # 数据均值，即簇
        self.flag = 0  # 结束标志

    def get_mean(self):
        data = np.array(self.data)
        self.mean = np.array(self.mean)
        mean = data.mean(axis=0)  # 计算数组列表的均值坐标
        if (self.mean == mean).all():  # 判断原簇和现簇是否相等
            self.flag = 1
        else:
            self.flag = 0
        self.mean = mean
