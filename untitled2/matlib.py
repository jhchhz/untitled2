# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,2*np.pi,50)

y = np.sin(x)
# plt.plot(x, y)
# plt.plot(x, y**3)
# plt.show()


plt.plot(x, y, 'b*-')

plt.plot(x, y**3, 'r--')

plt.show()


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(98, 99,130,0.01)
plt.plot(x, x**2)
plt.grid(True)  # 设置网格线
plt.xlabel("老丁头体重")
plt.ylabel("年份")
plt.show()
#
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.random.normal(0, 1, 1000)  # 1000个点的x坐标
# y = np.random.normal(0, 1, 1000) # 1000个点的y坐标
# c = np.random.rand(1000) #1000个颜色
# s = np.random.rand(100)*100 #100种大小
# plt.scatter(x, y, c=c, s=s,alpha=0.5)
# plt.grid(True)
# plt.show()

# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc")
plt.xlabel("中文文本", fontproperties=font)
x=[98,99,115,125,135]
y=[2016,2017,2018,2019,2020]
plt.xlabel("老丁头体重")
plt.ylabel("年")
plt.plot(x,y)
plt.show()
