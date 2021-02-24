from cluster import *
import numpy as np

class ClusterList:
    def __init__(self, data):
        self.all_data = data
        self.cluster_list = []
        self.flag = 0
        self.init_cluster_list()
        self.set_cluster_list()

    def init_cluster_list(self):  # 初始化簇
        data = np.array(self.all_data.data)
        k = self.all_data.num
        delta = (data.max(axis=0) - data.min(axis=0)) / k
        if len(self.cluster_list) == 0:
            for i in range(k):
                cluster = Cluster(data.min(axis=0) + delta * i)
                self.cluster_list.append(cluster)

    def set_cluster_list(self):  # 计算簇直至簇不变
        # 初始化数据，得到
        data = np.array(self.all_data.data)
        max_data = data.max(axis=0)  # 数组最大值
        min_data = data.min(axis=0)  # 数据最小值
        origin_min_dist = np.sqrt(np.sum(np.square(max_data - min_data)))  # 初始欧式距离
        # 多次循环直至簇不变
        while self.flag == 0:
            # 每次循环清空簇数组
            for cluster in self.cluster_list:
                cluster.data = []  # 将数据按最小距离放进簇数组
            for data in self.all_data.data:
                data = np.array(data)  # 将数组转换成np数组
                min_dist = origin_min_dist  # 初始化最小距离
                index = 0
                for cluster in self.cluster_list:
                    mean_data = np.array(cluster.mean)
                    dist = np.sqrt(np.sum(np.square(data - mean_data)))
                    if dist <= min_dist:
                        min_dist = dist
                        index = self.cluster_list.index(cluster)
                self.cluster_list[index].data.append(data)
            #根据新放入的簇数组计算簇
            end_flag = 1
            for cluster in self.cluster_list:
                cluster.get_mean()
                end_flag *= cluster.flag
            self.flag = end_flag
        #输出结果
        i = 0
        for cluster in self.cluster_list:
            i += 1
            print("第", i, "类簇为：", cluster.mean.tolist())
            print("第", i, "类结果为：", np.array(cluster.data).tolist())

