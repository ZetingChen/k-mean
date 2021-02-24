import numpy as np

class Data:
    def __init__(self, path, num):
        self.data = []  # 所有数据
        self.num = num  # 簇的类
        self.get_data(path)

    def get_data(self, path):
        with open(path, 'r') as f:
            for line in f.readlines():  # 按行读取数据
                line = line.strip('\n').split(' ')  # 以空格分隔数据
                line = [float(x) for x in line]  # 将字符列表转化为数组列表
                self.data.append(line)
        self.data = np.array(self.data)  # 转换成np数组
