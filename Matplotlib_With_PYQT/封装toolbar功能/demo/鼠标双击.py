import matplotlib.pyplot as plt
fig = plt.figure()
def onclick(event):
    if event.dblclick:
         print (event.button)

connection_id = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()