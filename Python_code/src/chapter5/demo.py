import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

j = np.linspace(-np.pi, np.pi, 100)
k = np.cos(x)
plt.title("正弦和余弦函数图像")
plt.plot(x,y,color="red",label=r'$sin(x)$')
plt.plot(j,k,color="blue",linestyle="--",label=r'$cos(x)$')
plt.show()