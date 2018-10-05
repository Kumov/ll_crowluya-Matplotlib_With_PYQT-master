# 【Python】【matplotlib】键鼠响应事件 https://blog.csdn.net/guofei9987/article/details/78106492


# 事件绑定

'''

mpl_connect的参数：

参数	                    意义
‘button_press_event’	    按下鼠标
‘button_release_event’	释放鼠标
‘draw_event’    	        界面重新绘制
‘key_press_event’       	按下键盘
‘key_release_event’	    释放键盘
‘motion_notify_event’   	鼠标移动
‘pick_event’	            鼠标点选绘图对象
‘resize_event’
‘scroll_event’	        鼠标滚轴事件
‘figure_enter_event’	    鼠标进入figure
‘figure_leave_event’	    鼠标离开figure
‘axes_enter_event’	    鼠标进入Axes
‘axes_leave_event’	    鼠标离开Axes
‘close_event’	关闭图表
'''

import matplotlib.pyplot as plt

log = print


def on_key_press(event):
    log('进函数的')
    # log(event
    # 点击缩小
    # x 轴上下限变化
    # y 轴缩小上下限变化
    ax.xlabel = 'aaaa'
    log(event.key)


fig, ax = plt.subplots()
fig.canvas.mpl_connect('button_press_event', on_key_press)
plt.show()