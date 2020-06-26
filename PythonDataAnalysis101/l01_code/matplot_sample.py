import numpy as np
import matplotlib.pyplot as plt

# 基本配置
plt.figure(figsize = (10, 10), dpi = 80)
plt.xlim(-4.0, 4.0) # 坐标上下限
plt.ylim(-1.0, 1.0)
'''
plt.xticks(np.linspace(-4, 4, 9, endpoint = True))
plt.yticks(np.linspace(-1, 1, 5, endpoint = True))
'''
# 更直观的记号
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

# 画曲线
X = np.linspace(-np.pi, np.pi, 256,endpoint = True)
Cos,Sin = np.cos(X), np.sin(X)
plt.plot(X, Cos, color = 'blue', linewidth = 1.0, linestyle = '-', label = 'cos') # label添加图例
plt.plot(X, Sin, color = 'green', linewidth = 1.0, linestyle = '-', label = 'sin')
plt.legend(loc='upper left') # 图例位置左上角

# 移动坐标
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# 给特殊点加注释
t = 2*np.pi/3
plt.plot([t, t],[0, np.cos(t)], color = 'blue', linewidth = 2.5, linestyle = '--')
plt.scatter([t, ],[np.cos(t),], 50, color ='red')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
            xy = (t, np.cos(t)), xycoords = 'data',
            xytext = (-90, -50), textcoords = 'offset points', fontsize = 16,
            arrowprops = {'arrowstyle':'->', 'connectionstyle':'arc3,rad=.2'})
plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=2.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='red')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
            xy = (t, np.sin(t)), xycoords = 'data',
            xytext = (+10, +30), textcoords = 'offset points', fontsize = 16,
            arrowprops = {'arrowstyle':'->', 'connectionstyle':'arc3,rad=.2'})

# 显示图片
plt.show()
