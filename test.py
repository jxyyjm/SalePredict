# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import datetime
import time

z = pd.DataFrame(np.zeros((5,3)), columns=['A','B', 'C'])
print(z)


a = pd.read_csv("/home/yujianmin/下载/AKaggleData/train.csv")
b = a['Date'][0:10]
print(b)
c = pd.to_datetime(b)
print(c[0].month)
s = b[0]
print(time.strptime(s,"%Y"))
