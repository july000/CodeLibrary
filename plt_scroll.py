import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Plot Example')
ax.set_xlabel('X Axis Label')
ax.set_ylabel('Y Axis Label')
ax.grid(True)

def on_scroll(event):
    axtemp = event.inaxes
    x_min, x_max = axtemp.get_xlim()
    y_min, y_max = axtemp.get_ylim()
    x_mid = (x_min + x_max)/2.0
    y_mid = (y_min + y_max)/2.0
    if event.button == 'up':
        # 放大
        scale_factor = 1/1.5
    elif event.button == 'down':
        # 缩小
        scale_factor = 1.5
    else:
        # 没有滚动事件
        scale_factor = 1
    axtemp.set_xlim([x_mid - (x_mid - x_min)*scale_factor, x_mid + (x_max - x_mid)*scale_factor])
    axtemp.set_ylim([y_mid - (y_mid - y_min)*scale_factor, y_mid + (y_max - y_mid)*scale_factor])
    plt.draw()

fig.canvas.mpl_connect('scroll_event', on_scroll)
plt.show()